# SoftwareEngineeringTest

####环境
+Ubuntu 5.4.0-6ubuntu1~16.04.10
+MySQL5.7
+Python 3.5.2【Django (2.2.6) pip (8.1.1) PyMySQL (0.9.3)】

1、配置数据库
打开 engineer/settings.py，修改80行数据库信息。

2、切换到manage.py所在目录
`python manage.py makemigrations`
`python manage.py migrate`
`python manage.py createsuperuser`

3、运行
`python manage.py runserver 0:8088`
访问 http://localhost:8088


