# Generated by Django 2.0 on 2020-02-28 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20191223_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='link_to',
            field=models.CharField(max_length=300),
        ),
    ]