from django.conf.urls import url
from django.urls import path, include
from home import views
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth.views import (
LoginView, LogoutView)

urlpatterns = [      
       url(r'^$', views.home),
       url(r'^gallery', views.gallery),
       url(r'^wywlu', views.wywlu, name='wywlu'),
       url(r'^know_more', views.more, name='more'),
       path('login/', LoginView.as_view(), name='login'),
       path('accounts/profile/logout', views.user_logout),   
       path('profile/logout', views.user_logout),   
]
