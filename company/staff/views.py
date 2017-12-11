# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect 
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate, login 
from .forms import LoginForm,PostForm,ResumeForm,SearchForm,UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Applicant,Client,Recuiter
from django.core.urlresolvers import reverse
import cStringIO as StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context

@login_required 
def dashboard(request):
	return render(request,'staff/dashboard.html',{'section': 'dashboard'}) 

	# Create your views here.

def user_login(request):    
	if request.method == 'POST':        
		form = LoginForm(request.POST)        
		if form.is_valid():            
			cd = form.cleaned_data            
			user = authenticate(username=cd['username'],                                
			password=cd['password'])            
			if user is not None:                
				if user.is_active:                    
					login(request, user)                    
					return HttpResponse('Authenticated successfully')                
				else:                    
					return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
		else:
			form = LoginForm()
		return render(request, 'staff/login.html', {'form': form})

def register(request):
	if request.method=='POST':
		user_form=UserRegistrationForm(request.POST)
		if user_form.is_valid():
			new_user=user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			return render(request,'staff/register_done.html',{'new_user':new_user})
	else:
		user_form=UserRegistrationForm()
	return render(request,'staff/register.html',{'user_form':user_form})
		
def recuiter_name(request):
	obj1=Recuiter.objects.all()
	return render(request,'recuiter.html',{'recuiter_name' : obj1})

def client_name(request):
	obj2=Client.objects.all()
	return render(request,'client.html',{'client_name' : obj2})

def applicant_name(request):
	obj3=Applicant.objects.all()
	return render(request,'applicant.html',{'applicant_name' : obj3})

def change(request,id=None):
	instance=get_object_or_404(Recuiter,id=id)
	form=SearchForm(request.POST)
	if request.method=='POST':
		instance=form.save(commit=False)
		instance.save()
	return render(request,'change.html',{'change':instance, 'form':form})

def add(request):
	form=PostForm(request.POST)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect("/staff/recname/")
	return render(request, 'post.html',{'form':form} )	

def delete(request,id=None):
	instance=get_object_or_404(Recuiter,id=id)
	instance.delete()
	return redirect("/staff/recname/")

def upload_resume(request):
	form=ResumeForm(request.POST)
	if request.method=='POST':
		if form.is_valid():
			instance=form.save(commit=False)
			instance.save()
			return redirect("/staff/resume/")
	return render(request, 'resume.html',{'form':form})

def render_to_pdf(template_src, context_dict):
	template = get_template(template_src)
	context = Context(context_dict)
	html  = template.render(context)
	result = StringIO.StringIO()
	pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def my_view(request):
	firstname=""
	lastname=""
	projectdescription=""
	universityname=""
	languagesknow=""
	email=""
	contactnumber=""
	form=ResumeForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		firstname=request.POST['fname']
		lastname=request.POST['lname']
		projectdescription=request.POST['description']
		universityname=request.POST['uniname']
		languagesknow=request.POST['languagesknow']
		email=request.POST['email']
		contactnumber=request.POST['contactnumber']
	return render_to_pdf('entries.html',{'pagesize':'A4', 'languagesknow':languagesknow, 'email':email, 'contactnumber':contactnumber, 'firstname':firstname, 'lastname':lastname ,'projectdescription':projectdescription, 'universityname':universityname })

def get_resume(request):
	if request.method=='GET':
		ob=Applicant.objects.filter(languagesknow__icontains='python')
	return render(request,'get_resume.html', {'applicantsname':ob})














