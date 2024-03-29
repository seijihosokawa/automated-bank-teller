# Generated by Django 2.1.7 on 2019-04-22 20:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('automatedbankteller', '0007_auto_20190420_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(choices=[('SA', 'Savings'), ('CA', 'Checking')], max_length=2)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20, validators=[django.core.validators.MinValueValidator('10.00')])),
                ('deposit_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
