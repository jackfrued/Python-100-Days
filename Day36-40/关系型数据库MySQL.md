## 关系数据库入门

### 关系数据库概述

1. 数据持久化 - 将数据保存到（在掉电情况下）能够长久保存数据的存储介质中。

2. 数据库发展史 - 网状数据库、层次数据库、关系数据库、NoSQL数据库。

   > 1970年，IBM的研究员E.F.Codd在*Communication of the ACM*上发表了名为*A Relational Model of Data for Large Shared Data Banks*的论文，提出了关系模型的概念，奠定了关系模型的理论基础。后来Codd又陆续发表多篇文章，论述了范式理论和衡量关系系统的12条标准，用数学理论奠定了关系数据库的基础。

3. 关系数据库特点。

   - 理论基础：集合论和关系代数。

   - 具体表象：用二维表（有行和列）组织数据。

   - 编程语言：结构化查询语言（SQL）。

4. E-R图。
   - 实体 - 矩形框
   - 属性 - 椭圆框
   - 关系 - 菱形框
   - 重数 - 1:1 / 1:N / M:N

5. 关系数据库产品。
   - [Oracle](https://www.oracle.com/index.html) - 目前世界上使用最为广泛的数据库管理系统，作为一个通用的数据库系统，它具有完整的数据管理功能；作为一个关系数据库，它是一个完备关系的产品；作为分布式数据库，它实现了分布式处理的功能。在Oracle最新的12c版本中，还引入了多承租方架构，使用该架构可轻松部署和管理数据库云。
   - [DB2](https://www.ibm.com/analytics/us/en/db2/) - IBM公司开发的、主要运行于Unix（包括IBM自家的[AIX](https://zh.wikipedia.org/wiki/AIX)）、Linux、以及Windows服务器版等系统的关系数据库产品。DB2历史悠久且被认为是最早使用SQL的数据库产品，它拥有较为强大的商业智能功能。
   - [SQL Server](https://www.microsoft.com/en-us/sql-server/) - 由Microsoft开发和推广的关系型数据库产品，最初适用于中小企业的数据管理，但是近年来它的应用范围有所扩展，部分大企业甚至是跨国公司也开始基于它来构建自己的数据管理系统。
   - [MySQL](https://www.mysql.com/) - MySQL是开放源代码的，任何人都可以在GPL（General Public License）的许可下下载并根据个性化的需要对其进行修改。MySQL因为其速度、可靠性和适应性而备受关注。
   - [PostgreSQL]() - 在BSD许可证下发行的开放源代码的关系数据库产品。

### MySQL简介

1. 安装和配置（以CentOS Linux环境为例）。

   - Linux下有一个MySQL的分支版本，名为MariaDB，它由MySQL的一些原始开发者开发，有商业支持，旨在继续保持MySQL数据库在[GNU GPL](https://zh.wikipedia.org/wiki/GNU%E9%80%9A%E7%94%A8%E5%85%AC%E5%85%B1%E8%AE%B8%E5%8F%AF%E8%AF%81)下开源（因为大家担心MySQL被甲骨文收购后会不再开源）。如果决定要直接使用MariaDB作为MySQL的替代品，可以使用下面的命令进行安装。

     ```Shell
     yum install mariadb mariadb-server
     ```

   - 如果要安装官方版本的MySQL，可以在[MySQL官方网站](<https://www.mysql.com/>)下载安装文件。首先在下载页面中选择平台和版本，然后找到对应的下载链接。下面以MySQL 5.7.26版本和Red Hat Enterprise Linux为例，直接下载包含所有安装文件的归档文件，解归档之后通过包管理工具进行安装。

     ```Shell
     wget https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.26-1.el7.x86_64.rpm-bundle.tar
     tar -xvf mysql-5.7.26-1.el7.x86_64.rpm-bundle.tar
     ```

     如果系统上有MariaDB相关的文件，需要先移除MariaDB相关的文件。

     ```Shell
     yum list installed | grep mariadb | awk '{print $1}' | xargs yum erase -y
     ```

     接下来可以按照如下所示的顺序用RPM（Redhat Package Manager）工具安装MySQL。

     ```Shell
     rpm -ivh mysql-community-common-5.7.26-1.el7.x86_64.rpm
     rpm -ivh mysql-community-libs-5.7.26-1.el7.x86_64.rpm
     rpm -ivh mysql-community-client-5.7.26-1.el7.x86_64.rpm
     rpm -ivh mysql-community-server-5.7.26-1.el7.x86_64.rpm
     ```

     可以使用下面的命令查看已经安装的MySQL相关的包。

     ```Shell
     rpm -qa | grep mysql
     ```

   - 启动MySQL服务。

     先修改MySQL的配置文件（`/etc/my.cnf`）添加一行`skip-grant-tables`，可以设置不进行身份验证即可连接MySQL服务器，然后就可以以超级管理员（root）身份登录。

     ```Shell
     vim /etc/my.cnf
     ```

     ```INI
     [mysqld]
     skip-grant-tables
     
     datadir=/var/lib/mysql
     socket=/var/lib/mysql/mysql.sock
     
     symbolic-links=0
     
     log-error=/var/log/mysqld.log
     pid-file=/var/run/mysqld/mysqld.pid
     ```

     接下来可以使用下面的命令来启动MySQL。

     ```Shell
     service mysqld start
     ```

     在CentOS 7中建议使用下面的命令来启动MySQL。

     ```Shell
     systemctl start mysqld
     ```

   - 使用MySQL客户端工具连接服务器。

     命令行工具：

     ```Shell
     mysql -u root
     ```

     修改超级管理员（root）的访问口令为i_LOVE_macos_123。

     ```SQL
     use mysql;
     update user set authentication_string=password('i_LOVE_macos_123') where user='root';
     flush privileges;
     ```

     将MySQL配置文件中的`skip-grant-tables`去掉，然后重启服务器，重新登录。这一次需要提供用户名和口令才能连接MySQL服务器。

     ```Shell
     systemctl restart mysqld
     mysql -u root -p
     ```

     也可以选择图形化的客户端工具来连接MySQL服务器，可以选择下列工具之一：

     - MySQL Workbench（官方提供的工具）
     - Navicat for MySQL（界面简单优雅，功能直观强大）
     - SQLyog for MySQL（强大的MySQL数据库管理员工具）

2. 常用命令。

   - 查看服务器版本。

     ```SQL
     select version();
     ```

   - 查看所有数据库。

     ```SQL
     show databases;
     ```

   - 切换到指定数据库。

     ```SQL
     use mysql;
     ```

   - 查看数据库下所有表。

     ```Shell
     show tables;
     ```

   - 获取帮助。

     ```SQL
     ? contents;
     ? functions;
     ? numeric functions;
     ? round;
     
     ? data types;
     ? longblob;
     ```


### SQL详解

1. DDL

   ```SQL
   -- 如果存在名为school的数据库就删除它
   drop database if exists school;
   
   -- 创建名为school的数据库并设置默认的字符集和排序方式
   create database school default charset utf8 collate utf8_bin;
   
   -- 切换到school数据库上下文环境
   use school;
   
   -- 创建学院表
   create table tb_college
   (
   collid int not null auto_increment comment '编号',
   collname varchar(50) not null comment '名称',
   collmaster varchar(20) not null comment '院长',
   collweb varchar(511) default '' comment '网站',
   primary key (collid)
   );
   
   -- 创建学生表
   create table tb_student
   (
   stuid int not null comment '学号',
   stuname varchar(20) not null comment '姓名',
   stusex bit default 1 comment '性别',
   stubirth date not null comment '出生日期',
   stuaddr varchar(255) default '' comment '籍贯',
   collid int not null comment '所属学院',
   primary key (stuid),
   foreign key (collid) references tb_college (collid)
   );
   
   -- alter table tb_student add constraint fk_student_collid foreign key (collid) references tb_college (collid);
   
   -- 创建教师表
   create table tb_teacher
   (
   teaid int not null comment '工号',
   teaname varchar(20) not null comment '姓名',
   teatitle varchar(10) default '助教' comment '职称',
   collid int not null comment '所属学院',
   primary key (teaid),
   foreign key (collid) references tb_college (collid)
   );
   
   -- 创建课程表
   create table tb_course
   (
   couid int not null comment '编号',
   couname varchar(50) not null comment '名称',
   coucredit int not null comment '学分',
   teaid int not null comment '授课老师',
   primary key (couid),
   foreign key (teaid) references tb_teacher (teaid)
   );
   
   -- 创建选课记录表
   create table tb_score
   (
   scid int auto_increment comment '选课记录编号',
   stuid int not null comment '选课学生',
   couid int not null comment '所选课程',
   scdate datetime comment '选课时间日期',
   scmark decimal(4,1) comment '考试成绩',
   primary key (scid),
   foreign key (stuid) references tb_student (stuid),
   foreign key (couid) references tb_course (couid)
   );
   
   -- 添加唯一性约束（一个学生选某个课程只能选一次）
   alter table tb_score add constraint uni_score_stuid_couid unique (stuid, couid);
   ```

2. DML

   ```SQL
   
   -- 插入学院数据
   insert into tb_college (collname, collmaster, collweb) values 
   ('计算机学院', '左冷禅', 'http://www.abc.com'),
   ('外国语学院', '岳不群', 'http://www.xyz.com'),
   ('经济管理学院', '风清扬', 'http://www.foo.com');
   
   -- 插入学生数据
   insert into tb_student (stuid, stuname, stusex, stubirth, stuaddr, collid) values
   (1001, '杨逍', 1, '1990-3-4', '四川成都', 1),
   (1002, '任我行', 1, '1992-2-2', '湖南长沙', 1),
   (1033, '王语嫣', 0, '1989-12-3', '四川成都', 1),
   (1572, '岳不群', 1, '1993-7-19', '陕西咸阳', 1),
   (1378, '纪嫣然', 0, '1995-8-12', '四川绵阳', 1),
   (1954, '林平之', 1, '1994-9-20', '福建莆田', 1),
   (2035, '东方不败', 1, '1988-6-30', null, 2),
   (3011, '林震南', 1, '1985-12-12', '福建莆田', 3),
   (3755, '项少龙', 1, '1993-1-25', null, 3),
   (3923, '杨不悔', 0, '1985-4-17', '四川成都', 3),
   (4040, '隔壁老王', 1, '1989-1-1', '四川成都', 2);
   
   -- 删除学生数据
   delete from tb_student where stuid=4040;
   
   -- 更新学生数据
   update tb_student set stuname='杨过', stuaddr='湖南长沙' where stuid=1001;
   
   -- 插入老师数据
   insert into tb_teacher (teaid, teaname, teatitle, collid) values 
   (1122, '张三丰', '教授', 1),
   (1133, '宋远桥', '副教授', 1),
   (1144, '杨逍', '副教授', 1),
   (2255, '范遥', '副教授', 2),
   (3366, '韦一笑', '讲师', 3);
   
   -- 插入课程数据
   insert into tb_course (couid, couname, coucredit, teaid) values 
   (1111, 'Python程序设计', 3, 1122),
   (2222, 'Web前端开发', 2, 1122),
   (3333, '操作系统', 4, 1122),
   (4444, '计算机网络', 2, 1133),
   (5555, '编译原理', 4, 1144),
   (6666, '算法和数据结构', 3, 1144),
   (7777, '经贸法语', 3, 2255),
   (8888, '成本会计', 2, 3366),
   (9999, '审计学', 3, 3366);
   
   -- 插入选课数据
   insert into tb_score (stuid, couid, scdate, scmark) values 
   (1001, 1111, '2017-09-01', 95),
   (1001, 2222, '2017-09-01', 87.5),
   (1001, 3333, '2017-09-01', 100),
   (1001, 4444, '2018-09-03', null),
   (1001, 6666, '2017-09-02', 100),
   (1002, 1111, '2017-09-03', 65),
   (1002, 5555, '2017-09-01', 42),
   (1033, 1111, '2017-09-03', 92.5),
   (1033, 4444, '2017-09-01', 78),
   (1033, 5555, '2017-09-01', 82.5),
   (1572, 1111, '2017-09-02', 78),
   (1378, 1111, '2017-09-05', 82),
   (1378, 7777, '2017-09-02', 65.5),
   (2035, 7777, '2018-09-03', 88),
   (2035, 9999, curdate(), null),
   (3755, 1111, date(now()), null),
   (3755, 8888, date(now()), null),
   (3755, 9999, '2017-09-01', 92);
   ```

3. DQL

   ```SQL
   -- 查询所有学生信息
   select * from tb_student;
   
   -- 查询所有课程名称及学分(投影和别名)
   select couname, coucredit from tb_course;
   select couname as 课程名称, coucredit as 学分 from tb_course;
   
   -- 查询所有学生的姓名和性别(条件运算)
   select stuname as 姓名, case stusex when 1 then '男' else '女' end as 性别 from tb_student;
   select stuname as 姓名, if(stusex, '男', '女') as 性别 from tb_student;
   
   -- 查询所有女学生的姓名和出生日期(筛选)
   select stuname, stubirth from tb_student where stusex=0;
   
   -- 查询所有80后学生的姓名、性别和出生日期(筛选)
   select stuname, stusex, stubirth from tb_student where stubirth>='1980-1-1' and stubirth<='1989-12-31';
   select stuname, stusex, stubirth from tb_student where stubirth between '1980-1-1' and '1989-12-31';
   
   -- 查询姓"杨"的学生姓名和性别(模糊)
   select stuname, stusex from tb_student where stuname like '杨%';
   
   -- 查询姓"杨"名字两个字的学生姓名和性别(模糊)
   select stuname, stusex from tb_student where stuname like '杨_';
   
   -- 查询姓"杨"名字三个字的学生姓名和性别(模糊)
   select stuname, stusex from tb_student where stuname like '杨__';
   
   -- 查询名字中有"不"字或"嫣"字的学生的姓名(模糊)
   select stuname, stusex from tb_student where stuname like '%不%' or stuname like '%嫣%';
   
   -- 查询没有录入家庭住址的学生姓名(空值)
   select stuname from tb_student where stuaddr is null;
   
   -- 查询录入了家庭住址的学生姓名(空值)
   select stuname from tb_student where stuaddr is not null;
   
   -- 查询学生选课的所有日期(去重)
   select distinct scdate from tb_score;
   
   -- 查询学生的家庭住址(去重)
   select distinct stuaddr from tb_student where stuaddr is not null;
   
   -- 查询男学生的姓名和生日按年龄从大到小排列(排序)
   -- asc (ascending) - 升序（从小到大）/ desc (descending) - 降序（从大到小）
   select stuname as 姓名, year(now())-year(stubirth) as 年龄 from tb_student where stusex=1 order by 年龄 desc;
   
   -- 聚合函数：max / min / count / sum / avg
   -- 查询年龄最大的学生的出生日期(聚合函数)
   select min(stubirth) from tb_student;
   
   -- 查询年龄最小的学生的出生日期(聚合函数)
   select max(stubirth) from tb_student;
   
   -- 查询男女学生的人数(分组和聚合函数)
   select stusex, count(*) from tb_student group by stusex;
   
   -- 查询课程编号为1111的课程的平均成绩(筛选和聚合函数)
   select avg(scmark) from tb_score where couid=1111;
   
   -- 查询学号为1001的学生所有课程的平均分(筛选和聚合函数)
   select avg(scmark) from tb_score where stuid=1001;
   
   -- 查询每个学生的学号和平均成绩(分组和聚合函数)
   select stuid as 学号, avg(scmark) as 平均分 from tb_score group by stuid;
   
   -- 查询平均成绩大于等于90分的学生的学号和平均成绩
   -- 分组以前的筛选使用where子句 / 分组以后的筛选使用having子句
   select stuid as 学号, avg(scmark) as 平均分 from tb_score group by stuid having 平均分>=90;
   
   -- 查询年龄最大的学生的姓名(子查询/嵌套的查询)
   select stuname from tb_student where stubirth=(
   	select min(stubirth) from tb_student
   );
   
   -- 查询年龄最大的学生姓名和年龄(子查询+运算)
   select stuname as 姓名, year(now())-year(stubirth) as 年龄 from tb_student where stubirth=(
   	select min(stubirth) from tb_student
   );
   
   -- 查询选了两门以上的课程的学生姓名(子查询/分组条件/集合运算)
   select stuname from tb_student where stuid in (
   	select stuid from tb_score group by stuid having count(stuid)>2
   )
   
   -- 查询学生姓名、课程名称以及成绩(连接查询)
   select stuname, couname, scmark from tb_student t1, tb_course t2, tb_score t3 where t1.stuid=t3.stuid and t2.couid=t3.couid and scmark is not null;
   
   -- 查询学生姓名、课程名称以及成绩按成绩从高到低查询第11-15条记录(内连接+分页)
   select stuname, couname, scmark from tb_student t1 inner join tb_score t3 on t1.stuid=t3.stuid inner join tb_course t2 on t2.couid=t3.couid where scmark is not null order by scmark desc limit 5 offset 10;
   
   select stuname, couname, scmark from tb_student t1 inner join tb_score t3 on t1.stuid=t3.stuid inner join tb_course t2 on t2.couid=t3.couid where scmark is not null order by scmark desc limit 10, 5;
   
   -- 查询选课学生的姓名和平均成绩(子查询和连接查询)
   select stuname, avgmark from tb_student t1, (select stuid, avg(scmark) as avgmark from tb_score group by stuid) t2 where t1.stuid=t2.stuid;
   
   select stuname, avgmark from tb_student t1 inner join 
   (select stuid, avg(scmark) as avgmark from tb_score group by stuid) t2 on t1.stuid=t2.stuid;
   
   -- 内连接（inner join）- 只有满足连接条件的记录才会被查出来
   -- 外连接（outer join）- 左外连接(left outer join) / 右外连接(right outer join) / 全外连接
   -- 查询每个学生的姓名和选课数量(左外连接和子查询)
   select stuname, ifnull(total, 0) from tb_student t1 left outer join (select stuid, count(stuid) as total from tb_score group by stuid) t2 on t1.stuid=t2.stuid;
   ```

4. DCL

   ```SQL
   -- 创建名为hellokitty的用户
   create user 'hellokitty'@'%' identified by '123123';
   
   -- 将对school数据库所有对象的所有操作权限授予hellokitty
   grant all privileges on school.* to 'hellokitty'@'%';
   
   -- 召回hellokitty对school数据库所有对象的insert/delete/update权限
   revoke insert, delete, update on school.* from 'hellokitty'@'%';
   ```

###  相关知识

#### 范式理论 - 设计二维表的指导思想

1. 第一范式：数据表的每个列的值域都是由原子值组成的，不能够再分割。
2. 第二范式：数据表里的所有数据都要和该数据表的键（主键与候选键）有完全依赖关系。
3. 第三范式：所有非键属性都只和候选键有相关性，也就是说非键属性之间应该是独立无关的。

#### 数据完整性

1. 实体完整性 - 每个实体都是独一无二的
   - 主键（primary key） / 唯一约束 / 唯一索引（unique）
2. 引用完整性（参照完整性）- 关系中不允许引用不存在的实体
   - 外键（foreign key）
3. 域完整性 - 数据是有效的
   - 数据类型及长度
   - 非空约束（not null）
   - 默认值约束（default）
   - 检查约束（check）

#### 数据一致性

1. 事务：一系列对数据库进行读/写的操作。

2. 事务的ACID特性
   - 原子性：事务作为一个整体被执行，包含在其中的对数据库的操作要么全部被执行，要么都不执行
   - 一致性：事务应确保数据库的状态从一个一致状态转变为另一个一致状态
   - 隔离性：多个事务并发执行时，一个事务的执行不应影响其他事务的执行
   - 持久性：已被提交的事务对数据库的修改应该永久保存在数据库中

### Python数据库编程

我们用如下所示的数据库来演示在Python中如何访问MySQL数据库。

```SQL
drop database if exists hrs;
create database hrs default charset utf8;

use hrs;

drop table if exists tb_emp;
drop table if exists tb_dept;

create table tb_dept
(
dno   int not null comment '编号',
dname varchar(10) not null comment '名称',
dloc  varchar(20) not null comment '所在地',
primary key (dno)
);

insert into tb_dept values 
	(10, '会计部', '北京'),
	(20, '研发部', '成都'),
	(30, '销售部', '重庆'),
	(40, '运维部', '深圳');

create table tb_emp
(
eno   int not null comment '员工编号',
ename varchar(20) not null comment '员工姓名',
job   varchar(20) not null comment '员工职位',
mgr   int comment '主管编号',
sal   int not null comment '员工月薪',
comm  int comment '每月补贴',
dno   int comment '所在部门编号',
primary key (eno)
);

alter table tb_emp add constraint fk_emp_dno foreign key (dno) references tb_dept (dno);

insert into tb_emp values 
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

在Python 3中，我们通常使用纯Python的三方库PyMySQL来访问MySQL数据库，它应该是目前最好的选择。

1. 安装PyMySQL。

   ```Shell
   pip install pymysql
   ```

2. 添加一个部门。

   ```Python
   import pymysql
   
   
   def main():
       no = int(input('编号: '))
       name = input('名字: ')
       loc = input('所在地: ')
       # 1. 创建数据库连接对象
       con = pymysql.connect(host='localhost', port=3306,
                             database='hrs', charset='utf8',
                             user='root', password='123456')
       try:
           # 2. 通过连接对象获取游标
           with con.cursor() as cursor:
               # 3. 通过游标执行SQL并获得执行结果
               result = cursor.execute(
                   'insert into tb_dept values (%s, %s, %s)',
                   (no, name, loc)
               )
           if result == 1:
               print('添加成功!')
           # 4. 操作成功提交事务
           con.commit()
       finally:
           # 5. 关闭连接释放资源
           con.close()
   
   
   if __name__ == '__main__':
       main()
   ```

3. 删除一个部门。

   ```Python
   import pymysql
   
   
   def main():
       no = int(input('编号: '))
       con = pymysql.connect(host='localhost', port=3306,
                             database='hrs', charset='utf8',
                             user='root', password='123456',
                             autocommit=True)
       try:
           with con.cursor() as cursor:
               result = cursor.execute(
                   'delete from tb_dept where dno=%s',
                   (no, )
               )
           if result == 1:
               print('删除成功!')
       finally:
           con.close()
   
   
   if __name__ == '__main__':
       main()
   ```

4. 更新一个部门。

   ```Python
   import pymysql
   
   
   def main():
       no = int(input('编号: '))
       name = input('名字: ')
       loc = input('所在地: ')
       con = pymysql.connect(host='localhost', port=3306,
                             database='hrs', charset='utf8',
                             user='root', password='123456',
                             autocommit=True)
       try:
           with con.cursor() as cursor:
               result = cursor.execute(
                   'update tb_dept set dname=%s, dloc=%s where dno=%s',
                   (name, loc, no)
               )
           if result == 1:
               print('更新成功!')
       finally:
           con.close()
   
   
   if __name__ == '__main__':
       main()
   ```

5. 查询所有部门。

   ```Python
   import pymysql
   from pymysql.cursors import DictCursor
   
   
   def main():
       con = pymysql.connect(host='localhost', port=3306,
                             database='hrs', charset='utf8',
                             user='root', password='123456')
       try:
           with con.cursor(cursor=DictCursor) as cursor:
               cursor.execute('select dno as no, dname as name, dloc as loc from tb_dept')
               results = cursor.fetchall()
               print(results)
               print('编号\t名称\t\t所在地')
               for dept in results:
                   print(dept['no'], end='\t')
                   print(dept['name'], end='\t')
                   print(dept['loc'])
       finally:
           con.close()
   
   
   if __name__ == '__main__':
       main()
   ```

6. 分页查询员工信息。

   ```Python
   import pymysql
   from pymysql.cursors import DictCursor
   
   
   class Emp(object):
   
       def __init__(self, no, name, job, sal):
           self.no = no
           self.name = name
           self.job = job
           self.sal = sal
   
       def __str__(self):
           return f'\n编号：{self.no}\n姓名：{self.name}\n职位：{self.job}\n月薪：{self.sal}\n'
   
   
   def main():
       page = int(input('页码: '))
       size = int(input('大小: '))
       con = pymysql.connect(host='localhost', port=3306,
                             database='hrs', charset='utf8',
                             user='root', password='123456')
       try:
           with con.cursor() as cursor:
               cursor.execute(
                   'select eno as no, ename as name, job, sal from tb_emp limit %s,%s',
                   ((page - 1) * size, size)
               )
               for emp_tuple in cursor.fetchall():
                   emp = Emp(*emp_tuple)
                   print(emp)
       finally:
           con.close()
   
   
   if __name__ == '__main__':
       main()
   ```
