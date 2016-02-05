from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from accounts.forms import SignupForm, SignupForm2
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
import hashlib, datetime, random
from django.utils import timezone

# Create your views here.
def profile(request):
    return render(request, 'accounts/profile.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm2(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            user =User.objects.get(username=username)
            send_mail('가입 승인 메일', 'http://e0c05682.ngrok.io/accounts/approval/%s' %(activation_key), 'sarkmen@naver.com', [email], fail_silently=False)
            return redirect('/accounts/register_success')
            #return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm2()
    return render(request, 'accounts/signup.html', {'form' : form}, )

def register_success(request):
    return render(request, 'accounts/register_success.html')

'''
def signup(request):
    user = User.objects.create_user('username', 'email', 'password')
    user.is_active=False
    user.save()

    send_mail('가입 승인 메일', 'msg[http://e0c05682.ngrok.io/accounts/approval]', 'sarkmen@naver.com', [user.email], fail_silently=False)
    return HttpResponseRedirect('accounts/register_success.html')
'''
def activate(request,activation_key):
    user=User.objects.get(pk=pk)
    user.is_active=True
    user.save()
    return HttpResponseRedirect('accounts/activation_success.html')




