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
    ## Course
    path('course/', course.CourseApi.as_view(), name="course"),
    path('tag/', course.TagApi.as_view(), name="tag"),
    path('tag/list/', course.TagList.as_view(), name='tag list'),
    path('course/tag/', course.CourseTagApi.as_view(), name='course tag'),
    path('course/list/', course.CourseList.as_view(), name='course list'),
    ## People
    path('employee/', employee.EmployeeApi.as_view(), name="employee"),
    path('teacher/', teacher.TeacherApi.as_view(), name="teacher"),
    path('user/', user.UserApi.as_view(), name='user'),
    ## Organization
    path('org/', org.OrgApi.as_view(), name='org'),
    ## Shopping
    path('shopping/', shopping.ShoppingCartApi.as_view(), name='shopping'),
    ## File
    path('file/', files.FileApi.as_view(), name='file')
]
