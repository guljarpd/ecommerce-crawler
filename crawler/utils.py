import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Function to extract product URLs based on common patterns
def extract_product_urls_from_page(page_content, base_url):
    """
    Extract product URLs from a page using common patterns like '/product/' or '/item/'.

    Args:
        page_content (str): The HTML content of the page.
        base_url (str): The base URL for resolving relative links.

    Returns:
        set: A set of product URLs.
    """
    soup = BeautifulSoup(page_content, 'html.parser')
    product_urls = set()

    # Define common URL patterns for product pages
    patterns = ["/product/", "/item/", "/p/"]

    # Look for all anchor tags with href attributes
    for link in soup.find_all('a', href=True):
        href = link['href']
        
        # Check if the link matches any of the patterns
        if any(pattern in href for pattern in patterns):
            full_url = urljoin(base_url, href)  # Normalize the URL
            product_urls.add(full_url)
    
    return product_urls