# Generated by Django 5.0.4 on 2024-04-30 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("author", models.CharField(max_length=50)),
                ("title", models.CharField(max_length=255)),
                ("body", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("author", models.CharField(max_length=50)),
                ("body", models.TextField()),
                ("article", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="article.article")),
            ],
        ),
    ]
