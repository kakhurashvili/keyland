# Generated by Django 4.2.2 on 2023-07-11 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0019_alter_banner_subtitle_alter_banner_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='subtitle',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]