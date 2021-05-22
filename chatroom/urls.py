from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('login', views.login_page, name='login'),
	path('chat/<str:roomname>', views.chatroom, name='chatroom'),	
	path('logout', views.logout_page, name='logout'),
]