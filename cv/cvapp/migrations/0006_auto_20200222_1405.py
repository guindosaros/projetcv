# Generated by Django 2.2.8 on 2020-02-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvapp', '0005_auto_20200220_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
