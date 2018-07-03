from django.shortcuts import render

from demo.models import Teacher


def home(request):
    # 通过ORM框架实现持久化操作CRUD
    ctx = {'teachers_list': list(Teacher.objects.all())}
    return render(request, 'demo/home.html', ctx)
