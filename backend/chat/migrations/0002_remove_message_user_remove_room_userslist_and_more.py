# Generated by Django 5.2 on 2025-04-29 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.RemoveField(
            model_name='room',
            name='userslist',
        ),
        migrations.AddField(
            model_name='message',
            name='username',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterModelTable(
            name='message',
            table=None,
        ),
    ]
