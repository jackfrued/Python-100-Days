import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

from demo.forms import UserForm
from demo.models import Subject, Teacher, User, proto


def login(request):
    if request.method.lower() == 'get':
        return render(request, 'demo/login.html', {})
    else:
        username = request.POST['username']
        try:
            user = User.objects.get(username__exact=username)
            password = request.POST['password']
            hasher = proto.copy()
            hasher.update(password.encode('utf-8'))
            if hasher.hexdigest() == user.password:
                return redirect('sub')
        except User.DoesNotExist:
            pass
        return render(request, 'demo/login.html',
                      {'hint': '用户名或密码错误'})



def register(request):
    form = UserForm()
    if request.method.lower() == 'get':
        return render(request, 'demo/register.html', {'f': form})
    else:
        ctx = {}
        try:
            form = UserForm(request.POST)
            ctx['f'] = form
            if form.is_valid():
                form.save(commit=True)
                ctx['hint'] = '注册成功请登录!'
                return render(request, 'demo/login.html', ctx)
        except:
            ctx['hint'] = '注册失败, 请重新尝试!'
    return render(request, 'demo/register.html', ctx)


def show_subjects(request):
    ctx = {'subjects_list': Subject.objects.all()}
    return render(request, 'demo/subject.html', ctx)


def show_teachers(request, no):
    teachers = Teacher.objects.filter(subject__no=no)
    ctx = {'teachers_list': teachers}
    return render(request, 'demo/teacher.html', ctx)


def make_comment(request, no):
    ctx = {'code': 200}
    try:
        teacher = Teacher.objects.get(pk=no)
        if request.path.startswith('/good'):
            teacher.good_count += 1
            ctx['result'] = f'好评({teacher.gcount})'
        else:
            teacher.bad_count += 1
            ctx['result'] = f'差评({teacher.bcount})'
        teacher.save()
    except Teacher.DoesNotExist:
        ctx['code'] = 404
    return HttpResponse(json.dumps(ctx),
                        content_type='application/json; charset=utf-8')
