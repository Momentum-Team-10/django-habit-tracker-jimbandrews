# Generated by Django 3.2.9 on 2021-12-04 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20211204_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyrecord',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]