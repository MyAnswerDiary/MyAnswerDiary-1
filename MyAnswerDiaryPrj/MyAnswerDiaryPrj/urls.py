from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from myAnswerDiaryApp import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login/', accounts_views.login, name='login'),
    path('signup/', accounts_views.signup, name='signup'),
]
