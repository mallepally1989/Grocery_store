# Generated by Django 3.0.4 on 2020-04-06 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0007_auto_20200405_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='totalCount',
            field=models.IntegerField(default=0),
        ),
    ]
