# Generated by Django 2.2.4 on 2019-08-23 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sign',
            name='description',
            field=models.TextField(default='0000'),
        ),
    ]
