# Generated by Django 4.2.2 on 2023-07-07 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(editable=False, max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
