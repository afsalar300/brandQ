# Generated by Django 4.2.11 on 2024-05-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0003_alter_orderdb_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdb',
            name='Product',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
