from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import ObjectDoesNotExist

from json import dumps

from hrs.models import Dept, Emp


def index(request):
    ctx = {
        'greeting': '你好，世界！'
    }
    return render(request, 'index.html', context=ctx)


def del_dept(request, no='0'):
    try:
        Dept.objects.get(pk=no).delete()
        ctx = {'code': 200}
    except (ObjectDoesNotExist, ValueError):
        ctx = {'code': 404}
    return HttpResponse(
        dumps(ctx), content_type='application/json; charset=utf-8')
    # 重定向 - 给浏览器一个URL, 让浏览器重新请求指定的页面
    # return redirect(reverse('depts'))
    # return depts(request)


def emps(request, no='0'):
    # no = request.GET['no']
    # dept = Dept.objects.get(no=no)
    # ForeignKey(Dept, on_delete=models.PROTECT, related_name='emps')
    # dept.emps.all()
    # emps_list = dept.emp_set.all()
    # all() / filter() ==> QuerySet
    # QuerySet使用了惰性查询 - 如果不是非得取到数据那么不会发出SQL语句
    # 这样做是为了节省服务器内存的开销 - 延迟加载 - 节省空间势必浪费时间
    emps_list = list(Emp.objects.filter(dept__no=no).select_related('dept'))
    ctx = {'emp_list': emps_list, 'dept_name': emps_list[0].dept.name} \
        if len(emps_list) > 0 else {}
    return render(request, 'emp.html', context=ctx)


def depts(request):
    ctx = {'dept_list': Dept.objects.all()}
    return render(request, 'dept.html', context=ctx)
