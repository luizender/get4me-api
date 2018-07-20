"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from rest_auth.views import LoginView, LogoutView
from get4me.views import BuyersView, GuardiansView, PostcodeView

router = routers.DefaultRouter()
router.register(r'buyers/profile', BuyersView, base_name='buyers/profile')
router.register(r'guardians/profile', GuardiansView, base_name='guardians/profile')
router.register(r'guardians/search', PostcodeView, base_name='guardians/search')

urlpatterns = [
    url(r'^login/', LoginView.as_view()),
    url(r'^logout/', LogoutView.as_view()),
    url(r'', include(router.urls)),
]

if settings.DEVELOP_MODE:
    urlpatterns.append(url(r'^admin/', admin.site.urls))
