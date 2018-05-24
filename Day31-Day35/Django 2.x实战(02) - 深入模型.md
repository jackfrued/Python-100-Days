## Django 2.x实战(02) - 深入模型

在上一个章节中，我们提到了Django是一个基于MVC架构的Web框架，MVC架构要追求的是模型和视图的解耦合，而其中的模型说得更直白一些就是数据，所以通常也被称作数据模型。在实际的项目中，数据模型通常通过数据库实现持久化操作，而关系型数据库在很长一段时间都是持久化的首选方案，在我们的OA项目中，我们选择使用MySQL来实现数据持久化。

### 配置关系型数据库MySQL 

1. 进入oa文件夹，修改项目的settings.py文件，首先将我们之前创建的应用hrs添加已安装的项目中，然后配置MySQL作为持久化方案。

   ```Shell
   (venv)$ cd oa
   (venv)$ vim settings.py
   ```

   ```Python
   # 此处省略上面的代码
   
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'hrs',
   ]
   
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'oa',
           'HOST': 'localhost',
           'PORT': 3306,
           'USER': 'root',
           'PASSWORD': '123456',
       }
   }
   
   # 此处省略下面的代码
   ```

   在配置ENGINE属性时，常用的可选值包括：

   - `'django.db.backends.sqlite3'`：SQLite嵌入式数据库
   - `'django.db.backends.postgresql'`：BSD许可证下发行的开源关系型数据库产品
   - `'django.db.backends.mysql'`：转手多次目前属于甲骨文公司的经济高效的数据库产品
   - `'django.db.backends.oracle'`：甲骨文公司的旗舰关系型数据库产品

   其他的配置可以参考官方文档中[数据库配置](https://docs.djangoproject.com/zh-hans/2.0/ref/databases/#third-party-notes)的部分。

   NAME属性代表数据库的名称，如果使用SQLite它对应着一个文件，在这种情况下NAME的属性值应该是一个绝对路径。如果使用其他关系型数据库，还要配置对应的USER、PASSWORD、HOST、PORT等属性。

2. 安装MySQL客户端工具，Python 3中使用PyMySQL，Python 2中用MySQLdb。

   ```Shell
   (venv)$ pip install pymysql
   ```

   如果使用Python 3需要修改**项目**的`__init__.py`文件并加入如下所示的代码，这段代码的作用是将PyMySQL视为MySQLdb来使用，从而避免Django找不到连接MySQL的客户端工具而询问你：“Did you install mysqlclient? ”（你安装了mysqlclient吗？）。

   ```Python
   import pymysql
   
   pymysql.install_as_MySQLdb()
   ```

3. 运行manage.py并指定migrate参数实现数据库迁移，为应用程序创建对应的数据表，当然在此之前需要先启动MySQL数据库服务器并创建名为oa的数据库，在MySQL中创建数据库的语句如下所示。

   ```SQL
   drop database if exists oa;
   create database oa default charset utf8;
   ```

   ```Shell
   (venv)$ cd ..
   (venv)$ python manage.py migrate
   Operations to perform:
     Apply all migrations: admin, auth, contenttypes, sessions
   Running migrations:
     Applying contenttypes.0001_initial... OK
     Applying auth.0001_initial... OK
     Applying admin.0001_initial... OK
     Applying admin.0002_logentry_remove_auto_add... OK
     Applying contenttypes.0002_remove_content_type_name... OK
     Applying auth.0002_alter_permission_name_max_length... OK
     Applying auth.0003_alter_user_email_max_length... OK
     Applying auth.0004_alter_user_username_opts... OK
     Applying auth.0005_alter_user_last_login_null... OK
     Applying auth.0006_require_contenttypes_0002... OK
     Applying auth.0007_alter_validators_add_error_messages... OK
     Applying auth.0008_alter_user_username_max_length... OK
     Applying auth.0009_alter_user_last_name_max_length... OK
     Applying sessions.0001_initial... OK
   ```

4. 可以看到，Django帮助我们创建了10张二维表，这些都是使用Django框架需要的东西，除了这些之外，我们还应该为我们自己的应用创建数据模型。如果要在hrs应用中实现对部门和员工的管理，我们可以创建如下所示的数据模型。

   ```Shell
   (venv)$ cd hrs
   (venv)$ vim models.py
   ```

   ```Python
   from django.db import models
   
   
   class Dept(models.Model):
       """部门类"""
       
       no = models.IntegerField(primary_key=True, db_column='dno', verbose_name='部门编号')
       name = models.CharField(max_length=20, db_column='dname', verbose_name='部门名称')
       location = models.CharField(max_length=10, db_column='dloc', verbose_name='部门所在地')
   
       class Meta:
           db_table = 'tb_dept'
   
   
   class Emp(models.Model):
       """员工类"""
       
       no = models.IntegerField(primary_key=True, db_column='eno', verbose_name='员工编号')
       name = models.CharField(max_length=20, db_column='ename', verbose_name='员工姓名')
       job = models.CharField(max_length=10, verbose_name='职位')
       mgr = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='主管编号')
       sal = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='月薪')
       comm = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='补贴')
       dept = models.ForeignKey(Dept, db_column='dno', on_delete=models.PROTECT, verbose_name='所在部门')
   
       class Meta:
           db_table = 'tb_emp'
   
   
   ```
   > 说明：上面定义模型时使用了字段类及其属性，其中IntegerField对应数据库中的integer类型，CharField对应数据库的varchar类型，DecimalField对应数据库的decimal类型，ForeignKey用来建立多对一外键关联。字段属性primary_key用于设置主键，max_length用来设置字段的最大长度，db_column用来设置数据库中与字段对应的列，verbose_name则设置了Django后台管理系统中该字段显示的名称。如果对这些东西感到很困惑也不要紧，文末提供了字段类、字段属性、元数据选项等设置的相关说明，不清楚的读者可以稍后查看对应的参考指南。

5. 通过模型创建数据表。

   ```Shell
   (venv)$ cd ..
   (venv)$ python manage.py makemigrations hrs
   Migrations for 'hrs':
     hrs/migrations/0001_initial.py
       - Create model Dept
       - Create model Emp
   (venv)$ python manage.py migrate
   Operations to perform:
     Apply all migrations: admin, auth, contenttypes, hrs, sessions
   Running migrations:
     Applying hrs.0001_initial... OK
   ```

   执行完数据迁移操作之后，可以在通过图形化的MySQL客户端工具查看到E-R图（实体关系图）。

   ![](./res/er-graph.png)

### 在后台管理模型

1. 创建超级管理员账号。
2. 登录后台管理系统。
3. 注册模型类。
4. 对模型进行CRUD操作。
5. 注册模型管理类。

### 使用ORM完成模型的CRUD操作

#### 新增



#### 删除



#### 更新



#### 查询



最后，我们通过上面掌握的知识来实现部门展示以及根据部门获取部门对应员工信息的功能，效果如下图所示，对应的代码可以访问<https://github.com/jackfrued/Python-100-Days/tree/master/Day31-Day35/oa>。

### Django模型最佳实践

1. 正确的模型命名和关系字段命名。
2. 设置适当的related_name属性。
3. 用OneToOneField代替ForeignKeyField(unique=True)。
4. 通过迁移操作来添加模型。
5. 用NoSQL来应对需要降低范式级别的场景。
6. 如果布尔类型可以为空要使用NullBooleanField。
7. 在模型中放置业务逻辑。
8. 用ModelName.DoesNotExists取代ObjectDoesNotExists。
9. 在数据库中不要出现无效数据。
10. 不要对QuerySet调用len函数。
11. 将QuerySet的exists()方法的返回值用于if条件。
12. 用DecimalField来存储货币相关数据而不是FloatField。
13. 定义\_\_str\_\_方法。
14. 不要将数据文件放在同一个目录中。

> 说明：以上内容来自于STEELKIWI网站的[*Best Practice working with Django models in Python*](https://steelkiwi.com/blog/best-practices-working-django-models-python/)，有兴趣的小伙伴可以阅读原文。

### 模型定义参考

#### 字段

对字段名称的限制

- 字段名不能是Python的保留字，否则会导致语法错误
- 字段名不能有多个连续下划线，否则影响ORM查询操作

Django模型字段类

| 字段类                |  说明                                                         |
| --------------------- | ------------------------------------------------------------ |
| AutoField             |自增ID字段                                                   |
| BigIntegerField       |64位有符号整数                                               |
| BinaryField           | 存储二进制数据的字段，对应Python的bytes类型                  |
| BooleanField          | 存储True或False                                              |
| CharField             | 长度较小的字符串                                             |
| DateField             | 存储日期，有auto_now和auto_now_add属性                       |
| DateTimeField         | 存储日期和日期，两个附加属性同上                             |
| DecimalField          |存储固定精度小数，有max_digits（有效位数）和decimal_places（小数点后面）两个必要的参数 |
| DurationField         |存储时间跨度                                                 |
| EmailField            | 与CharField相同，可以用EmailValidator验证                    |
| FileField             | 文件上传字段                                                 |
| FloatField            | 存储浮点数                                                   |
| ImageField            | 其他同FileFiled，要验证上传的是不是有效图像                  |
| IntegerField          | 存储32位有符号整数。                                         |
| GenericIPAddressField | 存储IPv4或IPv6地址                                           |
| NullBooleanField      | 存储True、False或null值                                      |
| PositiveIntegerField  | 存储无符号整数（只能存储正数）                               |
| SlugField             | 存储slug（简短标注）                                         |
| SmallIntegerField     | 存储16位有符号整数                                           |
| TextField             | 存储数据量较大的文本                                         |
| TimeField             | 存储时间                                                     |
| URLField              | 存储URL的CharField                                           |
| UUIDField             | 存储全局唯一标识符                                           |

#### 字段属性

通用字段属性

| 选项           | 说明                                                         |
| -------------- | ------------------------------------------------------------ |
| null           | 数据库中对应的字段是否允许为NULL，默认为False                |
| blank          | 后台模型管理验证数据时，是否允许为NULL，默认为False          |
| choices        | 设定字段的选项，各元组中的第一个值是设置在模型上的值，第二值是人类可读的值 |
| db_column      | 字段对应到数据库表中的列名，未指定时直接使用字段的名称       |
| db_index       | 设置为True时将在该字段创建索引                               |
| db_tablespace  | 为有索引的字段设置使用的表空间，默认为DEFAULT_INDEX_TABLESPACE |
| default        | 字段的默认值                                                 |
| editable       | 字段在后台模型管理或ModelForm中是否显示，默认为True          |
| error_messages | 设定字段抛出异常时的默认消息的字典，其中的键包括null、blank、invalid、invalid_choice、unique和unique_for_date |
| help_text      | 表单小组件旁边显示的额外的帮助文本。                         |
| primary_key    | 将字段指定为模型的主键，未指定时会自动添加AutoField用于主键，只读。 |
| unique         | 设置为True时，表中字段的值必须是唯一的                       |
| verbose_name   | 字段在后台模型管理显示的名称，未指定时使用字段的名称         |

ForeignKey属性

1. limit_choices_to：值是一个Q对象或返回一个Q对象，用于限制后台显示哪些对象。
2. related_name：用于获取关联对象的关联管理器对象（反向查询），如果不允许反向，该属性应该被设置为`'+'`，或者以`'+'`结尾。
3. to_field：指定关联的字段，默认关联对象的主键字段。
4. db_constraint：是否为外键创建约束，默认值为True。
5. on_delete：外键关联的对象被删除时对应的动作，可取的值包括django.db.models中定义的：
   - CASCADE：级联删除。
   - PROTECT：抛出ProtectedError异常，阻止删除引用的对象。
   - SET_NULL：把外键设置为null，当null属性被设置为True时才能这么做。
   - SET_DEFAULT：把外键设置为默认值，提供了默认值才能这么做。

ManyToManyField属性

1. symmetrical：是否建立对称的多对多关系。
2. through：指定维持多对多关系的中间表的Django模型。
3. throughfields：定义了中间模型时可以指定建立多对多关系的字段。
4. db_table：指定维持多对多关系的中间表的表名。

#### 模型元数据选项

| 选项                  | 说明                                                         |
| --------------------- | ------------------------------------------------------------ |
| abstract              | 设置为True时模型是抽象父类                                   |
| app_label             | 如果定义模型的应用不在INSTALLED_APPS中可以用该属性指定       |
| db_table              | 模型使用的数据表名称                                         |
| db_tablespace         | 模型使用的数据表空间                                         |
| default_related_name  | 关联对象回指这个模型时默认使用的名称，默认为<model_name>_set |
| get_latest_by         | 模型中可排序字段的名称。                                     |
| managed               | 设置为True时，Django在迁移中创建数据表并在执行flush管理命令时把表移除 |
| order_with_respect_to | 标记对象为可排序的                                           |
| ordering              | 对象的默认排序                                               |
| permissions           | 创建对象时写入权限表的额外权限                               |
| default_permissions   | 默认为`('add', 'change', 'delete')`                          |
| unique_together       | 设定组合在一起时必须独一无二的字段名                         |
| index_together        | 设定一起建立索引的多个字段名                                 |
| verbose_name          | 为对象设定人类可读的名称                                     |
| verbose_name_plural   | 设定对象的复数名称                                           |

### 数据库API参考



按字段查找可以用的条件：

1. exact / iexact
2. contains / icontains
3. in
4. gt / gte / lt / lte
5. startswith / istartswith / endswith / iendswith
6. range
7. year / month / day / week_day / hour / minute / second
8. isnull
9. search
10. regex / iregex

跨关系查找

