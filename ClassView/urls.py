from django.contrib import admin
from django.urls import path,include
from ClassView.views import list_1,create_1,detail_1,update_1,delete_1,mixins_1,CRUD_mixin
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
     path('list',list_1.as_view(),name ="list"),
     path('create',create_1.as_view(),name="create"),
     path('detail/<int:pk>',detail_1.as_view(),name="detail"),
     path('update/<int:pk>',update_1.as_view(),name="update"),
     path('delete/<int:pk>',delete_1.as_view(),name="delete"),
     path('mixin1',csrf_exempt(mixins_1.as_view()),name="mixin1"),
     path('crud/<int:pk>',CRUD_mixin.as_view(),name="crud"),
     

]

