# List of domains to crawl
DOMAINS = [
    'amazon.in', 'flipkart.com', 'snapdeal.com', 'myntra.com', 'ajio.com'
]

# Retry settings
RETRY_LIMIT = 5
RETRY_BACKOFF = 2  # Exponential backoff for retries (in seconds)

# Crawl delay and rate-limiting settings (in seconds)
RATE_LIMIT = 1  # 1 second delay between requests to the same domain

# Output file for saving product URLs
OUTPUT_FILE = './crawler/output/results.json'

# Whether to use Selenium for dynamic content (e.g., Amazon, Flipkart)
DYNAMIC_SITES = ['amazon.in', 'flipkart.com']