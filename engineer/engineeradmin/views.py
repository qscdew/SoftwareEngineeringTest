from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponsePermanentRedirect
import json
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from engineeruser.models import Engineer
from engineeradmin.models import Record
@login_required()
def index(request):
    if(request.user.username!="admin"):
        return HttpResponseRedirect(reverse('web:index'))
    context = {}
    # info=Engineer.objects.get(User=request.user)
    # context['info']=info
    return render(request, 'adminindex.html', context)

@login_required()
def new_user(request):
    if(request.user.username!="admin"):
        return HttpResponseRedirect(reverse('web:index'))
    else:
        if (request.method == 'POST'):
            username=request.POST.get('username')
            password=request.POST.get('password')
            Name=request.POST.get('Name')
            Tel=request.POST.get('Tel')

            newuser = User.objects.create_user(username=username, password=password)
            newuser.save()

            newengineer=Engineer.objects.create(Name=Name,Tel=Tel,User=newuser)
            newengineer.save()
            context = {}
            newrecord=Record.objects.create(text=request.user.username+" 创建了新用户："+username)
            newrecord.save()
            # info=Engineer.objects.get(User=request.user)
            context['info']="创建成功"
            return render(request, 'new_user.html', context)
        else:
            context = {}
            # info=Engineer.objects.get(User=request.user)

            return render(request, 'new_user.html', context)


@login_required()
def all_user(request):
    if(request.user.username!="admin"):
        return HttpResponseRedirect(reverse('web:index'))
    else:
        context = {}
        info=Engineer.objects.all()
        context['engineers']=info
        return render(request, 'all_user.html', context)


@login_required()
def edit_user(request,userid):
    if(request.user.username!="admin"):
        return HttpResponseRedirect(reverse('web:index'))
    else:
        if (request.method == 'POST'):
            Id = request.POST.get('Id')
            Name = request.POST.get('Name')
            Sex = request.POST.get('Sex')
            Birthday = request.POST.get('Birthday')
            NativePlace = request.POST.get('NativePlace')
            Address = request.POST.get('Address')
            Degree = request.POST.get('Degree')
            WorkYears = request.POST.get('WorkYears')
            Tel = request.POST.get('Tel')
            Salary = request.POST.get('Salary')
            us=User.objects.get(id=userid)

            obj = Engineer.objects.get(User=us)
            #obj.Id = Id
            obj.Name = Name
            if (Sex == "男"):
                obj.Sex = 1
            elif (Sex == "女"):
                obj.Sex = 0
            obj.Birthday = Birthday
            obj.NativePlace = NativePlace
            obj.Address = Address
            if (Degree == "高中"):
                obj.Degree = 0
            elif (Degree == "学士"):
                obj.Degree = 1
            elif (Degree == "硕士"):
                obj.Degree = 2
            elif (Degree == "博士"):
                obj.Degree = 3
            elif (Degree == "其它"):
                obj.Degree = 4
            obj.WorkYears = WorkYears
            obj.Tel = Tel
            obj.Salary = Salary
            obj.save()
            newrecord = Record.objects.create(text=request.user.username + " 修改了用户信息：" + us.username)
            newrecord.save()
            context = {}
            info = Engineer.objects.all()
            context['engineers'] = info
            return HttpResponseRedirect(reverse('engineeradmin:all_user'))
        else:
            context = {}
            info=Engineer.objects.all()
            context['engineers']=info
            return render(request, 'all_user.html', context)

@login_required()
def delete_user(request,userid):
    if(request.user.username!="admin"):
        return HttpResponseRedirect(reverse('web:index'))
    else:

        user=User.objects.get(id=userid)

        newrecord = Record.objects.create(text=request.user.username + " 删除了用户：" +user.username)
        newrecord.save()

        user.delete()
        return HttpResponseRedirect(reverse('engineeradmin:all_user'))


@login_required()
def all_record(request):
    if (request.user.username != "admin"):
        return HttpResponseRedirect(reverse('web:index'))
    else:
        context={}
        record=Record.objects.all()
        context['records'] = record
        return render(request, 'all_record.html', context)