# Generated by Django 5.0.7 on 2024-07-27 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="summary",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.CharField(max_length=255),
        ),
    ]
