from django.db import models

# Create your models here.

from django.contrib.auth.models import User
# Create your models here.
class Record(models.Model):
    # 自增主键, 这里不能设置default属性，负责执行save的时候就不会新增而是修改元素
    Id = models.AutoField(primary_key=True)

    text=models.TextField()

    # 创建时间 auto_now_add：只有在新增的时候才会生效
    createTime = models.DateTimeField(auto_now_add=True)
    # 修改时间 auto_now： 添加和修改都会改变时间
    modifyTime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.Id)+" "+self.text