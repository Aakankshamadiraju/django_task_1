# Generated by Django 4.0.6 on 2022-07-24 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pincode',
            field=models.CharField(blank=True, max_length=7),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
