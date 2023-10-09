# Generated by Django 4.2.5 on 2023-10-09 15:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='take',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]
