from datetime import datetime
from json import JSONEncoder

from django import forms
from django.http import JsonResponse
from django.shortcuts import render, redirect

from search.models import CarRecord

# 序列化/串行化/腌咸菜 - 把对象按照某种方式处理成字节或者字符的序列
# 反序列化/反串行化 - 把字符或者字节的序列重新还原成对象
# Python实现序列化和反序列化的工具模块 - json / pickle / shelve
# return HttpResponse(json.dumps(obj), content_type='application/json')
# return JsonResponse(obj, encoder=, safe=False)
# from django.core.serializers import serialize
# return HttpResponse(serialize('json', obj), content_type='application/json; charset=utf-8')
MAX_AGE = 14 * 24 * 60 * 60


class CarRecordEncoder(JSONEncoder):

    def default(self, o):
        del o.__dict__['_state']
        o.__dict__['date'] = o.happen_date
        return o.__dict__


def ajax_search(request):
    current_time = datetime.now().ctime()
    # Cookie是保存在浏览器临时文件中的用户数据(通常是识别用户身份的ID/token或者是用户的偏好设置)
    # 因为每次请求服务器时在HTTP请求的请求头中都会携带本网站的Cookie数据
    # 那么服务器就可以获取这些信息来识别用户身份或者了解用户的偏好 这就是所谓的用户跟踪
    # 因为HTTP本身是无状态的 所以需要使用Cookie/隐藏域/URL重写这样的技术来实现用户跟踪
    # 从请求中读取指定的cookie - 通过cookie的名字找到对应的值
    # 如果请求中没有指定名字的cookie可以通过get方法的第二个参数设置一个默认的返回值
    last_visit_time = request.COOKIES.get('last_visit_time')
    if request.method == 'GET':
        response = render(request, 'search2.html',
                          {'last': last_visit_time if last_visit_time
                           else '你是第一次访问我们的网站'})
        # 通过render渲染页面后先用set_cookie方法设置cookie后再返回HttpResponse对象
        # 第一个参数是cookie的名字 第二个参数是cookie的值 第三个参数是过期时间(秒)
        response.set_cookie('last_visit_time', current_time, max_age=MAX_AGE)
        return response
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


class CarRecordForm(forms.ModelForm):
    carno = forms.CharField(min_length=7, max_length=7, label='车牌号', error_messages={'carno': '请输入有效的车牌号'})
    reason = forms.CharField(max_length=50, label='违章原因')
    punish = forms.CharField(max_length=50, required=False, label='处罚方式')

    """
    # 执行额外的表单数据验证
    def clean_carno(self):
        _carno = self.cleaned_data['carno']
        if not condition:
            raise forms.ValidationError('...')
        return _carno
    """

    class Meta:
        model = CarRecord
        fields = ('carno', 'reason', 'punish')


def add(request):
    if request.method == 'GET':
        f = CarRecordForm(initial={'reason': '打警察', 'punish': '牢底坐穿'})
    else:
        f = CarRecordForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/search2')
    return render(request, 'add.html', {'f': f})
