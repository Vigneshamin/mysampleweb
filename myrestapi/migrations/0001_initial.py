# Generated by Django 3.2.9 on 2021-11-18 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productitems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='products')),
            ],
        ),
    ]
