from django.shortcuts import render

from cart.models import Goods


def index(request):
    goods_list = list(Goods.objects.all())
    return render(request, 'goods.html', {'goods_list': goods_list})


def show_cart(request):
    return render(request, 'cart.html')


def add_to_cart(request, no):
    pass
