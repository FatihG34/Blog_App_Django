# Generated by Django 4.1 on 2022-09-14 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_pic",
            field=models.ImageField(
                blank=True,
                default="Avatar.png",
                upload_to="profile_pics",
                verbose_name="Profile Picture",
            ),
        ),
    ]
