# Generated by Django 4.2.7 on 2023-11-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Karibu_Kilifi', '0015_alter_guide_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
