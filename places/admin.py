from adminsortable2.admin import SortableStackedInline, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html
from places.models import Place, Image


class ImageInline(SortableStackedInline):
    model = Image
    fields = ('image', 'preview', 'order')
    readonly_fields = ['preview']

    def preview(self, obj):
        return format_html('<img src="{}" style="max-height: 200px"/>'.format(obj.image.url))


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ('image', 'place')
