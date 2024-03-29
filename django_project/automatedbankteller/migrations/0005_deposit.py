# Generated by Django 2.1.7 on 2019-04-20 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('automatedbankteller', '0004_auto_20190415_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(choices=[('SA', 'Savings'), ('CA', 'Checking')], max_length=2)),
                ('accountID', models.IntegerField()),
                ('deposit_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('account_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
