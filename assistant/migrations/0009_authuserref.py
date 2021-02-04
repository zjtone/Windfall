# Generated by Django 3.1 on 2021-02-04 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0008_auto_20210204_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUserRef',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(default=1)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('delete_time', models.DateTimeField(default=None, null=True)),
                ('auth_id', models.BigIntegerField()),
                ('type', models.IntegerField(default=-1)),
                ('org_id', models.BigIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
