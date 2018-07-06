from django.contrib import admin

from demo.models import Teacher, Subject, User


class UserAdmin(admin.ModelAdmin):
    list_display = ('no', 'username', 'email', 'counter')
    ordering = ('no', )


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'intro')
    ordering = ('no', )


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'intro', 'motto', 'subject', 'manager')
    search_fields = ('name', 'intro')
    ordering = ('no', )


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(User, UserAdmin)

