# Generated by Django 4.1 on 2022-09-10 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0013_remove_category_post_post_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="category",
        ),
        migrations.AddField(
            model_name="category",
            name="post",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="blog.post"
            ),
            preserve_default=False,
        ),
    ]