from django.urls import path,include
from . views import (PostListView,)
from . import views


app_name ='insta'
#local: http://127.0.0.1:8000/
urlpatterns= [
     path('post/', PostListView.as_view(), name="post_list"),
     path('', views.index, name='home'),
]