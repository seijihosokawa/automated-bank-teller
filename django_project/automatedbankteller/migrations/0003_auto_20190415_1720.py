# Generated by Django 2.1.7 on 2019-04-15 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automatedbankteller', '0002_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('SA', 'Savings'), ('CA', 'Checking')], max_length=2),
        ),
    ]