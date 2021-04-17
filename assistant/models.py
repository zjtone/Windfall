import enum
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.CharField(max_length=1000, null=True)
    status = models.IntegerField(default=1)
    org_id = models.BigIntegerField()
    create_time = models.DateTimeField(auto_now=True)
    modify_time = models.DateTimeField(auto_now=True)
    delete_time = models.DateTimeField(default=None, null=True)

    class Meta:
        abstract = True


class People(BaseModel):
    username = models.CharField(max_length=100)
    id_card = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    openid = models.CharField(max_length=200, default="")
    leader_id = models.BigIntegerField(default=-1)
    gender = models.CharField(max_length=10, default="")

    class Meta:
        abstract = True


class AuthUserRef(BaseModel):
    class Type(enum.Enum):
        INVALID = -1
        USER = 0  # 用户
        TEACHER = 1  # 教师
        EMPLOYEE = 2  # 员工
        ORG = 3  # 机构

    auth_id = models.BigIntegerField()
    auth_user_id = models.BigIntegerField(default=-1)
    type = models.IntegerField(default=-1)
    org_id = models.BigIntegerField()


class Org(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)


class Employee(People):
    description = models.CharField(max_length=1000, default="……")


class Teacher(People):
    description = models.CharField(max_length=1000, default="……")


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
    price = models.IntegerField()  # 以分为单位，不使用小数，防止浮点数误差。
    used = models.IntegerField(default=0)  # 已经卖出的数量
    capacity = models.IntegerField()
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)


class CourseTagRef(BaseModel):
    course_id = models.BigIntegerField(default=-1)
    tag_id = models.BigIntegerField(default=-1)


class CourseTeacherRef(BaseModel):
    course_id = models.BigIntegerField(default=-1)
    teacher_id = models.BigIntegerField(default=-1)


class CourseTimeRef(BaseModel):
    course_id = models.BigIntegerField(default=-1)
    time_id = models.BigIntegerField(default=-1)


class CourseUserRef(BaseModel):
    course_id = models.BigIntegerField(default=-1)
    user_id = models.BigIntegerField(default=-1)


class ShoppingCart(BaseModel):
    class Type(enum.Enum):
        INVALID = -1
        COURSE = 0
    user_id = models.BigIntegerField(null=False)
    good_id = models.BigIntegerField(null=False)
    type = models.IntegerField(default=-1)


class Order(BaseModel):
    user_id = models.BigIntegerField(null=False)
    pay_time = models.DateTimeField(null=True, default=None)  # 是否已支付，为空则未支付，否则表示已支付


class OrderRef(BaseModel):
    class Type(enum.Enum):
        INVALID = -1
        COURSE = 0
    order_id = models.BigIntegerField(null=False)
    good_id = models.BigIntegerField(null=False)
    type = models.IntegerField(default=-1)
