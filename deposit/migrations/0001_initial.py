# Generated by Django 4.1.6 on 2023-02-12 13:29

import deposit.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Deposit",
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
                ("amount", models.FloatField()),
                ("note", models.CharField(max_length=1000)),
                (
                    "reference",
                    models.CharField(
                        default=deposit.models._generate_reference, max_length=255
                    ),
                ),
                ("depositor", models.CharField(max_length=255)),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
