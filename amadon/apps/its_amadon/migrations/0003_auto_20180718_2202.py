# Generated by Django 2.0.7 on 2018-07-19 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('its_amadon', '0002_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]