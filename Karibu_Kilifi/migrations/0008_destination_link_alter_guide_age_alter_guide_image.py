# Generated by Django 4.2.7 on 2023-11-23 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Karibu_Kilifi', '0007_guide'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='link',
            field=models.URLField(blank=True, verbose_name='Google Maps Link'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='age',
            field=models.IntegerField(verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Photo'),
        ),
    ]