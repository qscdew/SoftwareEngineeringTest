from django.urls import include, path
from engineeruser import views
app_name = 'engineeruser'
urlpatterns = [

    path('', views.index,name='index'),
    path('edit', views.edit_detail,name='edit'),
    path('search', views.search,name='search'),
    path('all', views.all_engineer,name='all'),
    path('calc', views.calc_salary,name='calc'),
    path('sort', views.sort, name='sort'),
    path('sort/id', views.sort_id, name='sort_id'),
path('sort/name', views.sort_name, name='sort_name'),
path('sort/workyears', views.sort_workyears, name='sort_workyears'),

    path('sort/id/reverse', views.sort_id_reverse, name='sort_id_reverse'),
path('sort/name/reverse', views.sort_name_reverse, name='sort_name_reverse'),
path('sort/workyears/reverse', views.sort_workyears_reverse, name='sort_workyears_reverse'),


]