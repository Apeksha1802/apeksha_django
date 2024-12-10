# Generated by Django 5.1.3 on 2024-12-10 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superstar', '0003_rename_n_country_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('population', models.IntegerField()),
                ('capital', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'states',
            },
        ),
    ]