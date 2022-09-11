from os.path import basename

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


def add_place_in_db(place_data):
    place, created = Place.objects.get_or_create(
        title=place_data['title'],
        defaults={
            'description_short': place_data.get('description_short', ''),
            'description_long': place_data.get('description_long', ''),
            'latitude': place_data['coordinates']['lat'],
            'longitude': place_data['coordinates']['lng'],
        }
    )
    if not created:
        print('Object "{}" already exist'.format(place_data['title']))
        return

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


class Command(BaseCommand):
    help = 'Скрипт загрузки данных в JSON-формате в базу данных'

    def add_arguments(self, parser):
        parser.add_argument('url', nargs='?', help='URL *.json файла для загрузки')

    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()
        add_place_in_db(response.json())
