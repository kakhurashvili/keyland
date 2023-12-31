# Generated by Django 4.2.2 on 2023-07-11 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0011_banner_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='image_height',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='banner',
            name='image_width',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
