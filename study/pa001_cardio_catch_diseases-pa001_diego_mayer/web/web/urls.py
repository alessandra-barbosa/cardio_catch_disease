from django.contrib import admin
from django.urls import path
from app.views import form_post, prediction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', form_post, name='form'),
    path('prediction/', prediction, name='prediction'),
]