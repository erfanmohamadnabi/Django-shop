# Generated by Django 5.0.2 on 2024-10-16 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0005_alter_weblog_comments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblog_comments',
            name='date',
            field=models.CharField(default='1403/07/26', max_length=100, verbose_name='تاریخ'),
        ),
    ]
