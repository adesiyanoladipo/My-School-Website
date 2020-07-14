from django.conf.urls import url
from contacts import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
		 url(r'^contacts/$', views.contacts, name='contacts'),
] 