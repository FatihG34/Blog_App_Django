# Generated by Django 4.1 on 2022-09-09 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0010_alter_like_post_like"),
    ]

    operations = [
        migrations.AlterField(
            model_name="like",
            name="post_like",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="blog.post"
            ),
        ),
    ]