# Generated by Django 4.2.3 on 2023-07-25 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("content", models.TextField()),
            ],
        ),
    ]
