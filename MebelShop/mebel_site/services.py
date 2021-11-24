from MebelShop.settings import API_URL
import requests as re
def get_list_category():
    url = API_URL + 'category/'
    return re.get(url).json()['items']