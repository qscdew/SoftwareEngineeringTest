from django.urls import include, path
from engineeradmin import views
app_name = 'engineeradmin'
urlpatterns = [

    path('', views.all_user,name='index'),
path('newuser', views.new_user,name='new_user'),
path('edituser', views.edit_user,name='edit_user'),
path('deleteuser/<int:userid>', views.delete_user,name='delete_user'),
path('alluser', views.all_user,name='all_user'),
path('edituser/<int:userid>', views.edit_user,name='edit_user'),
path('allrecord', views.all_record,name='all_record'),
]