# Generated by Django 4.2.2 on 2023-07-04 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='total_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
