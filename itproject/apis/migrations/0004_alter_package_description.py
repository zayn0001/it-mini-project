# Generated by Django 4.2.3 on 2023-07-25 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apis", "0003_review_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="package",
            name="description",
            field=models.TextField(max_length=400),
        ),
    ]
