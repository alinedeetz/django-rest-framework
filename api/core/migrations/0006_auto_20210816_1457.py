# Generated by Django 3.2.5 on 2021-08-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210812_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproduct',
            name='cost',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]