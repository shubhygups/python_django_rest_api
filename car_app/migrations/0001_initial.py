# Generated by Django 3.2.4 on 2021-06-29 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('brand_name', models.CharField(max_length=100)),
                ('top_speed', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=10)),
                ('car_type', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
            ],
            options={
                'unique_together': {('car_name', 'brand_name')},
            },
        ),
    ]
