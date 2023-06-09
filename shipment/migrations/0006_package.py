# Generated by Django 4.2.1 on 2023-05-23 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0005_shipment_updated_alter_shipment_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=250)),
                ('sender_nationality', models.CharField(blank=True, max_length=100, null=True)),
                ('sender_location', models.CharField(blank=True, max_length=100, null=True)),
                ('receiver_name', models.CharField(blank=True, max_length=250, null=True)),
                ('receiver_address', models.CharField(blank=True, max_length=300, null=True)),
                ('receiver_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('receiver_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('tracking_number', models.CharField(blank=True, max_length=80, null=True)),
                ('weight', models.CharField(blank=True, max_length=10, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('shipment_location', models.CharField(blank=True, max_length=100, null=True)),
                ('comment', models.TextField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
