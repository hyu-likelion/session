from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Todolist
import datetime
from django.http import HttpResponse
# Create your views here.

@csrf_exempt
def select(request):
    data = Todolist.objects.all()
    ret = []
    for i in data:
        ret.append([i.id, i.mainText, i.created_at.strftime('%Y-%m-%d'), i.is_approve])
    ret = json.dumps(ret)
    return HttpResponse(ret, status=200)

@csrf_exempt
def update(request):
    data = Todolist.objects.get(id=request.POST['id'])
    data.is_approve = not data.is_approve
    data.save()
    return HttpResponse("성공", status=200)

@csrf_exempt
def delete(request):
    data = Todolist.objects.get(id=request.POST['id'])
    data.delete()
    return HttpResponse("성공", status=200)

@csrf_exempt
def insert(request):
    data = Todolist.objects.create(mainText=request.POST['mainText'])
    return HttpResponse("성공", status=200)

