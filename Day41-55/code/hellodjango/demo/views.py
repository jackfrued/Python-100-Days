import json

from django.http import HttpResponse
from django.shortcuts import render

from demo.models import Subject, Teacher


def index(request):
    ctx = {'subjects_list': Subject.objects.all()}
    return render(request, 'demo/index.html', ctx)


def show_teachers(request, no):
    teachers = Teacher.objects.filter(subject__no=no)
    ctx = {'teachers_list': teachers}
    return render(request, 'demo/teacher.html', ctx)


def make_good_comment(request, no):
    teacher = Teacher.objects.get(pk=no)
    teacher.good_count += 1
    teacher.save()
    ctx = {'code': 200, 'result': f'好评({teacher.good_count})'}
    return HttpResponse(json.dumps(ctx),
                        content_type='application/json; charset=utf-8')


def make_bad_comment(request, no):
    teacher = Teacher.objects.get(pk=no)
    teacher.bad_count += 1
    teacher.save()
    ctx = {'code': 200, 'result': f'差评({teacher.bad_count})'}
    return HttpResponse(json.dumps(ctx),
                        content_type='application/json; charset=utf-8')
