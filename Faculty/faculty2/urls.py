from allauth.account.views import LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('', FacultyViewSet.as_view({'get': 'list', 'post': 'create'}), name='faculty_list'),
    path('<int:pk>/', FacultyViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='faculty_detail'),


    path('prov/', ProvViewSet.as_view({'get': 'list', 'post': 'create'}), name='prov_list'),
    path('prov/<int:pk>/', ProvViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='prov_detail'),


    path('stu/', StuViewSet.as_view({'get': 'list', 'post': 'create'}), name='stu_list'),
    path('stu/<int:pk>/', StuViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='stu_detail'),


    path('well/', WellViewSet.as_view({'get': 'list', 'post': 'create'}), name='well_list'),
    path('well/<int:pk>/', WellViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='well_detail'),


    path('cabinet/', CabinetViewSet.as_view({'get': 'list', 'post': 'create'}), name='cabinet_list'),
    path('cabinet/<int:pk>/', CabinetViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='cabinet_detail'),


    path('schedule/', ScheduleViewSet.as_view({'get': 'list', 'post': 'create'}), name='schedule_list'),
    path('schedule/<int:pk>/', ScheduleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='schedule_detail'),
]
