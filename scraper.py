from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import json
class AmazonScraper:
    def __init__(self):
        # Set up Chrome options with headers to reduce bot detection
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    def fetch_products(self, query, pages=1):
        base_url = "https://www.amazon.com/s?k="
        self.driver.get(base_url + query)
        products = []

        for page in range(1, pages + 1):
            print(f"Scraping page {page} for query: {query}")
            time.sleep(2)  # Wait for page to load
            
            items = self.driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
            for item in items:
                try:
                    title = item.find_element(By.XPATH, ".//div[@data-cy='title-recipe']").text
                    print(title)
                    total_reviews = item.find_element(By.CSS_SELECTOR, ".a-size-base").text if self._check_element(item, ".a-size-base") else "N/A"
                    # price = item.find_element(By.CSS_SELECTOR, ".a-price span.a-offscreen").text if self._check_element(item, ".a-price span.a-offscreen") else "N/A"
                    price = item.find_element(By.XPATH,"//span[@class='a-offscreen']")
                    if price:
                        price = str(price.get_attribute("innerText"))
                    image_url = item.find_element(By.CSS_SELECTOR, ".s-image").get_attribute("src")
                    
                    product = {
                        "title": title,
                        "total_reviews": total_reviews,
                        "price": price,
                        "image_url": image_url,
                        "scrape_date": time.strftime("%Y-%m-%d %H:%M:%S")
                    }
                    products.append(product)
                except Exception as e:
                    print(f"Error scraping item: {e}")
            
            try:
                # Move to the next page
                next_button = self.driver.find_element(By.XPATH, "//a[contains(@class, 's-pagination-next')]")
                next_button.click()
                time.sleep(2)
            except Exception as e:
                print(f"No more pages or error navigating: {e}")
                break
        # self.save_to_json(query, products)
        return products

    # def save_to_json(self, query, products):
    #     # Create the output directory if it doesn't exist
    #     output_dir = "public/output"
    #     os.makedirs(output_dir, exist_ok=True)

    #     filename = os.path.join(output_dir, f"{query.replace(' ', '_').lower()}.json")
    #     try:
    #         with open(filename, "w", encoding="utf-8") as file:
    #             json.dump(products, file, indent=4, ensure_ascii=False)
    #         print(f"Products saved to {filename}")
    #     except Exception as e:
    #         print(f"Error saving to JSON: {e}")

    def _check_element(self, element, selector):
        """
        Helper function to check if an element exists for a given selector
        """
        try:
            element.find_element(By.CSS_SELECTOR, selector)
            return True
        except:
            return False

    def close(self):
        self.driver.quit()


# # Example Usage
# if __name__ == "__main__":
#     scraper = AmazonScraper()
#     try:
#         products = scraper.fetch_products("laptops", pages=2)
#         for product in products:
#             print(product)
#     finally:
#         scraper.close()
