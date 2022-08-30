import requests
import urllib.parse
from bs4 import BeautifulSoup

def check_for_redirect(response):
    if response.history:
        raise requests.HTTPError


def get_place_urls():
    url = 'https://github.com/devmanorg/where-to-go-places/tree/master/places'
    try:
        response = requests.get(url)
        response.raise_for_status()
        check_for_redirect(response)
    except (requests.HTTPError, requests.ConnectTimeout, requests.ConnectionError):
        print('Ошибка при загрузке данных')
        exit()
    soup = BeautifulSoup(response.text, 'lxml')
    a_tags = soup.select("div.py-2 a.js-navigation-open")
    place_urls = [urllib.parse.urljoin(url, a_tag['href']) for a_tag in a_tags]
    return place_urls


def get_place_raw_url(place_url):
    try:
        response = requests.get(place_url)
        response.raise_for_status()
        check_for_redirect(response)
    except (requests.HTTPError, requests.ConnectTimeout, requests.ConnectionError):
        print('Ошибка при загрузке данных')
        exit()
    soup = BeautifulSoup(response.text, 'lxml')
    a_tag_raw_url = soup.select_one('a#raw-url')
    place_raw_url = urllib.parse.urljoin(place_url, a_tag_raw_url['href'])
    return place_raw_url


if __name__ == '__main__':

    for place_url in get_place_urls():
        print(get_place_raw_url(place_url))

    exit()
        # response = requests.get(place_url)
        # soup = BeautifulSoup(response.text, 'lxml')
        # a_tag_rawurl = soup.select_one('a#raw-url')
        # json_raw_url = urllib.parse.urljoin(place_url, a_tag_rawurl['href'])
        # response = requests.get(json_raw_url)
        # print(response.json())

