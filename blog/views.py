from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'blog/blog_index.html', )


def about(request):
    return HttpResponse("This is a test of Django framework")


def result_demo(request):
    return render(request, 'blog/show_detail.html', )
