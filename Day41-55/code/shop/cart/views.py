from django.core import serializers
from django.shortcuts import render, redirect

from cart.models import Goods


def index(request):
    goods_list = list(Goods.objects.all())
    return render(request, 'goods.html', {'goods_list': goods_list})


class CartItem(object):
    """购物车中的商品项"""

    def __init__(self, goods, amount=1):
        self.goods = goods
        self.amount = amount

    @property
    def total(self):
        return self.goods.price * self.amount


class ShoppingCart(object):
    """购物车"""

    def __init__(self):
        self.items = {}
        self.index = 0

    def add_item(self, item):
        if item.goods.id in self.items:
            self.items[item.goods.id].amount += item.amount
        else:
            self.items[item.goods.id] = item

    def remove_item(self, id):
        if id in self.items:
            self.items.remove(id)

    def clear_all_items(self):
        self.items.clear()

    @property
    def cart_items(self):
        return self.items.values()

    @property
    def total(self):
        val = 0
        for item in self.items.values():
            val += item.total
        return val


def add_to_cart(request, id):
    goods = Goods.objects.get(pk=id)
    # 通过request对象的session属性可以获取到session
    # session相当于是服务器端用来保存用户数据的一个字典
    # session利用了Cookie保存sessionid
    # 通过sessionid就可以获取与某个用户对应的会话(也就是用户数据)
    # 如果在浏览器中清除了Cookie那么也就清除了sessionid
    # 再次访问服务器时服务器会重新分配新的sessionid这也就意味着之前的用户数据无法找回
    # 默认情况下Django的session被设定为持久会话而非浏览器续存期会话
    # 通过SESSION_EXPIRE_AT_BROWSER_CLOSE和SESSION_COOKIE_AGE参数可以修改默认设定
    # Django中的session是进行了持久化处理的因此需要设定session的序列化方式
    # 1.6版开始Django默认的session序列化器是JsonSerializer
    # 可以通过SESSION_SERIALIZER来设定其他的序列化器(例如PickleSerializer)
    cart = request.session.get('cart', ShoppingCart())
    cart.add_item(CartItem(goods))
    request.session['cart'] = cart
    return redirect('/')


def show_cart(request):
    cart = serializers.deserialize(request.session.get('cart'))
    return render(request, 'cart.html', {'cart': cart})
