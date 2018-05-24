from django.db import models

# ORM - 对象关系映射
# 对象模型  <--->   关系模型
# 实体类    <--->   二维表
# 属性      <--->   列
# 对象      <--->   记录


class Dept(models.Model):
    no = models.IntegerField(primary_key=True, verbose_name='部门编号')
    name = models.CharField(max_length=20, verbose_name='部门名称')
    location = models.CharField(max_length=10, verbose_name='部门所在地')
    excellent = models.BooleanField(default=0, verbose_name='是否优秀')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_dept'


class Emp(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    job = models.CharField(max_length=10)
    mgr = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    # mgr = models.IntegerField(null=True, blank=True)
    sal = models.DecimalField(max_digits=7, decimal_places=2)
    comm = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    dept = models.ForeignKey(Dept, on_delete=models.PROTECT)

    class Meta:
        db_table = 'tb_emp'
