# Generated by Django 2.2.7 on 2021-02-11 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='password',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='phone',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
