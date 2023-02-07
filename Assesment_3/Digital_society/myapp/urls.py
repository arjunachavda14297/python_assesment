from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('notice/',views.notice,name='notice'),
    path('login/',views.login,name='login'),
    path('forgot/',views.forgot,name='forgot'),
    path('contact/',views.contact,name='contact'),
    path('signup',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('change_password/',views.change_password,name='change_password'),
    path('change_profile/',views.change_profile,name='change_profile'),
    path('add_notice/',views.add_notice,name='add_notice'),
    path('add_event/',views.add_event,name='add_event'),
    path('notice/',views.notice,name='notice'),
    path('event/',views.event,name='event'),
    path('add_member/',views.add_member,name='add_member'),
    path('member_change_password/',views.member_change_password,name='member_change_password'),
    path('member_change_profile/',views.member_change_profile,name='member_change_profile'),
    path('special_member/',views.special_member,name='special_member'),
    path('member/<str:member_type>',views.member,name='member'),
    path('add_visitor/',views.add_visitor,name='add_visitor'),
]