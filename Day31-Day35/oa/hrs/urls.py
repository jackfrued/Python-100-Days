from django.urls import path

from hrs import views

urlpatterns = [
    path('depts', views.depts, name='depts'),
    # url('depts/emps/(?P<no>[0-9]+)', views.emps, name='empsindept'),
    path('depts/emps/<int:no>', views.emps, name='empsindept'),
    path('deldept/<int:no>', views.del_dept, name='ddel')
]
