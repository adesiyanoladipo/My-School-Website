from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.forms import RegistrationForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext, loader
from post.models import Post
import ssl
from accounts.forms import UserUpdateForm, ProfileUpdateForm
import smtplib
from smtplib import SMTP
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.contrib import messages
from django.template import RequestContext
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from home.forms import ProfileModelForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

#Create your views here.	
def register(request):
    registered = False
    if request.method == "POST":
        user_form = RegistrationForm(data=request.POST)
        profile_form = ProfileModelForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect("/success")

        else:
            user_form = RegistrationForm()
            profile_form = ProfileModelForm()

            return render(request, "reg_form.html",
                    {'user_form':RegistrationForm,
                           'profile_form':ProfileModelForm,
                           'registered':registered})

          



    form2 = ProfileModelForm
    form = RegistrationForm
    return render(request = request,
                  template_name = "reg_form.html",
                                 context={"form":form, "form2":form2 })

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

@login_required
def success(request):
  def read_creds():
      user = passw = ""
      with open("files/core_files/credential.txt", "r") as f:
          file = f.readlines()
          user = file[0].strip()
          passw = file[1].strip()

      return user, passw

  receive = [request.user.email]

  port = 465
  sender, password = read_creds()

  message = """From:  Messiah ICT TEAM <from@noreply>
To: You You
Subject: Your e-portal as being successfully created

Dear student, your account as being successfully created. With your e-portal, you can check your payment record, result and any other information you need. Enjoy!.
"""
  context = ssl.create_default_context()

  with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
      server.login(sender, password)
      server.sendmail(sender, receive, message)

  return render(request, 'reg_form2.html')

def index(request):
    template_name = 'users.html'    
    users = User.objects.all()  
    profile = Profile.objects.all()
    args = {
        'users': users,
        'profile': Profile
                   }
    return render(request, template_name, args)                                               

def view_profile(request):
	args = {'user': request.user},
	return render(request, 'profile.html')

@login_required
def edit_profile(request):
    if request.method == "POST":        
      form = UserUpdateForm(request.POST, instance=request.user)
      form2 = ProfileUpdateForm(request.POST, instance=request.user.profile)
      if form.is_valid() and form2.is_valid():
        form.save()
        form2.save()
        return redirect('view_profile')
    else: 
        form = UserUpdateForm(instance=request.user)
        form2 = ProfileUpdateForm(instance=request.user.profile)

    context = {"form":form,
              "form2":form2}

    return render(request, "edit_profile.html", context)
                  
    
	          
def users_list(request):
    template_name = 'users.html'    
    users = User.objects.all()  
    profile = Profile.objects.all()
    args = {
        'users': users,
        'profile': Profile
                   }
    return render(request, template_name, args)

	  
@login_required
def change_password(request):
	if request.method == 'POST':
            form = PasswordChangeForm(request.POST)
            if form.is_valid():
	              form.save()  
	              return redirect('http://127.0.0.1:8000/accounts/profile')
	else:
		           form = PasswordChangeForm(user=request.user)	
		           args = {'form': form}
		           return render(request, 'change_password.html', args)
		           
def view_results(request):
	model : Result
	return render(request, 'result.html')
	
def view_resultss(request):
	model : Result
	return render(request, 'results.html')
	
def accounts(request):
	return render(request, 'account.html')
       
def profile(request):
	return render(request, 'profile2.html')
