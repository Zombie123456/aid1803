from django import forms
from .models import *

class RegisterForm(forms.Form):
    uphone = forms.CharField(label='手机号')
    upwd = forms.CharField(label='密码', widget=forms.PasswordInput)
    cupwd = forms.CharField(label='确认密码', widget=forms.PasswordInput)
    uname = forms.CharField(label='用户名')
    uemail = forms.EmailField(label='邮箱')


        