# Generated by Django 4.2.2 on 2023-07-11 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0008_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='size_value',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
