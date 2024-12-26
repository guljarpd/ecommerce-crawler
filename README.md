# Ecommerce Product URL Crawler

This is a scalable web crawler designed to extract product URLs from various e-commerce websites. The crawler supports static and dynamic content extraction and can be run on multiple domains concurrently.

## Features
- Asynchronous crawling for fast and efficient scraping.
- Selenium support for websites with dynamic content (e.g., infinite scrolling, AJAX).
- Retry mechanism with exponential backoff for handling transient errors.
- Output product URLs into a structured JSON file.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/guljarpd/ecommerce-crawler.git
   cd ecommerce-crawler

2. Install by pip
   ```bash
   pip install -r crawler/requirements.txt

3. Run 
   ```bash
   python crawler/crawler.py
