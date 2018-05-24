from json import JSONEncoder

from django import forms
from django.http import JsonResponse
from django.shortcuts import render

from search.models import CarRecord

# 序列化/串行化/腌咸菜 - 把对象按照某种方式处理成字节或者字符的序列
# 反序列化/反串行化 - 把字符或者字节的序列重新还原成对象
# Python实现序列化和反序列化的工具模块 - json / pickle / shelve
# return HttpResponse(json.dumps(obj), content_type='application/json')
# return JsonResponse(obj, encoder=, safe=False)
# from django.core.serializers import serialize
# return HttpResponse(serialize('json', obj), content_type='application/json; charset=utf-8')


class CarRecordEncoder(JSONEncoder):

    def default(self, o):
        del o.__dict__['_state']
        o.__dict__['date'] = o.happen_date
        return o.__dict__


def ajax_search(request):
    if request.method == 'GET':
        return render(request, 'search2.html')
    else:
        carno = request.POST['carno']
        record_list = list(CarRecord.objects.filter(carno__icontains=carno))
        # 第一个参数是要转换成JSON格式(序列化)的对象
        # encoder参数要指定完成自定义对象序列化的编码器(JSONEncoder的子类型)
        # safe参数的值如果为True那么传入的第一个参数只能是字典
        # return HttpResponse(json.dumps(record_list), content_type='application/json; charset=utf-8')
        return JsonResponse(record_list, encoder=CarRecordEncoder,
                            safe=False)


def search(request):
    # 请求行中的请求命令
    # print(request.method)
    # 请求行中的路径
    # print(request.path)
    # 请求头(以HTTP_打头的键是HTTP请求的请求头)
    # print(request.META)
    # 查询参数: http://host/path/resource?a=b&c=d
    # print(request.GET)
    # 表单参数
    # print(request.POST)
    if request.method == 'GET':
        ctx = {'show_result': False}
    else:
        carno = request.POST['carno']
        ctx = {
            'show_result': True,
            'record_list': list(CarRecord.objects.filter(carno__contains=carno))}
    return render(request, 'search.html', ctx)


class CarRecordForm(forms.Form):
    carno = forms.CharField(min_length=7, max_length=7, label='车牌号', error_messages={'carno': '请输入有效的车牌号'})
    reason = forms.CharField(max_length=50, label='违章原因')
    punish = forms.CharField(max_length=50, required=False, label='处罚方式')


def add(request):
    errors = []
    if request.method == 'GET':
        f = CarRecordForm()
    else:
        f = CarRecordForm(request.POST)
        if f.is_valid():
            CarRecord(**f.cleaned_data).save()
            f = CarRecordForm()
        else:
            errors = f.errors.values()
    return render(request, 'add.html', {'f': f, 'errors': errors})
