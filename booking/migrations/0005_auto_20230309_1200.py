# Generated by Django 3.2.18 on 2023-03-09 12:00

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_booking_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='booking',
            name='special_requirements',
            field=models.TextField(blank=True, default=123),
            preserve_default=False,
        ),
    ]