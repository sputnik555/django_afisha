from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from places.models import Place


def render_main_page(request):
    context = {'geo_json': get_geojson()}
    return render(request, 'index.html', context)


def get_geojson():
    features = []
    places = Place.objects.all()
    for place in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse(get_place_info, args=[place.id])
                }
            }
        )
    geo_json = {
        "type": "FeatureCollection",
        "features": features,
    }
    return geo_json


def get_place_info(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    images = place.images.all().order_by('number')
    place_dict = {
        'title': place.title,
        'imgs': [img.image.url for img in images],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude,
        }
    }
    return JsonResponse(place_dict)
