# Generated by Django 5.1.1 on 2024-09-11 16:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0002_forumpost_forumcomment"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="message",
            name="modified",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
