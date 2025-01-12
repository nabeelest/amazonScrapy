
class Product:
    def __init__(self, title, total_reviews, price, image_url, scrape_date):
        self.title = title
        self.total_reviews = total_reviews
        self.price = price
        self.image_url = image_url
        self.scrape_date = scrape_date

    def to_dict(self):
        return {
            "title": self.title,
            "total_reviews": self.total_reviews,
            "price": self.price,
            "image_url": self.image_url,
            "scrape_date": self.scrape_date
        }
