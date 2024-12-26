import asyncio
import aiohttp
from aiohttp import ClientSession
import json
import time
import random
from config import DOMAINS, RETRY_LIMIT, RETRY_BACKOFF, OUTPUT_FILE, DYNAMIC_SITES
from utils import extract_product_urls_from_page
from handlers import extract_product_urls_with_selenium

# Asynchronous function to crawl a single URL (static pages)
async def crawl_static_page(url: str, session: ClientSession):
    async with session.get(url) as response:
        page_content = await response.text()
        return extract_product_urls_from_page(page_content, url)

# Main crawling function to handle both static and dynamic sites
async def crawl_domain(domain: str, session: ClientSession, use_selenium=False):
    visited_urls = set()
    product_urls = set()
    homepage_url = f"https://{domain}"

    # Simple retry mechanism
    retries = 0
    while retries < RETRY_LIMIT:
        try:
            print(f"Crawling {homepage_url}...")
            
            # Crawl static page for most domains
            if not use_selenium:
                product_urls.update(await crawl_static_page(homepage_url, session))
            else:
                product_urls.update(extract_product_urls_with_selenium(homepage_url))

            # Add more pages if needed (pagination or linked categories)
            # Here, we simply simulate additional pages for crawling
            for i in range(2, 5):
                product_urls.update(await crawl_static_page(f"{homepage_url}?page={i}", session))

            break  # If successful, exit the retry loop
        except Exception as e:
            retries += 1
            print(f"Error crawling {homepage_url}: {e}. Retrying {retries}/{RETRY_LIMIT}...")
            time.sleep(RETRY_BACKOFF * retries)

    return product_urls

# Main asynchronous function to crawl multiple domains concurrently
async def crawl_multiple_domains(domains: list):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for domain in domains:
            use_selenium = domain in DYNAMIC_SITES  # Use Selenium for dynamic content
            tasks.append(crawl_domain(domain, session, use_selenium))

        results = await asyncio.gather(*tasks)

        # Save results to a JSON file
        domain_product_urls = {domain: list(product_urls) for domain, product_urls in zip(domains, results)}
        with open(OUTPUT_FILE, 'w') as outfile:
            json.dump(domain_product_urls, outfile, indent=4)

# Run the crawler
if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(crawl_multiple_domains(DOMAINS))
    end_time = time.time()

    print(f"Crawling completed in {end_time - start_time:.2f} seconds.")