# Generated by Django 2.2.4 on 2019-08-11 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_card_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='starterdeck',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
