# Generated by Django 3.0.4 on 2020-04-16 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0011_auto_20200404_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Fruits', 'Fruits'), ('Foods', 'Foods'), ('Drinks', 'Drinks'), ('Others', 'Others')], default='Others', max_length=120),
        ),
    ]
