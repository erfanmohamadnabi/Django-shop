# Generated by Django 5.0.2 on 2024-10-18 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0006_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.CharField(default='27 مهر', max_length=100, verbose_name='تاریخ'),
        ),
    ]
