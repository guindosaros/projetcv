# Generated by Django 2.2.8 on 2020-02-03 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='annee',
        ),
        migrations.AlterField(
            model_name='competence',
            name='titre',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='detailcompetence',
            name='nom',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='education',
            name='diplôme',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='experience',
            name='annee',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='experience',
            name='nom',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='message',
            name='nom',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='message',
            name='sujet',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='adresse',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='numero',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='service',
            name='nom',
            field=models.CharField(max_length=250),
        ),
    ]
