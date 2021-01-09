from django.urls import path
from . import views
from assistant.api.v1 import course, employee, teacher, user, org

urlpatterns = [
    path('index/', views.index, name='index'),
    path('course/', course.CourseApi.as_view(), name="course"),
    path('employee/', employee.EmployeeApi.as_view(), name="employee"),
    path('teacher/', teacher.TeacherApi.as_view(), name="teacher"),
    path('org/', org.OrgApi.as_view(), name='org'),
    path('user/', user.UserApi.as_view(), name='user')
]
