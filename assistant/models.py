from django.db import models


# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.PositiveBigIntegerField(default=1)
    org_id = models.PositiveBigIntegerField()


class People(BaseModel):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    id_card = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    openid = models.CharField(max_length=200)
    leader_id = models.PositiveBigIntegerField(default=-1)


class Org(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Emploee(People):
    pass


class Teacher(People):
    pass


class Course(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    img = models.CharField(max_length=1000)


class Tag(BaseModel):
    name = models.CharField(max_length=100)


class CourseTagRef(BaseModel):
    course_id = models.PositiveBigIntegerField()
    tag_id = models.PositiveBigIntegerField()


class CourseTeacherRef(BaseModel):
    course_id = models.PositiveBigIntegerField()
    teacher_id = models.PositiveBigIntegerField()
