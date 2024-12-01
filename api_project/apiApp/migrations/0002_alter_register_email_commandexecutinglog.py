# Generated by Django 4.2.9 on 2024-11-27 07:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("apiApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="register",
            name="email",
            field=models.CharField(max_length=254, unique=True),
        ),
        migrations.CreateModel(
            name="CommandExecutingLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hostname", models.CharField(max_length=254)),
                ("username", models.CharField(max_length=254)),
                ("password", models.CharField(max_length=254)),
                ("command", models.TextField()),
                ("output", models.TextField(blank=True, null=True)),
                ("error", models.TextField(blank=True, null=True)),
                (
                    "executed_at",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apiApp.register",
                    ),
                ),
            ],
        ),
    ]
