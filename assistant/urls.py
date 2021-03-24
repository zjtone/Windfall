from django.urls import path
from . import views
from assistant.api.serializers import MyTokenObtainPairView
from assistant.api.v1 import course, employee, teacher, user, org, login, shopping, files
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # jwt
    path('token/', MyTokenObtainPairView.as_view(), name='obtain_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('auth/user/', login.AuthUserApi.as_view(), name='auth_user'),
    # functions
    path('index/', views.index, name='index'),
    # Course
    path('course/', course.CourseApi.as_view(), name="course"),
    path('tag/', course.TagApi.as_view(), name="tag"),
    path('tag/list/', course.TagList.as_view(), name='tag list'),
    path('course/tag/', course.CourseTagApi.as_view(), name='course tag'),
    path('course/teacher/', course.CourseTeacherApi.as_view(), name='course teacher'),
    path('course/list/', course.CourseList.as_view(), name='course list'),
    path('course/time/', course.CourseTimeRefApi.as_view(), name='course time'),
    path('time/', course.TimeApi.as_view(), name='time'),
    # People
    path('employee/', employee.EmployeeApi.as_view(), name="employee"),
    path('employee/list/', employee.EmployeeList.as_view(), name='employee list'),
    path('teacher/', teacher.TeacherApi.as_view(), name="teacher"),
    path('teacher/list/', teacher.TeacherList.as_view(), name='teacher list'),
    path('user/', user.UserApi.as_view(), name='user'),
    path('user/list/', user.UserList.as_view(), name='user list'),
    # Organization
    path('org/', org.OrgApi.as_view(), name='org'),
    path('org/create/', org.CreateOrg.as_view(), name='create org'),  # 不规范的写法，暂时留一个
    # Shopping
    path('shopping/', shopping.ShoppingCartApi.as_view(), name='shopping'),
    path('shopping/list/', shopping.ShoppingCartList.as_view(), name='shopping'),
    # File
    path('file/', files.FileApi.as_view(), name='file')
]
