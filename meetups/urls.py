from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'all_meetups'),
    path('<slug:meetup_slug>/success/', views.registration_succesful, name = 'registration_succesful' ),
    path('<slug:meetup_slug>/', views.meetup_details, name = 'detailed_meetups')
] 