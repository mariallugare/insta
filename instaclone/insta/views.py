from django.shortcuts import render
from .models import post
from django.views.generic import (ListView)
# Create your views here.

class PostisView(ListView):
    template_name = "insta/post_lists.html"
    Queryset =post.objects.all()
    context_object_name ='posts'
