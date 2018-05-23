from django.shortcuts import render, redirect
from django.urls import reverse

from hrs.models import Dept, Emp


def index(request):
    ctx = {
        'greeting': '你好，世界！'
    }
    return render(request, 'index.html', context=ctx)


def del_dept(request):
    # 重定向 - 重新请求一个指定的页面
    return redirect(reverse('depts'))


def emps(request):
    no = request.GET['no']
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
