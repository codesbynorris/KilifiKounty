# Generated by Django 4.2.7 on 2023-11-21 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Karibu_Kilifi', '0003_accommodation_email_address_accommodation_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carhire',
            name='description',
            field=models.TextField(blank=True, max_length=50, verbose_name='Car Description'),
        ),
    ]
