# Generated by Django 2.0.7 on 2020-04-22 19:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('joke', '0006_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
