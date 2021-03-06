# Generated by Django 3.1 on 2021-01-24 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0004_auto_20210116_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(default=1)),
                ('org_id', models.BigIntegerField()),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('delete_time', models.DateTimeField(default=None, null=True)),
                ('course_id', models.BigIntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
