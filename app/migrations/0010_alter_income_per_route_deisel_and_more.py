# Generated by Django 4.0.5 on 2022-06-09 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_income_per_route_deisel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income_per_route',
            name='deisel',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='income_per_route',
            name='extra_expenses',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='income_per_route',
            name='total_expense',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
