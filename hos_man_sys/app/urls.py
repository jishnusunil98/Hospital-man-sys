from . import views
from django.urls import include, path

urlpatterns = [
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('appointment',views.appointment,name="appointment"),
    path('doctors',views.doctors,name="doctors"),
    path('contact',views.contact,name="contact"),
]