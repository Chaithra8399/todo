# Generated by Django 4.1.4 on 2023-01-10 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-10-12'),
            preserve_default=False,
        ),
    ]
