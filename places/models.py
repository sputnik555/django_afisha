from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    description_short = models.TextField(verbose_name='Описание краткое', blank=True)
    description_long = HTMLField(verbose_name='Описание полное', blank=True)
    latitude = models.DecimalField(verbose_name='Широта', max_digits=16, decimal_places=14)
    longitude = models.DecimalField(verbose_name='Долгота', max_digits=17, decimal_places=14)

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_title')
        ]

class Image(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey(
        Place,
        models.SET_NULL,
        verbose_name='Место',
        null=True,
        blank=True,
        related_name='images'
    )
    order = models.PositiveIntegerField(
        verbose_name='Порядок',
        default=0
    )

    def __str__(self):
        if self.place:
            return '{} [{}]'.format(self.image, self.place.title)
        else:
            return str(self.image)

    class Meta:
        ordering = ['order']
