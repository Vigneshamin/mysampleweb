# Generated by Django 3.2.9 on 2021-11-14 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Romantic', 'Romantic'), ('Horror', 'Horror'), ('Comedy', 'Comedy'), ('Comic', 'Comic'), ('Education', 'Education'), ('Mystery', 'Mystery'), ('Fantasy', 'Fantasy'), ('Historical Fiction', 'Historical Fiction'), ('Science Fiction', 'Science Fiction'), ('Autobiography', 'Autobiography'), ('Cook Book', 'Cook Book'), ('Others', 'Others')], max_length=200, null=True),
        ),
    ]
