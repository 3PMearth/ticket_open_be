# Generated by Django 4.2.3 on 2023-07-18 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tokens", "0004_alter_asset_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="token",
            name="nft_id",
            field=models.IntegerField(blank=True, null=True, verbose_name="NFT ID"),
        ),
    ]
