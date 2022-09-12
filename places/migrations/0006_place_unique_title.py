# Generated by Django 4.1 on 2022-09-12 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_image_image_alter_image_order_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='place',
            constraint=models.UniqueConstraint(fields=('title',), name='unique_title'),
        ),
    ]
