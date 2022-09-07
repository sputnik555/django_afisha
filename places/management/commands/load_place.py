import urllib.parse
from os.path import basename

import requests
from bs4 import BeautifulSoup
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, Image

URL = 'https://github.com/devmanorg/where-to-go-places/tree/master/places'


def add_place_in_db(place_data):
    place, _ = Place.objects.get_or_create(
        title=place_data['title'],
        defaults={
            'description_short': place_data['description_short'],
            'description_long': place_data['description_long'],
            'latitude': place_data['coordinates']['lat'],
            'longitude': place_data['coordinates']['lng'],
        }
    )

    for image in place.images.all():
        image.image.delete()
        image.delete()

    for img_order, image_url in enumerate(place_data['imgs']):
        response = requests.get(image_url)
        response.raise_for_status()
        Image.objects.update_or_create(
            image=basename(image_url),
            defaults={
                'image': ContentFile(response.content, name=basename(image_url)),
                'place': place,
                'order': img_order
            }
        )


def get_place_urls():
    response = requests.get(URL)
    response.raise_for_status()
    soup = get_soap(URL)
    a_tags = soup.select("div.py-2 a.js-navigation-open")
    place_urls = [urllib.parse.urljoin(URL, a_tag['href']) for a_tag in a_tags]
    return place_urls


def get_place_raw_url(place_url):
    soup = get_soap(place_url)
    a_tag_raw_url = soup.select_one('a#raw-url')
    place_raw_url = urllib.parse.urljoin(place_url, a_tag_raw_url['href'])
    return place_raw_url


def get_soap(url):
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'lxml')


class Command(BaseCommand):
    help = 'Скрипт загрузки данных в JSON-формате в базу данных'

    def add_arguments(self, parser):
        parser.add_argument('url', nargs='?', help='URL *.json файла для загрузки')

    def handle(self, *args, **options):
        if options['url']:
            response = requests.get(options['url'])
            response.raise_for_status()
            add_place_in_db(response.json())
            return

        for place_url in get_place_urls():
            response = requests.get(get_place_raw_url(place_url))
            response.raise_for_status()
            add_place_in_db(response.json())
