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

def index(request):
    latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
    return render_to_response('index3.html',  context={"latest_post_list":latest_post_list})
      # (request, {'latest_post_list': latest_post_list}))

def detail(request, post_id):
  p = Post.objects.get(pk=post_id)
  return render_to_response('detail3.html', context={'post': p})
