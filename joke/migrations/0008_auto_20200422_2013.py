# Generated by Django 2.0.7 on 2020-04-22 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joke', '0007_comment_timestamp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-datetime']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='timeStamp',
            new_name='datetime',
        ),
    ]
