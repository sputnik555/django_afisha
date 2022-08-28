from django.db import models


# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()
    latitude = models.DecimalField(max_digits=16, decimal_places=14)
    longitude = models.DecimalField(max_digits=17, decimal_places=14)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField()
    place = models.ForeignKey(Place, models.SET_NULL, null=True, related_name='images')
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['order']
