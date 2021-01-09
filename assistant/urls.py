from django.urls import path
from . import views
from assistant.api.v1 import course, employee, teacher, user, org

urlpatterns = [
    path('index/', views.index, name='index'),
    path('course/', course.index, name="course"),
    path('employee/', employee.index, name="employee"),
    path('teacher/', teacher.index, name="teacher"),
    path('organization/', org.index, name='org'),
    path('user/', user.UserApi.as_view(), name='user')
]
