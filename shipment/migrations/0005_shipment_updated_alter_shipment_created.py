# Generated by Django 4.2.1 on 2023-05-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0004_alter_shipment_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
