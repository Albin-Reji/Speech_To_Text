from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('signup/login/', views.success, name='success'),
    path('user/<str:username>/', views.user, name='user'),
    path('user/<str:username>/microphone_input/', views.microphone_input, name='microphone_input'),
    path('user/<str:username>/output/', views.output, name='output'),
]
