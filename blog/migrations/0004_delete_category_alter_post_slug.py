# Generated by Django 4.1 on 2022-09-08 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_post_slug"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Category",
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
