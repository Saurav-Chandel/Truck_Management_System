# Generated by Django 4.0.5 on 2022-06-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_income_per_route_deisel_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income_per_route',
            old_name='earning',
            new_name='extra_expenses',
        ),
        migrations.AddField(
            model_name='income_per_route',
            name='payment_per_route',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='income_per_route',
            name='total_earning_per_route',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
