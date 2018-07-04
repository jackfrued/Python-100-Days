from django.contrib import admin

from demo.models import Teacher, Subject


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'intro')
    ordering = ('no', )


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'intro', 'motto', 'subject', 'manager')
    search_fields = ('name', 'intro')
    ordering = ('no', )


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)

