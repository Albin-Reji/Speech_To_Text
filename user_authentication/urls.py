from  django.urls import path
from . import views

urlpatterns=[
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('signup/login/', views.success, name='success'),
    path('user/<str:username>/', views.user, name='user'),
]