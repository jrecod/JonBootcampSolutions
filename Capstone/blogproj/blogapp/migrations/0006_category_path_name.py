# Generated by Django 3.1.1 on 2020-10-22 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_auto_20201022_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='path_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
