# Generated by Django 3.1.3 on 2020-11-12 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='lot_last_bet_price',
            field=models.IntegerField(blank=True, max_length=1000, null=True),
        ),
    ]
