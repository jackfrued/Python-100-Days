## Python程序接入MySQL数据库

在 Python3 中，我们可以使用`mysqlclient`或者`pymysql`三方库来接入 MySQL 数据库并实现数据持久化操作。二者的用法完全相同，只是导入的模块名不一样。我们推荐大家使用纯 Python 的三方库`pymysql`，因为它更容易安装成功。下面我们仍然以之前创建的名为`hrs`的数据库为例，为大家演示如何通过 Python 程序操作 MySQL 数据库实现数据持久化操作。

### 建库建表

```SQL
-- 创建名为hrs的数据库并指定默认的字符集
create database `hrs` default character set utf8mb4;

-- 切换到hrs数据库
use `hrs`;

-- 创建部门表
create table `tb_dept`
(
`dno` int not null comment '编号',
`dname` varchar(10) not null comment '名称',
`dloc` varchar(20) not null comment '所在地',
primary key (`dno`)
);

-- 插入4个部门
insert into `tb_dept` values 
    (10, '会计部', '北京'),
    (20, '研发部', '成都'),
    (30, '销售部', '重庆'),
    (40, '运维部', '深圳');

-- 创建员工表
create table `tb_emp`
(
`eno` int not null comment '员工编号',
`ename` varchar(20) not null comment '员工姓名',
`job` varchar(20) not null comment '员工职位',
`mgr` int comment '主管编号',
`sal` int not null comment '员工月薪',
`comm` int comment '每月补贴',
`dno` int not null comment '所在部门编号',
primary key (`eno`),
constraint `fk_emp_mgr` foreign key (`mgr`) references tb_emp (`eno`),
constraint `fk_emp_dno` foreign key (`dno`) references tb_dept (`dno`)
);

-- 插入14个员工
insert into `tb_emp` values 
    (7800, '张三丰', '总裁', null, 9000, 1200, 20),
    (2056, '乔峰', '分析师', 7800, 5000, 1500, 20),
    (3088, '李莫愁', '设计师', 2056, 3500, 800, 20),
    (3211, '张无忌', '程序员', 2056, 3200, null, 20),
    (3233, '丘处机', '程序员', 2056, 3400, null, 20),
    (3251, '张翠山', '程序员', 2056, 4000, null, 20),
    (5566, '宋远桥', '会计师', 7800, 4000, 1000, 10),
    (5234, '郭靖', '出纳', 5566, 2000, null, 10),
    (3344, '黄蓉', '销售主管', 7800, 3000, 800, 30),
    (1359, '胡一刀', '销售员', 3344, 1800, 200, 30),
    (4466, '苗人凤', '销售员', 3344, 2500, null, 30),
    (3244, '欧阳锋', '程序员', 3088, 3200, null, 20),
    (3577, '杨过', '会计', 5566, 2200, null, 10),
    (3588, '朱九真', '会计', 5566, 2500, null, 10);
```

### 接入MySQL

首先，我们可以在命令行或者 PyCharm 的终端中通过下面的命令安装`pymysql`，如果需要接入 MySQL 8，还需要安装一个名为`cryptography`的三方库来支持 MySQL 8 的密码认证方式。

```Shell
pip install pymysql cryptography
```

使用`pymysql`操作 MySQL 的步骤如下所示：

1. 创建连接。MySQL 服务器启动后，提供了基于 TCP （传输控制协议）的网络服务。我们可以通过`pymysql`模块的`connect`函数连接 MySQL 服务器。在调用`connect`函数时，需要指定主机（`host`）、端口（`port`）、用户名（`user`）、口令（`password`）、数据库（`database`）、字符集（`charset`）等参数，该函数会返回一个`Connection`对象。
2. 获取游标。连接 MySQL 服务器成功后，接下来要做的就是向数据库服务器发送 SQL 语句，MySQL 会执行接收到的 SQL 并将执行结果通过网络返回。要实现这项操作，需要先通过连接对象的`cursor`方法获取游标（`Cursor`）对象。
3. 发出 SQL。通过游标对象的`execute`方法，我们可以向数据库发出 SQL 语句。
4. 如果执行`insert`、`delete`或`update`操作，需要根据实际情况提交或回滚事务。因为创建连接时，默认开启了事务环境，在操作完成后，需要使用连接对象的`commit`或`rollback`方法，实现事务的提交或回滚，`rollback`方法通常会放在异常捕获代码块`except`中。如果执行`select`操作，需要通过游标对象抓取查询的结果，对应的方法有三个，分别是：`fetchone`、`fetchmany`和`fetchall`。其中`fetchone`方法会抓取到一条记录，并以元组或字典的方式返回；`fetchmany`和`fetchall`方法会抓取到多条记录，以嵌套元组或列表装字典的方式返回。
5. 关闭连接。在完成持久化操作后，请不要忘记关闭连接，释放外部资源。我们通常会在`finally`代码块中使用连接对象的`close`方法来关闭连接。

### 代码实操

下面，我们通过代码实操的方式为大家演示上面说的五个步骤。

#### 插入数据

```Python
import pymysql

no = int(input('部门编号: '))
name = input('部门名称: ')
location = input('部门所在地: ')

# 1. 创建连接（Connection）
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='guest', password='Guest.618',
                       database='hrs', charset='utf8mb4')
try:
    # 2. 获取游标对象（Cursor）
    with conn.cursor() as cursor:
        # 3. 通过游标对象向数据库服务器发出SQL语句
        affected_rows = cursor.execute(
            'insert into `tb_dept` values (%s, %s, %s)',
            (no, name, location)
        )
        if affected_rows == 1:
            print('新增部门成功!!!')
    # 4. 提交事务（transaction）
    conn.commit()
except pymysql.MySQLError as err:
    # 4. 回滚事务
    conn.rollback()
    print(type(err), err)
finally:
    # 5. 关闭连接释放资源
    conn.close()
```

> **说明**：上面的`127.0.0.1`称为回环地址，它代表的是本机。下面的`guest`是我提前创建好的用户，该用户拥有对`hrs`数据库的`insert`、`delete`、`update`和`select`权限。我们不建议大家在项目中直接使用`root`超级管理员账号访问数据库，这样做实在是太危险了。我们可以使用下面的命令创建名为`guest`的用户并为其授权。
>
> ```SQL
> create user 'guest'@'%' identified by 'Guest.618';
> grant insert, delete, update, select on `hrs`.* to 'guest'@'%';
> ```

如果要插入大量数据，建议使用游标对象的`executemany`方法做批处理（一个`insert`操作后面跟上多组数据），大家可以尝试向一张表插入10000条记录，然后看看不使用批处理一条条的插入和使用批处理有什么差别。游标对象的`executemany`方法第一个参数仍然是 SQL 语句，第二个参数可以是包含多组数据的列表或元组。

#### 删除数据

```Python
import pymysql

no = int(input('部门编号: '))

# 1. 创建连接（Connection）
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='guest', password='Guest.618',
                       database='hrs', charset='utf8mb4',
                       autocommit=True)
try:
    # 2. 获取游标对象（Cursor）
    with conn.cursor() as cursor:
        # 3. 通过游标对象向数据库服务器发出SQL语句
        affected_rows = cursor.execute(
            'delete from `tb_dept` where `dno`=%s',
            (no, )
        )
        if affected_rows == 1:
            print('删除部门成功!!!')
finally:
    # 5. 关闭连接释放资源
    conn.close()
```

> **说明**：如果不希望每次 SQL 操作之后手动提交或回滚事务，可以`connect`函数中加一个名为`autocommit`的参数并将它的值设置为`True`，表示每次执行 SQL 成功后自动提交。但是我们建议大家手动提交或回滚，这样可以根据实际业务需要来构造事务环境。如果不愿意捕获异常并进行处理，可以在`try`代码块后直接跟`finally`块，省略`except`意味着发生异常时，代码会直接崩溃并将异常栈显示在终端中。

#### 更新数据

```Python
import pymysql

no = int(input('部门编号: '))
name = input('部门名称: ')
location = input('部门所在地: ')

# 1. 创建连接（Connection）
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='guest', password='Guest.618',
                       database='hrs', charset='utf8mb4')
try:
    # 2. 获取游标对象（Cursor）
    with conn.cursor() as cursor:
        # 3. 通过游标对象向数据库服务器发出SQL语句
        affected_rows = cursor.execute(
            'update `tb_dept` set `dname`=%s, `dloc`=%s where `dno`=%s',
            (name, location, no)
        )
        if affected_rows == 1:
            print('更新部门信息成功!!!')
    # 4. 提交事务
    conn.commit()
except pymysql.MySQLError as err:
    # 4. 回滚事务
    conn.rollback()
    print(type(err), err)
finally:
    # 5. 关闭连接释放资源
    conn.close()
```

#### 查询数据

1. 查询部门表的数据。

```Python
import pymysql

# 1. 创建连接（Connection）
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='guest', password='Guest.618',
                       database='hrs', charset='utf8mb4')
try:
    # 2. 获取游标对象（Cursor）
    with conn.cursor() as cursor:
        # 3. 通过游标对象向数据库服务器发出SQL语句
        cursor.execute('select `dno`, `dname`, `dloc` from `tb_dept`')
        # 4. 通过游标对象抓取数据
        row = cursor.fetchone()
        while row:
            print(row)
            row = cursor.fetchone()
except pymysql.MySQLError as err:
    print(type(err), err)
finally:
    # 5. 关闭连接释放资源
    conn.close()
```
>**说明**：上面的代码中，我们通过构造一个`while`循环实现了逐行抓取查询结果的操作。这种方式特别适合查询结果有非常多行的场景。因为如果使用`fetchall`一次性将所有记录抓取到一个嵌套元组中，会造成非常大的内存开销，这在很多场景下并不是一个好主意。如果不愿意使用`while`循环，还可以考虑使用`iter`函数构造一个迭代器来逐行抓取数据，有兴趣的读者可以自行研究。

2. 分页查询员工表的数据。

```Python
import pymysql

page = int(input('页码: '))
size = int(input('大小: '))

# 1. 创建连接（Connection）
con = pymysql.connect(host='127.0.0.1', port=3306,
                      user='guest', password='Guest.618',
                      database='hrs', charset='utf8')
try:
    # 2. 获取游标对象（Cursor）
    with con.cursor(pymysql.cursors.DictCursor) as cursor:
        # 3. 通过游标对象向数据库服务器发出SQL语句
        cursor.execute(
            'select `eno`, `ename`, `job`, `sal` from `tb_emp` order by `sal` desc limit %s,%s',
            ((page - 1) * size, size)
        )
        # 4. 通过游标对象抓取数据
        for emp_dict in cursor.fetchall():
            print(emp_dict)
finally:
    # 5. 关闭连接释放资源
    con.close()
```

### 案例讲解

下面我们为大家讲解一个将数据库表数据导出到 Excel 文件的例子，我们需要先安装`openpyxl`三方库，命令如下所示。

```Bash
pip install openpyxl
```

接下来，我们通过下面的代码实现了将数据库`hrs`中所有员工的编号、姓名、职位、月薪、补贴和部门名称导出到一个 Excel 文件中。

```Python
import openpyxl
import pymysql

# 创建工作簿对象
workbook = openpyxl.Workbook()
# 获得默认的工作表
sheet = workbook.active
# 修改工作表的标题
sheet.title = '员工基本信息'
# 给工作表添加表头
sheet.append(('工号', '姓名', '职位', '月薪', '补贴', '部门'))
# 创建连接（Connection）
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='guest', password='Guest.618',
                       database='hrs', charset='utf8mb4')
try:
    # 获取游标对象（Cursor）
    with conn.cursor() as cursor:
        # 通过游标对象执行SQL语句
        cursor.execute(
            'select `eno`, `ename`, `job`, `sal`, coalesce(`comm`, 0), `dname` '
            'from `tb_emp` natural join `tb_dept`'
        )
        # 通过游标抓取数据
        row = cursor.fetchone()
        while row:
            # 将数据逐行写入工作表中
            sheet.append(row)
            row = cursor.fetchone()
    # 保存工作簿
    workbook.save('hrs.xlsx')
except pymysql.MySQLError as err:
    print(err)
finally:
    # 关闭连接释放资源
    conn.close()
```

大家可以参考上面的例子，试一试把 Excel 文件的数据导入到指定数据库的指定表中，看看是否可以成功。