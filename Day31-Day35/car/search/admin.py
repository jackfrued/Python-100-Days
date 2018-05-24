from django.contrib import admin

from search.models import CarRecord


class CarRecordAdmin(admin.ModelAdmin):

    list_display = ('carno', 'reason', 'date', 'punish', 'isdone')
    search_fields = ('carno', )


admin.site.register(CarRecord, CarRecordAdmin)
