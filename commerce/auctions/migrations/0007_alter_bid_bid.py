# Generated by Django 4.2 on 2023-04-14 15:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0006_alter_bid_bid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bid",
            name="bid",
            field=models.IntegerField(),
        ),
    ]
