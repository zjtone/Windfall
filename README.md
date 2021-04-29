# 用户账号模型
django的User类在我们这里被认定为AuthUser类，用户、教师、员工、机构分别被定义为User、Teacher、Employee、Org类。
注意AuthUser仅仅与登录、注册用户等接口相关，也仅仅与用户、教师、员工、机构相关，而具体的课程、购物车等则与具体的类相关。

# 数据库管理
python manage.py makemigrations

python manage.py migrate assistant --fake

python manage.py migrate

python manage.py migrate --run-syncdb