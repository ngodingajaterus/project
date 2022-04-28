
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path , include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('elearning/',include('elearning.urls')),
    path('account/',include('account.urls')),
]
