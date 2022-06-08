# Generated by Django 4.0.5 on 2022-06-08 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_route_back_load_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='route',
            old_name='expense',
            new_name='deisel_expense',
        ),
        migrations.AddField(
            model_name='route',
            name='driver_expense',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
