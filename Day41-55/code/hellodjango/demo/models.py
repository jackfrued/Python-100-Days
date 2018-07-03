from django.db import models

# Django框架中包含了ORM(对象关系映射)框架
# ORM可以帮助我们完成对象模型到关系模型的双向转换


class Teacher(models.Model):
    no = models.AutoField(primary_key=True, db_column='tno', verbose_name='编号')
    name = models.CharField(max_length=20, db_column='tname', verbose_name='姓名')
    job = models.CharField(max_length=10, db_column='tjob', verbose_name='职位')
    intro = models.CharField(max_length=1023, db_column='tintro', verbose_name='简介')
    motto = models.CharField(max_length=255, db_column='tmotto', verbose_name='教学理念')
    photo = models.CharField(max_length=511, db_column='tphoto', null=True)

    class Meta(object):
        db_table = 'tb_teacher'
        ordering = ('-no', )
