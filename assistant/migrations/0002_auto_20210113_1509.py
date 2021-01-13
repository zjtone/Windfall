# Generated by Django 3.1 on 2021-01-13 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursetagref',
            name='course_id',
        ),
        migrations.RemoveField(
            model_name='coursetagref',
            name='tag_id',
        ),
        migrations.RemoveField(
            model_name='courseteacherref',
            name='course_id',
        ),
        migrations.RemoveField(
            model_name='courseteacherref',
            name='teacher_id',
        ),
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(through='assistant.CourseTagRef', to='assistant.Tag'),
        ),
        migrations.AddField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(through='assistant.CourseTeacherRef', to='assistant.Teacher'),
        ),
        migrations.AddField(
            model_name='coursetagref',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assistant.course'),
        ),
        migrations.AddField(
            model_name='coursetagref',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assistant.tag'),
        ),
        migrations.AddField(
            model_name='courseteacherref',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assistant.course'),
        ),
        migrations.AddField(
            model_name='courseteacherref',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assistant.teacher'),
        ),
    ]
