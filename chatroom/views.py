from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def index(request):
	return render(request, 'index.html', {})

@login_required(login_url='login')
def chatroom(request, roomname):
	return render(request, 'chat.html', {'roomname': roomname})

def login_page(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		print(user)
		if user is not None:
			login(request, user)
		return HttpResponseRedirect(reverse('index'))
	return render(request, 'login.html', {})

def logout_page(request):
	logout(request)
	return HttpResponseRedirect(reverse('login'))
