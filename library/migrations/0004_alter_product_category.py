# Generated by Django 3.2.9 on 2021-11-14 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Romantic', 'Romantic'), ('Horror', 'Horror'), ('Comedy', 'Comedy'), ('Comic', 'Comic'), ('Mystery', 'Mystery'), ('Fantasy', 'Fantasy'), ('Historical Fiction', 'Historical Fiction'), ('Science Fiction', 'Science Fiction'), ('Autobiography', 'Autobiography'), ('Cook Book', 'Cook Book'), ('Others', 'Others')], max_length=200, null=True),
        ),
    ]
