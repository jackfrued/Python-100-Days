from django.contrib import admin

from cart.models import Goods


class GoodsAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'price', 'image')


admin.site.register(Goods, GoodsAdmin)
