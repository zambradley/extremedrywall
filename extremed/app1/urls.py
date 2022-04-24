from django.urls import path
from .views import aboutUs, contact, index, paint, texture, tape, hang, service, admin, careers
                

urlpatterns = [
    path('', index, name='index'),
    path('this_is_us', aboutUs, name='about'),
    path('paint', paint, name="paint"),
    path('texture', texture, name="texture"),
    path('tape', tape, name="tape"),
    path('hang', hang, name="hang"),
    path('services', service, name="services"),
    path('careers', careers, name="careers"),
    path('contact', contact, name="contact"),
    path('admin', admin, name="admin"),
]
