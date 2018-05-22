from django.contrib import admin

from hrs.models import Dept, Emp


class DeptAdmin(admin.ModelAdmin):

    list_display = ('no', 'name', 'location')
    ordering = ('no', )


class EmpAdmin(admin.ModelAdmin):

    list_display = ('no', 'name', 'job', 'sal', 'dept')
    search_fields = ('name', 'job')
    ordering = ('dept', )


admin.site.register(Dept, DeptAdmin)
admin.site.register(Emp, EmpAdmin)
