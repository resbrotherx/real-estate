# Generated by Django 4.2.2 on 2023-06-21 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='value',
            name='description',
        ),
        migrations.AddField(
            model_name='value',
            name='icon',
            field=models.CharField(default='flaticon-door', max_length=100),
            preserve_default=False,
        ),
    ]
