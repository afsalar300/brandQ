# Generated by Django 3.2.10 on 2023-11-14 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categorydb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ca_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ca_description', models.CharField(blank=True, max_length=100, null=True)),
                ('ca_image', models.ImageField(blank=True, null=True, upload_to='category')),
            ],
        ),
    ]