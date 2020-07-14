from django.contrib.auth import authenticate, login, logout
from django.conf.urls import url
from django.urls import path, include
from accounts import views
from django.contrib.auth.views import (
LoginView, LogoutView)
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [      
  url(r'^accounts/profile/view-results/$', views.view_results, name='view_results'),
  url(r'^accounts/profile/view-resultss/$', views.view_resultss, name='view_resultss'),     
  url(r'^profile/view-results/$', views.view_results, name='view_results'),    
  url(r'^profile/view-resultss/$', views.view_resultss, name='view_resultss'),
  url(r'^accounts/profile/password/$', views.change_password, name='change_password'),   
  url(r'^profile/password/$', views.change_password, name='change_password'),   
  url(r'^accounts/profile/$', views.view_profile, name='view_profile'),  
  url(r'^profile/$', views.view_profile, name='view_profile'), 
  url(r'^profiles/$', views.index, name='index'), 
  url(r'^profile/$', views.view_profile, name='view_profile'),    
  url(r'^register/$', views.register, name='register'),
  url(r'^register/register/$', views.register, name='register'),
  url(r'^profile/edit/$', views.edit_profile, name='profile_edit'),
  url(r'^accounts/profile/edit/$', views.edit_profile, name='profile_edit'), 
  url(r'^success/$', views.success, name='success'),
  path('logout/', LogoutView),
  url(r'^accounts/$', views.accounts, name='accounts'),
  url(r'^accounts/profile2/$', views.profile),
  path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
  path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),
  path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete")
]