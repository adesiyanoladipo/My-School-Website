from django.shortcuts import render, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from .forms import ContactModelForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from time import strftime
from django.conf import settings
from datetime import date
from django.template import RequestContext, loader
from post.models import Post
from post.forms import PostForm
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def home(request):
  day_time = int(strftime('%H'))
  if day_time < 12:
    latest_post_list = Post.objects.all().order_by('-pub_date')[:2]
    if request.method == "POST":
        form = ContactModelForm(request.POST)        
        if form.is_valid():
            form.save()
            return HttpResponse("Your message as being sent and will be replied through your email")
        else:
              return render(request = request,
                          template_name = "home.html",
                          context={"form":form, "latest_post_list":latest_post_list})
          

    form = ContactModelForm
    return render(request = request,
                  template_name = "home.html",
                  context={"form":form, "latest_post_list":latest_post_list}) 

  elif 12 <= day_time < 18:
    latest_post_list = Post.objects.all().order_by('-pub_date')[:2]
    if request.method == "POST":
        form = ContactModelForm(request.POST)        
        if form.is_valid():
            form.save()
            return HttpResponse("Your message as being sent and will be replied through your email")
        else:
              return render_to_response("afternoon.html", context={"form":form, "latest_post_list":latest_post_list})
          

    form = ContactModelForm
    return render(request = request,
                  template_name = "afternoon.html",
                  context={"form":form, "latest_post_list":latest_post_list}) 

  else:
    latest_post_list = Post.objects.all().order_by('-pub_date')[:2]
    if request.method == "POST":
        form = ContactModelForm(request.POST)        
        if form.is_valid():
            form.save()
            return HttpResponse("Your message as being sent and will be replied through your email")
        else:
              return render(request = request,
                          template_name = "evening.html",
                          context={"form":form, "latest_post_list":latest_post_list})
          

    form = ContactModelForm
    return render(request = request,
                  template_name = "evening.html",
                  context={"form":form, "latest_post_list":latest_post_list}) 



    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def error_404(request, exception):
  return render(request, '404.html')

def error_500(request):
  return render(request, '500.html')

def gallery(request):
	return render(request, 'gallery.html')
	           
def wywlu(request):
	return render(request, 'index.html')

def more(request):
	return render(request, 'index2.html')