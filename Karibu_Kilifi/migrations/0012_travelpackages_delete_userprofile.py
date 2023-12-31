# Generated by Django 4.2.7 on 2023-11-26 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Karibu_Kilifi', '0011_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelPackages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=40, verbose_name='Package Name')),
                ('package_description', models.TextField()),
                ('package_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Price')),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Karibu_Kilifi.accommodation')),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Karibu_Kilifi.attraction')),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
