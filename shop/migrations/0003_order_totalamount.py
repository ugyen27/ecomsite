# Generated by Django 4.0.1 on 2022-02-01 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='totalamount',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
    ]