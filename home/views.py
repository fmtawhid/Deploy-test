from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q

# Create your views here.
def home_page(request):
    article = blog.objects.all()
    promotion_post = blog.objects.filter(post_filter='PR')
    latest_news = blog.objects.all().order_by('-date')[:6]
    

    #Common Function
    Category = category.objects.all()
    feature_post = blog.objects.filter(post_filter='F')[:3]

    #search function
    search = request.GET.get('q')
    if search:
        latest_news = latest_news.filter(
            Q(title__icontains=search)
        )

    context = {
        'article':article,
        'feature_post':feature_post,
        'latest_news':latest_news,
        'Category':Category,
        'promotion_post':promotion_post,
        'search':search,
    }
    return render(request, 'index.html', context)


def single_page(request, slug):
    single_article = get_object_or_404(blog, slug=slug)
    #Common Function
    Category = category.objects.all()
    feature_post = blog.objects.filter(post_filter='F')[:3]
   

    

    context = {
        'single_article':single_article,
        'Category':Category,
        'feature_post':feature_post,
       
    }
    return render(request, 'single.html',context)

def topic(request, name):
    cat_filter = get_object_or_404(category, name=name)
    post = blog.objects.filter(category=cat_filter.id)
     #Common Function
    Category = category.objects.all()
    feature_post = blog.objects.filter(post_filter='F')[:3]
    #search function
    search = request.GET.get('q')
    if search:
        post = post.filter(
            Q(title__icontains=search)
        )

    
    context = {
        'cat_filter':cat_filter,
        'post':post,
        'Category':Category,
        'feature_post':feature_post,
        'search':search,
        
    }
    return render(request, 'category.html', context)

def contact_page(request):
    return render(request, 'contact.html')
