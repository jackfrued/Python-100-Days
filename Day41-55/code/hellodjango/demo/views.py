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
                request.session['user'] = user
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


def check_username(request):
    ctx = {}
    if 'username' in request.GET:
        username = request.GET['username']
        try:
            User.objects.get(username__exact=username)
            ctx['valid'] = False
        except User.DoesNotExist:
            ctx['valid'] = True
    return HttpResponse(json.dumps(ctx),
                        content_type='application/json; charset=utf-8')


def show_subjects(request):
    if 'user' in request.session and request.session['user']:
        ctx = {'subjects_list': Subject.objects.all()}
        return render(request, 'demo/subject.html', ctx)
    else:
        return render(request, 'demo/login.html',
                      {'hint': '请先登录!'})


def show_teachers(request, no):
    if 'user' in request.session and request.session['user']:
        teachers = Teacher.objects.filter(subject__no=no)\
            .select_related('subject')
        ctx = {'teachers_list': teachers}
        return render(request, 'demo/teacher.html', ctx)
    else:
        return render(request, 'demo/login.html',
                      {'hint': '请先登录!'})


def make_comment(request, no):
    ctx = {'code': 200}
    if 'user' in request.session and request.session['user']:
        user = request.session['user']
        if user.counter > 0:
            try:
                teacher = Teacher.objects.get(pk=no)
                if request.path.startswith('/good'):
                    teacher.good_count += 1
                    ctx['result'] = f'好评({teacher.gcount})'
                else:
                    teacher.bad_count += 1
                    ctx['result'] = f'差评({teacher.bcount})'
                teacher.save()
                user.counter -= 1
                User.objects.filter(username__exact=user.username)\
                    .update(counter=user.counter)
                request.session['user'] = user
            except Teacher.DoesNotExist:
                ctx['code'] = 404
        else:
            ctx['code'] = 403
            ctx['result'] = '票数不足'
    else:
        ctx['code'] = 302
        ctx['result'] = '请先登录'
    return HttpResponse(json.dumps(ctx),
                        content_type='application/json; charset=utf-8')
