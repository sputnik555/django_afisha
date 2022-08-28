from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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
                    "detailsUrl": "static/places/roofs24.json"
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
    return HttpResponse(place.title)
