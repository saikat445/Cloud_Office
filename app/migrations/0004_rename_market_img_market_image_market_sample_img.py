# Generated by Django 3.2.13 on 2023-04-23 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_market_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='market_image',
            old_name='market_img',
            new_name='market_sample_img',
        ),
    ]