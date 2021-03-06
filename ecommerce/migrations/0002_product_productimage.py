# Generated by Django 3.0.4 on 2020-03-31 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('salePrice', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('slug', models.SlugField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'unique_together': {('title', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('featured', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('thumbnail', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Product')),
            ],
        ),
    ]
