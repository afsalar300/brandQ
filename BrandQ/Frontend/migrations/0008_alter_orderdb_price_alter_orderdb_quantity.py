# Generated by Django 4.2.11 on 2024-05-16 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0007_remove_orderdb_price_remove_orderdb_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdb',
            name='Price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orderdb',
            name='Quantity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]