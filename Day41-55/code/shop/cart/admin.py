from django.contrib import admin

from cart.models import Goods


class GoodsAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'price', 'image')
    search_fields = ('name', )


admin.site.register(Goods, GoodsAdmin)
