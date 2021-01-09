from django.db import models


# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BigIntegerField(default=1)
    org_id = models.BigIntegerField()
    create_time = models.DateTimeField(auto_now=True)
    modify_time = models.DateTimeField(auto_now=True)
    delete_time = models.DateTimeField(default=None, null=True)

    class Meta:
        abstract = True


class People(BaseModel):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    id_card = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    openid = models.CharField(max_length=200)
    leader_id = models.BigIntegerField(default=-1)

    class Meta:
        abstract = True


class Org(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Emploee(People):
    pass


class Teacher(People):
    pass


class User(People):
    pass


class Course(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    img = models.CharField(max_length=1000)
    price = models.IntegerField()  # 以分为单位，不使用小数，防止浮点数误差。
    capacity = models.IntegerField()


class Tag(BaseModel):
    name = models.CharField(max_length=100)


class CourseTagRef(BaseModel):
    course_id = models.BigIntegerField()
    tag_id = models.BigIntegerField()


class CourseTeacherRef(BaseModel):
    course_id = models.BigIntegerField()
    teacher_id = models.BigIntegerField()
