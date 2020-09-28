# Generated by Django 3.1.1 on 2020-09-25 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0002_auto_20200924_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='completed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date created'),
        ),
    ]
