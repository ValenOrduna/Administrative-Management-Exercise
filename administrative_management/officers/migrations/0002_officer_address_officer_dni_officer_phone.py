# Generated by Django 4.2 on 2023-04-04 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='officer',
            name='address',
            field=models.CharField(default=False, max_length=50),
        ),
        migrations.AddField(
            model_name='officer',
            name='dni',
            field=models.CharField(default=False, max_length=30),
        ),
        migrations.AddField(
            model_name='officer',
            name='phone',
            field=models.CharField(default=False, max_length=50),
        ),
    ]
