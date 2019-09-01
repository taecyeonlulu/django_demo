
import json
from django.shortcuts import render,HttpResponse
from django.views.generic.base import View

# Create your views here.

class LoginView(View):
    def get(self,request):
        # 渲染登录页面
        return render(request,'login.html')

    def post(self,request):
        # 登录逻辑
        return HttpResponse(json.dumps(request.POST))

class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
