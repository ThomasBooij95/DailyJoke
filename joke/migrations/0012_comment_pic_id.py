# Generated by Django 2.1.5 on 2020-04-24 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joke', '0011_auto_20200423_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pic_id',
            field=models.TextField(default='2'),
            preserve_default=False,
        ),
    ]
