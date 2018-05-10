from blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse


def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

def view_post(request):   
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog)
    })

def view_category(request):
    category = get_object_or_404(Category)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })




# Create your views here.
