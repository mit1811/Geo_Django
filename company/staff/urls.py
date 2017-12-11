from django.conf.urls import url 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [ 
				url(r'^$', views.dashboard, name='dashboard'),
				url(r'^login/$', auth_views.login, name='login'),
				url(r'^logout/$',auth_views.logout,name='logout'),
				url(r'^logout-then-login/$',auth_views.logout_then_login,name='logout_then_login'),
				url(r'^register/$', views.register, name='register'),
				url(r'^(?P<id>\d+)/$', views.change,name='change_by_id'),
				url(r'^recname/$', views.recuiter_name,name='recuiter'),
				url(r'^cliname/$', views.client_name,name='client'),
				url(r'^aplname/$', views.applicant_name,name='applicant'),
				url(r'^(?P<id>\d+)/delete/$', views.delete),
				url(r'^create/$', views.add),
				url(r'^upload/$', views.upload_resume,name='upload'),
				url(r'^pdf/$', views.my_view,name='pdf'),
				url(r'^resume/$', views.get_resume,name='resume'),
			  ]
