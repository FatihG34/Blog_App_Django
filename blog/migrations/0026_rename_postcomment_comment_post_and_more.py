# Generated by Django 4.1 on 2022-09-14 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0025_alter_category_options_alter_post_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="postcomment",
            new_name="post",
        ),
        migrations.RenameField(
            model_name="comment",
            old_name="post_user",
            new_name="user",
        ),
    ]