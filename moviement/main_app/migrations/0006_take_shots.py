# Generated by Django 4.2.5 on 2023-10-06 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_shot'),
    ]

    operations = [
        migrations.AddField(
            model_name='take',
            name='shots',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
