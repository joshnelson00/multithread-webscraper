from ScrapingStrategy import ScrapingStrategy
from abc import abstractmethod
class JSONScraper(ScrapingStrategy):

    @abstractmethod
    def fetch_data(self, url):
        pass

    @abstractmethod
    def parse_data(self, url):
        pass