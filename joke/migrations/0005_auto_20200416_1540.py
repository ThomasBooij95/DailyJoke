# Generated by Django 3.0.5 on 2020-04-16 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joke', '0004_auto_20200416_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='joke_id',
            new_name='joke',
        ),
    ]
