from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Engineer(models.Model):
    # 自增主键, 这里不能设置default属性，负责执行save的时候就不会新增而是修改元素
    Id = models.AutoField(primary_key=True)
    Name = models.CharField('姓名', max_length=20, default="待补充")
    Sex = models.IntegerField('性别', default=0)
    Birthday = models.CharField('生日', max_length=20, default="待补充")
    Degree = models.IntegerField('学历', default=0)
    NativePlace = models.CharField('籍贯', max_length=10, default="待补充")
    Address = models.CharField('地址', max_length=30, default="待补充")
    Tel = models.CharField('电话', max_length=15, default="待补充")

    WorkYears = models.IntegerField('工龄', default=0)
    Salary=models.DecimalField( max_digits=12, decimal_places=2,default=0)

    User = models.OneToOneField(User, on_delete=models.CASCADE)

    # 创建时间 auto_now_add：只有在新增的时候才会生效
    createTime = models.DateTimeField(auto_now_add=True)
    # 修改时间 auto_now： 添加和修改都会改变时间
    modifyTime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.Id)+" "+self.Name
