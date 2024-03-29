# Generated by Django 2.1.7 on 2020-07-30 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200730_0957'),
        ('check', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checking',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='checking',
            name='bar_code',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='checking',
            name='serial_number',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
