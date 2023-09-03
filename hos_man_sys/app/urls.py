from . import views
from django.urls import include, path

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('appointment',views.appointment),
    path('doctors',views.doctors),
    path('contact',views.contact),
]