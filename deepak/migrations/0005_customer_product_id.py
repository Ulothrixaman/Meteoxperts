# Generated by Django 5.0.1 on 2024-02-04 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepak', '0004_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='product_id',
            field=models.CharField(max_length=10, null=True),
        ),
    ]