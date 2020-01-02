from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import *

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_blog_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Blog.objects.order_by('date_published')[:5]

class DetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/detail.html'
    

def detail(request, post_id):
    blog = get_object_or_404(Blog, pk=post_id)
    return HttpResponse(blog.body)