# Generated by Django 3.0.3 on 2020-04-29 10:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_useraddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='state',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
    ]
