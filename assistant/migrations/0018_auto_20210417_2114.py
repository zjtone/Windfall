# Generated by Django 3.1 on 2021-04-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0017_authuserref_auth_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='teacher',
            name='gender',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default='', max_length=10),
        ),
    ]
