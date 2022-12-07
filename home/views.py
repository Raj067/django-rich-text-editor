from django.shortcuts import render
from .models import Blog
# Create your views here.


def blog(request, *args, **kwargs):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'blog.html', {})
