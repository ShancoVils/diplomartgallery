# Generated by Django 3.2 on 2021-05-28 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artgallery', '0005_customuser_bill_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bill_number',
            field=models.IntegerField(blank=True, max_length=16),
        ),
    ]
