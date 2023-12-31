# Generated by Django 4.2.2 on 2023-07-13 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0020_alter_banner_subtitle_alter_banner_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner_second',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('font1', models.CharField(max_length=100)),
                ('heading', models.CharField(max_length=100)),
                ('button_text', models.CharField(max_length=100)),
                ('button_link', models.CharField(max_length=200)),
                ('coupon_text', models.CharField(max_length=100)),
                ('coupon_discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_url', models.URLField()),
            ],
        ),
    ]
