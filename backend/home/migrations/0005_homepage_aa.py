# Generated by Django 2.2.10 on 2020-02-19 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_tes"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="aa",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
