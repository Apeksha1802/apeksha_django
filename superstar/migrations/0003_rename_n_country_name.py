# Generated by Django 5.1.3 on 2024-12-10 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superstar', '0002_country_alter_city_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='n',
            new_name='name',
        ),
    ]
