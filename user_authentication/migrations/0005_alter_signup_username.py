# Generated by Django 5.0.6 on 2024-07-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_authentication", "0004_userdata"),
    ]

    operations = [
        migrations.AlterField(
            model_name="signup",
            name="username",
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
