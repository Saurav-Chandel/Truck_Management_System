# Generated by Django 4.0.5 on 2022-06-08 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(blank=True, choices=[('single_excel', 'single_Excel'), ('multi_excel', 'multi_excel')], max_length=100, null=True)),
                ('vehicle_number', models.CharField(blank=True, max_length=100, null=True)),
                ('insurance_start_date', models.DateTimeField()),
                ('insurance_close_date', models.DateTimeField()),
                ('goods_tax', models.BooleanField(default=False)),
                ('permit_tax', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]