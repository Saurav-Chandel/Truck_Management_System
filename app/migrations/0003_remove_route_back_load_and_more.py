# Generated by Django 4.0.5 on 2022-06-08 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_back_load_material_route_add_vehicle_carriage_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='back_load',
        ),
        migrations.RemoveField(
            model_name='route',
            name='back_load_material',
        ),
        migrations.AddField(
            model_name='income_per_route',
            name='deisel',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
