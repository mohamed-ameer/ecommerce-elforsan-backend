# Generated by Django 3.2 on 2023-02-14 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_product_category_ar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category_ar',
        ),
    ]
