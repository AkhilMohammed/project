from django.urls import path

from .import views

app_name='zeroapp'

urlpatterns = [

    path('', views.base),

    path('login',views.login),

    path('signup',views.signup),

    path('otpvalidation',views.otpvalidation),

    path('home',views.home),

    path('signupapi',views.signuplist.as_view()),

    path('logout',views.logout)





]