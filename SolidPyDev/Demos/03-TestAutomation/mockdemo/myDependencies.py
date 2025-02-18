import time

# A constant to mock.
BASE_URL = "https://example.com/api/products"


# A function to mock.
def calculate_meaning_of_life():
    time.sleep(60)
    return 42


# A class with methods to mock.
class DataLoader:

    def __init__(self):
        self.delay = 60

    def load_product(self):
        time.sleep(self.delay)
        return 'Bugatti Divo'

    def load_great_football_team(self):
        time.sleep(self.delay)
        return 'Swansea City'