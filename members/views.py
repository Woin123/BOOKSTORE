from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

#import models
from .models import *


def details(request):
	members = Member.objects.all()
	context = {
		'mymember' : members
	}
	return render(request, 'details.html', context)

# Create your views here.
def members(request):
	mymember=Member.objects.all()
	#Create a context dictionary
	template = loader.get_template('all_members.html')
	#Load the template
	context = {
		'mymember': mymember,
	}
	return HttpResponse(template.render(context, request))

#Create a view for a single member
def details(request, id):
	mymember=Member.objects.get(id=id)
	#Create a context dictionary
	template = loader.get_template('details.html')
	#Load the template
	context = {
		'mymember': mymember,
	}
	return HttpResponse(template.render(context, request))

def main(request):
	template = loader.get_template('main.html')
	return HttpResponse(template.render())


def findmember(request):
  mydata = Member.objects.filter(author='Author3').values()
  template = loader.get_template('findmember.html')
  context = {
    'mymember': mydata,
  }
  return HttpResponse(template.render(context, request))

def findmember1(request):
  mydata = Member.objects.filter(is_available=False).values()
  template = loader.get_template('findmember.html')
  context = {
    'mymember': mydata,
  }
  return HttpResponse(template.render(context, request))

def findmember2(request):
  mydata = Member.objects.filter(publication_date__gt='2023-01-01').values()
  template = loader.get_template('findmember.html')
  context = {
    'mymember': mydata,
  }
  return HttpResponse(template.render(context, request))