from django.urls import path

from hrs import views

urlpatterns = [
    path('depts', views.depts, name='depts'),
    path('depts/emps', views.emps, name='empsindept'),
    path('deldepts', views.del_dept, name='ddel')
]
