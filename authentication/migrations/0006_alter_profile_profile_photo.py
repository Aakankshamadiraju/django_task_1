# Generated by Django 4.0.6 on 2022-07-25 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_profile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
