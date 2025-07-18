# Generated by Django 5.2.3 on 2025-06-24 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='members',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='firstname',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='members',
            name='lastname',
            field=models.CharField(max_length=255),
        ),
    ]
