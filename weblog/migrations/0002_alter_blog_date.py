# Generated by Django 5.0.2 on 2024-10-08 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.CharField(default='17 مهر', max_length=100, verbose_name='تاریخ'),
        ),
    ]
