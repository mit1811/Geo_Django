from django.conf.urls import url 
from . import views

urlpatterns = [ 
				 url(r'^home/$', views.poi_list,name='home'),
				] 