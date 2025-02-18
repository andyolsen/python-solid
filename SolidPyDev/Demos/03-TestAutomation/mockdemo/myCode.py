from mockdemo.myDependencies import BASE_URL
from mockdemo.myDependencies import calculate_meaning_of_life
from mockdemo.myDependencies import DataLoader


def build_url(**kwargs):
    url = BASE_URL
    if len(kwargs) != 0:
        url += "?"
        for k, v in kwargs.items():
            url += f"{k}={v}&"
        url = url.rstrip('&')
    return url


def get_meaning_of_life():
    result = calculate_meaning_of_life()
    return 'The meaning of life is ' + str(result)


def get_product():
    dataLoader = DataLoader()
    result = dataLoader.load_product()
    return 'Product is ' + str(result)