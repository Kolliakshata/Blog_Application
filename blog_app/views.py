from django.shortcuts import render

from django.views import generic
from .models import Post
from . import views

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'detail.html'



def home(response): # Don't indent this!
    return render(response, "home.html", {})



