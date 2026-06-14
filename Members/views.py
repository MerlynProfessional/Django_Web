from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member_class

def Member(Request):
    Model=Member_class.objects.all().values()
    templates =loader.get_template('all members.html')
    context={
        'MyMember':Model
    }

    return HttpResponse(templates.render(context, Request))

def details(Request, id):
    Model = Member_class.objects.get(id=id)
    templates=loader.get_template('details.html')
    context={
        'MyMember':Model
    }
    return HttpResponse(templates.render(context, Request))

# Create your views here.
def main(Request):
    templates=loader.get_template('main.html')
    return HttpResponse(templates.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))