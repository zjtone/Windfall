# Generated by Django 3.1 on 2021-04-04 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0015_auto_20210401_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='description',
            field=models.CharField(default='……', max_length=1000),
        ),
        migrations.AddField(
            model_name='teacher',
            name='description',
            field=models.CharField(default='……', max_length=1000),
        ),
    ]