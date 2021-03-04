from django.urls import path
from . import views



urlpatterns = [
    path("", views.index  ,  name = "home-page" ),
    path("info/", views.info,  name = "info-page"), 
    path("create/", views.create, name="create-page")
    , path("update/<int:pk>", views.update,  name = "update-page"),
    path("delete/<int:pk>", views.delete, name =  "delete-page" )
    
    ]