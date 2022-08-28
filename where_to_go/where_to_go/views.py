from django.shortcuts import render
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
