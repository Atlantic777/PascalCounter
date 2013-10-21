# Create your views here.
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.template import Context
from models import *

def home(request):
    sessions = Session.objects.order_by('-date').all()
    return render(request, 'home.html', Context({'sessions_list':sessions}))

def new_session(request):
    session = Session()
    session.save()
    return HttpResponse('New session created <a href="/get_session/'+str(session.id)+'/">click</a>')

def get_session(request, session_id):
    session = Session.objects.get(id=session_id)
    return render(request, 'counter.html', Context({'session':session}))

def session_api(request, session_id):
    session = Session.objects.get(id=session_id)
    session.increase()
    return HttpResponse(str(session.counter))
