# Generated by Django 5.0.2 on 2024-02-29 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0015_products_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='invoice_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='item_name',
            field=models.CharField(max_length=100),
        ),
    ]
