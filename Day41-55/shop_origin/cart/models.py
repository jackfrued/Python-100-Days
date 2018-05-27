from django.db import models


class Goods(models.Model):

    id = models.AutoField(primary_key=True, db_column='gid')
    name = models.CharField(max_length=50, db_column='gname')
    price = models.DecimalField(max_digits=10, decimal_places=2, db_column='gprice')
    image = models.CharField(max_length=255, db_column='gimage')

    class Meta:
        db_table = 'tb_goods'
        ordering = ('id',)
