from collections import namedtuple

from django.contrib.auth import authenticate, login
import json
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from asu.models import Group, Lesson


def index(request):
    return render(request, '../templates/auth.html')


def notfound(request):
    return render(request, '../templates/404.html')


def auth(request):
    errors = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is None and 'uname' not in errors.keys() and 'psw' not in errors.keys():
            errors['login'] = 'Логин или пароль введены неправильно'

        if not errors:
            login(request, user)
            return HttpResponseRedirect('../groups/')
        else:
            context = {'errors': errors}
            return render(request, 'auth.html', context)

    return render(request, 'auth.html', {'errors': errors})


def groups(request):
    groupList = Group.objects.all()
    return render(request, 'groups.html', {'groups': groupList})


def groupedit(request, id):
    group = Group.objects.get(id=id)
    return render(request, 'groupedit.html', {'group': group})


def loadgroups(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        lessons_list = (Lesson.objects.filter(group=id).values('id','name', 'classroom', 'type', 'time', 'day'))
        lessons_list = list(lessons_list)
        return JsonResponse(json.dumps(lessons_list, ensure_ascii=False), safe=False)
    else:
        return HttpResponse("404")


def editlesson(request): #TODO сделать галочку числитель и знаменатель
    if request.method == 'POST':
        operation = request.POST.get('operation')
        lesson = request.POST.get('lesson')
        lesson = json.loads(lesson, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        if operation == 'add':
            newlesson = Lesson()
            newlesson.name = lesson.name
            newlesson.classroom = lesson.classroom
            newlesson.type = lesson.type
            newlesson.time = lesson.time
            newlesson.day = lesson.day
            newlesson.group_id = lesson.group
            newlesson.save()
        if operation == 'edit':
            newlesson = Lesson.objects.get(id=lesson.id)
            newlesson.name = lesson.name
            newlesson.classroom = lesson.classroom
            newlesson.type = lesson.type
            newlesson.time = lesson.time
            newlesson.day = lesson.day
            newlesson.group_id = lesson.group
            newlesson.save()
        if operation == 'delete':
            newlesson = Lesson.objects.get(id=lesson.id)
            newlesson.delete()

        return HttpResponse("its ok")
    else:
        return HttpResponse("404")


def editgrouplist(request):
    if request.method == 'POST':
        operation = request.POST.get('operation')
        if operation == 'add':
            newgroup = Group()
            newgroup.name = request.POST.get('name')
            newgroup.save()
        if operation == 'edit':
            newgroup = Group.objects.get(id=request.POST.get('id'))
            newgroup.name = request.POST.get('name')
            newgroup.save()
        if operation == 'delete':
            newgroup = Group.objects.get(id=request.POST.get('id'))
            newgroup.delete()
        return HttpResponse("its ok")
    else:
        return HttpResponse("404")


def searchforgroups(request, name):
    if request.method == 'GET':
        groups = Group.objects.filter(name__icontains=name).values()
        groups = list(groups)
        return HttpResponse(json.dumps(groups, ensure_ascii=False))


def searchforlessons(request, id):
    if request.method == 'GET':
        lessons_list = (Lesson.objects.filter(group=id).values('name', 'classroom', 'type', 'time', 'day'))
        lessons_list = list(lessons_list)
        return HttpResponse(json.dumps(lessons_list, ensure_ascii=False))