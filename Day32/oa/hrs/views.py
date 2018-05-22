from django.shortcuts import render

from hrs.models import Dept, Emp


def index(request):
    ctx = {
        'greeting': '你好，世界！'
    }
    return render(request, 'index.html', context=ctx)


def emps(request):
    dno = int(request.GET['dno'])


def depts(request):
    # DRY - Don't Repeat Yourself
    # ORM - Object Relation Mapping
    ctx = {'dept_list': Dept.objects.all()}
    return render(request, 'dept.html', context=ctx)
