# Generated by Django 4.2.3 on 2023-07-22 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contracts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contract",
            name="active",
            field=models.BooleanField(default=True, verbose_name="활성화 여부"),
        ),
    ]
