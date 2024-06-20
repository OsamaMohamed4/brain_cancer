
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name= 'home' ),
    path('overflow/',views.overflow_page,name = 'overflow'),
    path('team/',views.team,name = 'team'),
    path('model/',views.model_page,name = 'model'),
    path('profile/',views.profile,name = 'profile'),
    path('history/',views.history,name = 'history'),
    #authentication 
    path('register/',views.register,name = 'register'),
    path('login/', views.login_view, name='login'),
    path('login_required/', views.signin_required, name='login_required'),
]
