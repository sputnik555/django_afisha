import urllib.parse
from os.path import basename

import requests
from bs4 import BeautifulSoup
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, Image

URL = 'https://github.com/devmanorg/where-to-go-places/tree/master/places'


def add_place_in_db(place_data):
    if not Place.objects.filter(title=place_data['title']):
        place = Place(
            title=place_data['title'],
            description_short=place_data['description_short'],
            description_long=place_data['description_long'],
            latitude=place_data['coordinates']['lat'],
            longitude=place_data['coordinates']['lng']
        )
        place.save()
        img_order = 0
        for image_url in place_data['imgs']:
            response = requests.get(image_url)
            response.raise_for_status()
            content = ContentFile(response.content)
            image = Image()
            image.image.save(basename(image_url), content, save=False)
            image.place = place
            image.order = img_order
            image.save()
            img_order += 1
    else:
        print('уже есть')


def get_place_urls():
    try:
        response = requests.get(url)
        response.raise_for_status()
    except (requests.HTTPError, requests.ConnectTimeout, requests.ConnectionError):
        print('Ошибка при загрузке данных')
        exit()
    soup = get_soap(URL)
    a_tags = soup.select("div.py-2 a.js-navigation-open")
    place_urls = [urllib.parse.urljoin(url, a_tag['href']) for a_tag in a_tags]
    return place_urls


def get_place_raw_url(place_url):
    soup = get_soap(place_url)
    a_tag_raw_url = soup.select_one('a#raw-url')
    place_raw_url = urllib.parse.urljoin(place_url, a_tag_raw_url['href'])
    return place_raw_url


def get_soap(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except (requests.HTTPError, requests.ConnectTimeout, requests.ConnectionError):
        print('Ошибка при загрузке данных')
        exit()
    return BeautifulSoup(response.text, 'lxml')


class Command(BaseCommand):
    def handle(self, *args, **options):
        for place_url in get_place_urls():
            try:
                response = requests.get(get_place_raw_url(place_url))
                response.raise_for_status()
            except (requests.HTTPError, requests.ConnectTimeout, requests.ConnectionError):
                print('Ошибка при загрузке данных')
                exit()
            add_place_in_db(response.json())