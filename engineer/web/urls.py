from django.urls import include, path
from web import views
app_name = 'web'
urlpatterns = [

    path('', views.index,name='index'),
    path('login', views.userlogin, name='login'),
    path('editpass', views.edit_password, name='editpass'),
    path('logout', views.userlogout, name='logout'),
    path('accounts/login/', views.userlogin, name='login2'),

]