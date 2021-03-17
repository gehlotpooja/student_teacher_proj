from . import views
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken import views as auth_views
app_name='student_teacher_app'

urlpatterns = [
    # path(r'', views.index, name='index'),
    path(r'', include('rest_auth.urls')),
    path(r'registration/', include('rest_auth.registration.urls')),
    path(r'create_user/', views.create_user_api , name='create_user'),
    path(r'update_user/', views.update_user_api , name='update_user'),
    path(r'get_user_details_with_id/', views.get_user_details_with_id_api , name='get_user_details_with_id'),
    path(r'get_all_user_details/', views.get_all_user_details_api , name='get_all_user_details'),
    path(r'verify/', views.verify, name='verify'),
    ]