from django.urls import path
from . import  views 

urlpatterns=[
path('',views.home,name='home'),
path('login/',views.login_user),
path('logout',views.logout_user),
path('register/',views.register),
path('api/',views.api),
path('cuser/',views.cuser),
path('addpost',views.addpost,name='addpost')
]