# Generated by Django 4.1 on 2022-08-29 08:43

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_image_options_remove_image_number_image_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(),
        ),
    ]
