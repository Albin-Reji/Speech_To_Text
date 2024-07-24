# Generated by Django 5.0.6 on 2024-07-24 13:06

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_authentication", "0003_contactus"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserData",
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
                (
                    "activity",
                    models.FileField(
                        upload_to="activities/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["pdf", "doc", "docx", "txt"]
                            )
                        ],
                    ),
                ),
                (
                    "email",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_authentication.signup",
                    ),
                ),
            ],
        ),
    ]
