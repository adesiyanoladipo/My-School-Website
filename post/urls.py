from django.conf.urls import url
from post import views

urlpatterns = [     
url(r'^posts/$', views.index, name='post'),
url(r'^posts/(?P<post_id>\d+)/$', views.detail),
]