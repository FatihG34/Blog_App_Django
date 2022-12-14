# Generated by Django 4.1 on 2022-09-10 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0022_rename_user_post_author_remove_comment_post_user_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="author",
            new_name="user",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="post_user",
        ),
        migrations.AddField(
            model_name="comment",
            name="post_user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
