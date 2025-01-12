
from input_reader import read_queries
from scraper import AmazonScraper
from output_writer import save_to_json
import time

def main():
    queries = read_queries()
    scraper = AmazonScraper()

    for query in queries:
        print(f"Scraping data for: {query}")
        products = scraper.fetch_products(query)
        save_to_json(query, products)
        time.sleep(5)  # Wait before starting a new query
    
    scraper.close()

if __name__ == "__main__":
    main()
