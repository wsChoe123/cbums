"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path

from cbums.views import defaultPage
from cbums.views import signUp
from cbums.views import inputCode
from cbums.views import inputInfo
from cbums.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', defaultPage.defaultPage, name="root"),
    path('signUp/',signUp.signUp, name="signup"),
    path('inputCode/',inputCode.inputCode, name = "inputcode"),
    path('inputInfo/',inputInfo.inputInfo, name="inputinfo"),
    path('login/',login.login, name="login"),
]

