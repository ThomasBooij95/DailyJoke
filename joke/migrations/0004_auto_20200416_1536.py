# Generated by Django 3.0.5 on 2020-04-16 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joke', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='joke_id',
        ),
    ]
