# Generated by Django 4.1 on 2022-09-10 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0023_rename_author_post_user_remove_comment_post_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="postcomment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="blog.post",
            ),
        ),
    ]