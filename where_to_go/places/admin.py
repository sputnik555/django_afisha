from django.contrib import admin
from places.models import Place, Image

# Register your models here.
admin.site.register(Image)


class ImageInline(admin.TabularInline):
    model = Image
    fields = ('image', 'number')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
