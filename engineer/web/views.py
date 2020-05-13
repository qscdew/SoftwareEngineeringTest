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

def index(request):
    context ={}
    # if(request.user.is_authenticated):
    #     userinfo = UserInfo.objects.get(user=request.user)
    #     context ['userinfo']=userinfo

    return render(request, 'index.html', context)


def userlogin(request):
        if (request.method == 'POST'):

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                if(username=="admin"):
                    return HttpResponseRedirect(reverse('engineeradmin:index'))
                else:
                    return HttpResponseRedirect(reverse('engineeruser:index'))
            else:
                context = {"error": "用户名或密码错误"}
                return render(request, 'index.html', context)
        else:

            return render(request, 'index.html')


@login_required()
def edit_password(request):
    context = {}
    if (request.method == 'POST'):
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        user=request.user
        if(pass1==pass2):
            user.set_password(pass1)
            user.save()

            context['info']="修改成功！"
            return render(request, "edit_password.html", context)
        else:
            context['info']="修改失败，密码不一致。"

            return render(request, "edit_password.html", context)
    else:
        return render(request, "edit_password.html", context)

def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('web:index'))
