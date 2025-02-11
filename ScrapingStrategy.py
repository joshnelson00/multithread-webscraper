from abc import ABC, abstractmethod

class ScrapingStrategy(ABC):

    @abstractmethod
    def fetch_data(self, url):
        pass

    @abstractmethod
    def parse_data(self, url):
        pass