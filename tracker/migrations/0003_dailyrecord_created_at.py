# Generated by Django 3.2.9 on 2021-12-02 21:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20211201_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyrecord',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
