# Generated by Django 2.1.7 on 2019-04-20 21:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('automatedbankteller', '0005_deposit'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='deposit_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
