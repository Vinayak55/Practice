from django.urls import path
from . import views
urlpatterns =[
    path('',views.Post_details,name = "post_details")
]