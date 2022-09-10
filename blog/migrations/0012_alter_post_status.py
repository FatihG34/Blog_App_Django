# Generated by Django 4.1 on 2022-09-10 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0011_alter_like_post_like"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="status",
            field=models.CharField(
                choices=[("Draft", "Draft"), ("Published", "Published")],
                max_length=50,
                verbose_name="Status",
            ),
        ),
    ]
