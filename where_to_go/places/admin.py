from django.contrib import admin
from django.utils.html import format_html
from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    fields = ('image', 'preview', 'number')
    readonly_fields = ['preview']

    def preview(self, obj):
        if obj.image.width > 200:
            width = 200
            height = obj.image.height * (200 / obj.image.width)
        else:
            width = obj.image.width
            height = obj.image.height
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=width,
            height=height)
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
