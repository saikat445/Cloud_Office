# Generated by Django 3.2.13 on 2023-05-06 12:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_testsample'),
    ]

    operations = [
        migrations.CreateModel(
            name='test_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receivedno', models.CharField(max_length=50)),
                ('samplename', models.CharField(max_length=50)),
                ('receivedfrom', models.CharField(max_length=50)),
                ('Mfg', models.CharField(max_length=50)),
                ('test_sample_img', models.ImageField(upload_to='static/')),
                ('receivedate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]