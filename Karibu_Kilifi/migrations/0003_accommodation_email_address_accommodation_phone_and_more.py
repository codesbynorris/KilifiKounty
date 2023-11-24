# Generated by Django 4.2.7 on 2023-11-21 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Karibu_Kilifi', '0002_carhire_image_carhire_plate'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodation',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email Address'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='phone',
            field=models.CharField(blank=True, max_length=15, verbose_name='Contact Phone'),
        ),
        migrations.AlterField(
            model_name='carhire',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Car Image'),
        ),
    ]