from django.urls import path
from . import  views 

urlpatterns=[
path('',views.home,name='home'),
path('login/',views.login_user),
path('logout',views.logout_user),
path('register/',views.register),
path('api/',views.api),
path('cuser/',views.cuser),
path('addpost',views.addpost,name='addpost'),
path('getposts/',views.getposts),
path('addposts',views.addpost),
path('single/<id>',views.single),
path('delete/<id>',views.deletepost),
path('update/<id>',views.updatepart)

]