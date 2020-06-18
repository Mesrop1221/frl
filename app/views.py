from django.shortcuts import render,redirect
from django.views.generic import View
from .models import Post,Group,Links,Type
from django.core.paginator import Paginator
import random
from .send_email import mail

def index(request):
    
    groups = Group.objects.all()
    links = Links.objects.all()
    types = Type.objects.all()
    l = []
    
    for g in Group.objects.all():
        for post in list(Post.objects.filter(group=g))[-4:]:
            l.append(post)
    
    return render(request,'main_html/index.html',{'types':types,'groups':groups,'l':l,'links':links})


def group_detail(request,slug):

    links = Links.objects.all()
    
    groups = Group.objects.all()
    group = Group.objects.get(group_slug=slug)
    types = Type.objects.all()
    
    posts = Post.objects.filter(group=group)
    paginator = Paginator(posts,4)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'main_html/item.html',{'groups':groups,'posts':page_obj ,'types':types,'links':links,'group':group})

def type_detail(request,type_id):

    links = Links.objects.all()
    
    groups = Group.objects.all()
    type = Type.objects.get(id=type_id)
    types = Type.objects.all()
    
    posts = Post.objects.filter(type=type)
    paginator = Paginator(posts,4)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'main_html/type_item.html',{'groups':groups,'posts':page_obj ,'types':types,'links':links})


def post_detail(request,pk):
    
    post = Post.objects.get(id=pk)
    groups = Group.objects.all()
    types = Type.objects.all()

    all_post = list(Post.objects.all())
    post_len = len(all_post)
    r = random.randint(0,post_len-1)
    
    if r < 4:
        random_posts = all_post[r:r+4]

    else:
        random_posts = all_post[r-4:r]    
    
    links = Links.objects.all()

    return render(request,'main_html/morepage.html',{'post':post,'groups':groups,'types':types,'links':links,'random_posts':random_posts})

def politic(request):

    links = Links.objects.all()
    
    groups = Group.objects.all()

    types = Type.objects.all()

    return render(request,'contact/pol.html',{'groups':groups,'links':links,'types':types})


def contact(request):

    links = Links.objects.all()
    
    groups = Group.objects.all()

    types = Type.objects.all()

    if request.method == 'POST':
        mail(request.POST['name'],request.POST['surname'],request.POST['msg'],request.POST['email'],request.POST['phone'])

    return render(request,'contact/contact.html',{'groups':groups,'links':links,'types':types})
