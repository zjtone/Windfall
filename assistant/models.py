import enum
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.IntegerField(default=1)
    org_id = models.BigIntegerField()
    create_time = models.DateTimeField(auto_now=True)
    modify_time = models.DateTimeField(auto_now=True)
    delete_time = models.DateTimeField(default=None, null=True)

    class Meta:
        abstract = True


class People(BaseModel):
    img = models.CharField(max_length=1000, null=True)
    username = models.CharField(max_length=100)
    id_card = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    openid = models.CharField(max_length=200)
    leader_id = models.BigIntegerField(default=-1)

    class Meta:
        abstract = True


class Org(BaseModel):
    img = models.CharField(max_length=1000, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Employee(People):
    pass


class Teacher(People):
    pass


class User(People):
    pass


class Tag(BaseModel):
    name = models.CharField(max_length=100)


class Time(BaseModel):
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)


class Course(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True)
    img = models.CharField(max_length=1000)
    price = models.IntegerField()  # 以分为单位，不使用小数，防止浮点数误差。
    capacity = models.IntegerField()
    tags = models.ManyToManyField(Tag, through='CourseTagRef', null=True)
    teachers = models.ManyToManyField(Teacher, through='CourseTeacherRef', null=True)
    times = models.ManyToManyField(Time, through='CourseTimeRef', null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)


class CourseTagRef(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)


class CourseTeacherRef(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)


class CourseTimeRef(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    time = models.ForeignKey(Time, on_delete=models.CASCADE, null=True)


class ShoppingCart(BaseModel):
    class Type(enum.Enum):
        INVALID = -1
        COURSE = 0
    user_id = models.BigIntegerField(null=False)
    good_id = models.BigIntegerField(null=False)
    type = models.IntegerField(default=-1)
