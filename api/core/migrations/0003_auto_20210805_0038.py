# Generated by Django 3.2.5 on 2021-08-05 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_historicalclient'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(default='default@default.com', max_length=254),
        ),
        migrations.AddField(
            model_name='historicalclient',
            name='email',
            field=models.EmailField(default='default@default.com', max_length=254),
        ),
    ]
