# Generated by Django 4.0.6 on 2022-07-24 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_profile_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='type',
            field=models.CharField(max_length=10),
        ),
    ]
