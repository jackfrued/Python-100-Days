from django.contrib import admin

from demo.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'job', 'intro', 'motto')
    search_fields = ('name', 'intro')
    ordering = ('no', )


admin.site.register(Teacher, TeacherAdmin)
