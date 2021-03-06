# Generated by Django 3.1 on 2021-02-13 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0011_auto_20210209_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='course',
            name='teachers',
        ),
        migrations.RemoveField(
            model_name='course',
            name='times',
        ),
        migrations.RemoveField(
            model_name='coursetagref',
            name='course',
        ),
        migrations.RemoveField(
            model_name='coursetagref',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='courseteacherref',
            name='course',
        ),
        migrations.RemoveField(
            model_name='courseteacherref',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='coursetimeref',
            name='course',
        ),
        migrations.RemoveField(
            model_name='coursetimeref',
            name='time',
        ),
        migrations.AddField(
            model_name='coursetagref',
            name='course_id',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='coursetagref',
            name='tag_id',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='courseteacherref',
            name='course_id',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='courseteacherref',
            name='teacher_id',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='coursetimeref',
            name='course_id',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='coursetimeref',
            name='time_id',
            field=models.BigIntegerField(default=-1),
        ),
    ]
