# Generated by Django 4.2.9 on 2024-11-28 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apiApp", "0003_remove_commandexecutinglog_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commandexecutinglog",
            name="executed_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
