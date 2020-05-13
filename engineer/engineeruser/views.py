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
from .models import Engineer
from engineeradmin.models import Record
@login_required()
def index(request):
    context = {}
    # if(request.user.is_authenticated):
    #     userinfo = UserInfo.objects.get(user=request.user)
    #     context ['userinfo']=userinfo
    info=Engineer.objects.get(User=request.user)
    context['info']=info
    return render(request, 'detail.html', context)

@login_required()
def edit_detail(request):
    if (request.method == 'POST'):
        Id=request.POST.get('Id')
        Name=request.POST.get('Name')
        Sex=request.POST.get('Sex')
        Birthday=request.POST.get('Birthday')
        NativePlace=request.POST.get('NativePlace')
        Address=request.POST.get('Address')
        Degree=request.POST.get('Degree')
        WorkYears=request.POST.get('WorkYears')
        Tel=request.POST.get('Tel')
        Salary=request.POST.get('Salary')
        # print(Id)
        # print(Name)
        # print(Sex)
        # print(Birthday)
        # print(NativePlace)
        # print(Address)
        # print(Degree)
        # print(WorkYears)
        # print(Tel)
        # print(Salary)
        obj=Engineer.objects.get(User=request.user)
        obj.Id=Id
        obj.Name=Name
        if(Sex=="男"):
            obj.Sex=1
        elif(Sex=="女"):
            obj.Sex=0
        obj.Birthday=Birthday
        obj.NativePlace=NativePlace
        obj.Address=Address
        if(Degree=="高中"):
            obj.Degree=0
        elif(Degree=="学士"):
            obj.Degree=1
        elif (Degree == "硕士"):
            obj.Degree = 2
        elif (Degree == "博士"):
            obj.Degree = 3
        elif (Degree == "其它"):
            obj.Degree = 4
        obj.WorkYears=WorkYears
        obj.Tel=Tel
        obj.Salary=Salary
        obj.save()
        newrecord = Record.objects.create(text=request.user.username + " 修改了用户信息：" + us.username)
        newrecord.save()
        context = {}
        # if(request.user.is_authenticated):
        #     userinfo = UserInfo.objects.get(user=request.user)
        #     context ['userinfo']=userinfo
        info = Engineer.objects.get(User=request.user)
        context['info'] = info
        return render(request, 'edit_detail.html', context)
    else:
        context = {}
        # if(request.user.is_authenticated):
        #     userinfo = UserInfo.objects.get(user=request.user)
        #     context ['userinfo']=userinfo
        info = Engineer.objects.get(User=request.user)
        context['info'] = info
        return render(request, 'edit_detail.html', context)
def isDigit(x):
    try:
        x=int(x)
        return isinstance(x,int)
    except ValueError:
        return False

def search(request):
    context = {}
    if (request.method == 'POST'):
        content=request.POST.get('content')
        content2=request.POST.get('exampleFormControlSelect1')
        if(content2=="编号"):
            if(isDigit(content)):
                engineers = Engineer.objects.filter(Id=content)
            else:
                engineers = Engineer.objects.filter(Name=content)
        else:
            engineers=Engineer.objects.filter(Name=content)



        context['engineers'] = engineers
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html',context)

def all_engineer(request):
    context = {}
    engineers=Engineer.objects.all()
    context['engineers']=engineers
    return render(request, 'all_engineer.html', context)

from decimal import Decimal
def calc_salary(request):
    context = {}
    if (request.method == 'POST'):
        days = float(request.POST.get('days'))#月有效工作日天数
        id=request.POST.get('id')#工程师编号
        month=float(request.POST.get('month'))#月效益
        month_insurance=float(request.POST.get('month_ins'))#月保险金

        engineer = Engineer.objects.get(Id=id)
        mon_salary=(float(engineer.Salary)+10*days+month*float(engineer.WorkYears)/100)*0.9-month_insurance*1.0
        context['month_salary'] = mon_salary
        return render(request, 'calc_salary.html', context)
    else:
        return render(request, 'calc_salary.html', context)

def sort(request):
    context = {}
    return render(request, 'sort.html', context)
def sort_id(request):
    context = {}
    engineers = Engineer.objects.all().order_by('Id')
    context['engineers'] = engineers
    context['sort']="id"

    return render(request, 'sort.html', context)
def sort_name(request):
    context = {}
    engineers = Engineer.objects.all().order_by('Name')
    context['engineers'] = engineers
    context['sort'] = "name"

    return render(request, 'sort.html', context)
def sort_workyears(request):
    context = {}
    engineers = Engineer.objects.all().order_by('WorkYears')
    context['engineers'] = engineers
    context['sort'] = "workyears"

    return render(request, 'sort.html', context)

def sort_id_reverse(request):
    context = {}
    engineers = Engineer.objects.all().order_by('-Id')
    context['engineers'] = engineers
    context['sort']="id"

    return render(request, 'sort.html', context)
def sort_name_reverse(request):
    context = {}
    engineers = Engineer.objects.all().order_by('-Name')
    context['engineers'] = engineers
    context['sort'] = "name"
    return render(request, 'sort.html', context)
def sort_workyears_reverse(request):
    context = {}
    engineers = Engineer.objects.all().order_by('-WorkYears')
    context['engineers'] = engineers
    context['sort'] = "workyears"
    return render(request, 'sort.html', context)
