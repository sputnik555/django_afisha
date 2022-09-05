from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from places.models import Place


def render_main_page(request):
    places = Place.objects.all()
    context = {'geo_json': get_geodata(places)}
    return render(request, 'index.html', context)


def get_geodata(places):
    features = []
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
    geo_data = {
        "type": "FeatureCollection",
        "features": features,
    }
    return geo_data


def get_place_info(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    images = place.images.order_by('order')
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
