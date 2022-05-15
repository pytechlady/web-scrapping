import requests
from bs4 import BeautifulSoup
from collections import Counter
from utils.utils import common_words


class RequestUrl:
    # initialise the requests.get for the provided URL
    def __init__(self):
        self.res = input("Please enter the website to analyze: ")
        self.url = requests.get(self.res).text

        with open("log.csv", "a") as fd:
            fd.write(f"{self.res}\n")
            fd.close()

    # using the Beautiful soup method to get the text content of the website
    def check_url(self):
        soup = BeautifulSoup(self.url, 'lxml').get_text().replace('\n', '').replace(u'\xa0', u' ').lower()
        soup_filter = soup.split()
        return soup_filter

    # function to filter the text in the website and use only the text not in the common_words list
    def filter_common_word(self):
        arr = []
        for items in self.check_url():
            if items.isalpha() and items not in common_words:
                arr.append(items)
        return arr

    # function to pick the first 7 words that occurs most in the website to appear on the pie chart
    def count_occur(self):
        count = Counter(self.filter_common_word())
        new_arr = count.most_common(7)
        return dict(new_arr)