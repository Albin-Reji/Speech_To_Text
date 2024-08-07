# Generated by Django 5.0.6 on 2024-07-24 13:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_authentication", "0005_alter_signup_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userdata",
            name="activity",
            field=models.FileField(
                upload_to="",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        ["pdf", "doc", "docx", "txt"]
                    )
                ],
            ),
        ),
    ]
