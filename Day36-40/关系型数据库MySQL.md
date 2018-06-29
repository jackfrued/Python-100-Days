## 关系型数据入门

### 关系型数据概述

1. 数据持久化。
2. 数据库发展史。
3. 关系型数据库特点。
   - 理论基础：集合论和关系代数。
   - 具体表象：用二维表（有行和列）组织数据。
   - 编程语言：结构化查询语言（SQL）。
4. E-R图。
   - 实体 - 矩形框
   - 属性 - 椭圆框
   - 关系 - 菱形框
   - 重数 - 1:1 / 1:N / M:N
5. 关系型数据库产品。
   - [Oracle](https://www.oracle.com/index.html)
   - [DB2](https://www.ibm.com/analytics/us/en/db2/)
   - [SQL Server](https://www.microsoft.com/en-us/sql-server/)
   - [MySQL](https://www.mysql.com/)
   - [SQLite](https://www.sqlite.org/index.html)

### MySQL简介

1. 安装和配置。
2. 常用命令。

### SQL详解

1. DDL

   ```SQL
   
   -- 创建数据库SRS
   drop database if exists SRS;
   create database SRS default charset utf8;
   
   -- 切换到SRS
   use SRS;
   
   -- 创建学院表
   create table tb_college
   (
   collid int not null auto_increment comment '学院编号',
   collname varchar(50) not null comment '学院名称',
   collmaster varchar(20) not null comment '院长姓名',
   collweb varchar(511) default '' comment '学院网站',
   primary key (collid)
   );
   
   -- 添加唯一性约束
   alter table tb_college add constraint uni_college_collname unique (collname);
   -- alter table tb_college drop index uni_college_collname;
   
   -- 创建学生表
   create table tb_student
   (
   stuid int not null comment '学号',
   stuname varchar(20) not null comment '学生姓名',
   stusex bit default 1 comment '性别',
   stubirth date not null comment '出生日期',
   stuaddr varchar(255) default '' comment '籍贯',
   collid int not null comment '所属学院编号',
   primary key (stuid)
   );
   
   -- 添加外键约束
   alter table tb_student add constraint fk_student_collid foreign key (collid) references tb_college (collid);
   
   -- 创建教师表
   create table tb_teacher
   (
   teacherid int not null comment '教师工号',
   tname varchar(20) not null comment '教师姓名',
   ttitle varchar(10) default '' comment '职称',
   collid int not null comment '所属学院编号'
   );
   
   -- 添加主键约束
   alter table tb_teacher add constraint pk_teacher primary key (teacherid);
   
   -- 添加外键约束
   alter table tb_teacher add constraint fk_teacher_collid foreign key (collid) references tb_college (collid);
   
   -- 创建课程表
   create table tb_course
   (
   courseid int not null comment '课程编号',
   cname varchar(50) not null comment '课程名称',
   ccredit tinyint not null comment '学分',
   tid int not null comment '教师工号',
   primary key (courseid)
   );
   
   -- 添加外键约束
   alter table tb_course add constraint fk_course_tid foreign key (tid) references tb_teacher (teacherid);
   
   -- 创建学生选课表
   create table tb_score
   (
   scid int not null auto_increment comment '选课编号',
   sid int not null comment '学号',
   cid int not null comment '课程编号',
   selectdate datetime comment '选课时间日期',
   score decimal(4,1) comment '考试成绩',
   primary key (scid)
   );
   
   -- 添加检查约束(MySQL中检查约束不生效)
   alter table tb_score add constraint ck_score_score check (score between 0 and 100);
   
   -- 添加外键约束
   alter table tb_score add constraint fk_score_sid foreign key (sid) references tb_student (stuid);
   alter table tb_score add constraint fk_score_cid foreign key (cid) references tb_course (courseid);
   ```

2. DML

   ```SQL
   
   -- 插入学院数据
   insert into tb_college 
   (collname, collmaster, collweb) values 
   ('计算机学院', '左冷禅', 'http://www.abc.com'),
   ('外国语学院', '岳不群', 'http://www.xyz.com'),
   ('经济管理学院', '风清扬', 'http://www.foo.com');
   
   -- 插入学生数据
   insert into tb_student 
   (stuid, stuname, stusex, stubirth, stuaddr, collid) values
   (1001, '向问天', 1, '1990-3-4', '四川成都', 1),
   (1002, '任我行', 1, '1992-2-2', '湖南长沙', 1),
   (1033, '任盈盈', 0, '1989-12-3', '湖南长沙', 1),
   (1572, '余沧海', 1, '1993-7-19', '四川成都', 1),
   (1378, '岳灵珊', 0, '1995-8-12', '四川绵阳', 1),
   (1954, '林平之', 1, '1994-9-20', '福建莆田', 1),
   (2035, '令狐冲', 1, '1988-6-30', '陕西咸阳', 2),
   (3011, '林震南', 1, '1985-12-12', '福建莆田', 3),
   (3755, '龙傲天', 1, '1993-1-25', '广东东莞', 3),
   (3923, '向天问', 0, '1985-4-17', '四川成都', 3),
   (2177, '隔壁老王', 1, '1989-11-27', '四川成都', 2);
   
   -- 插入老师数据
   insert into tb_teacher 
   (teacherid, tname, ttitle, collid) values 
   (1122, '张三丰', '教授', 1),
   (1133, '宋远桥', '副教授', 1),
   (1144, '杨逍', '副教授', 1),
   (2255, '范遥', '副教授', 2),
   (3366, '韦一笑', '讲师', 3);
   
   -- 插入课程数据
   insert into tb_course
   (courseid, cname, ccredit, tid) values 
   (1111, 'Python程序设计', 3, 1122),
   (2222, 'Web前端开发', 2, 1122),
   (3333, '操作系统', 4, 1122),
   (4444, '计算机网络', 2, 1133),
   (5555, '编译原理', 4, 1144),
   (6666, '算法和数据结构', 3, 1144),
   (7777, '经贸法语', 3, 2255),
   (8888, '成本会计', 2, 3366),
   (9999, '审计', 3, 3366);
   
   -- 插入选课数据
   insert into tb_score 
   (sid, cid, selectdate, score) values 
   (1001, 1111, now(), 95),
   (1001, 2222, now(), 87.5),
   (1001, 3333, now(), 100),
   (1001, 4444, now(), null),
   (1001, 6666, now(), 100),
   (1002, 1111, now(), 65),
   (1002, 5555, now(), 42),
   (1033, 1111, now(), 92.5),
   (1033, 4444, now(), 78),
   (1033, 5555, now(), 82.5),
   (1572, 1111, now(), 78),
   (1378, 1111, now(), 82),
   (1378, 7777, now(), 65.5),
   (2035, 7777, now(), 88),
   (2035, 9999, now(), 70),
   (3755, 1111, now(), 72.5),
   (3755, 8888, now(), 93),
   (3755, 9999, now(), null);
   
   -- 删除数据
   delete from tb_student where stuid=2177;
   
   -- 更新数据
   update tb_score set score=null where sid=1002 and cid=1111;
   ```

3. DQL

   ```SQL
   
   -- 查询所有学生信息
   select * from tb_student;
   select stuid, stuname, stusex, stubirth, stuaddr, collid 
   from tb_student;
   
   -- 查询所有课程名称及学分(投影和别名)
   select cname as 课程名称, ccredit as 学分 from tb_course;
   
   -- 查询所有女学生的姓名和出生日期(筛选)
   select stuname, stubirth from tb_student where stusex=0;
   
   -- 查询所有80后女学生的姓名、性别(显示成'女')和出生日期(筛选)
   select stuname, '女' as stusex, stubirth from tb_student 
   where stubirth between '1980-1-1' and '1989-12-31' and stusex=0;
   
   -- 查询姓“林”的学生姓名和性别(模糊)
   select stuname, if(stusex, '男', '女') as stusex 
   from tb_student where stuname like '林%';
   
   -- 查询姓“张”名字总共两个字的老师的姓名和职称(模糊)
   select tname from tb_teacher where tname like '张_';
   
   -- 查询姓“张”名字总共三个字的老师的姓名和职称(模糊)
   select tname, ttitle from tb_teacher where tname like '张__';
   
   -- 查询名字中有“天”字的学生的姓名(模糊)
   select stuname from tb_student where stuname like '%天%';
   
   -- 查询学生的籍贯(去重)
   select distinct stuaddr from tb_student 
   where stuaddr<>'' and stuaddr is not null;
   
   -- 查询男学生的姓名和生日按年龄从大到小排列(排序)
   select stuname, stubirth from tb_student 
   where stusex=1 order by stubirth asc;
   
   -- 查询年龄最大/最小的学生的出生日期(聚合函数)
   select min(stubirth) from tb_student;
   select max(stubirth) from tb_student;
   -- 查询学生/男学生/女学生的总人数
   select count(stuid) from tb_student;
   select count(stuid) from tb_student where stusex=1;
   select count(stuid) from tb_student where stusex=0;
   -- 查询1111课程的平均分/最低分/最高分/选课人数/考试人数
   select avg(score) from tb_score where cid=1111;
   select min(score) from tb_score where cid=1111;
   select max(score) from tb_score where cid=1111;
   select count(sid) from tb_score where cid=1111;
   select count(score) from tb_score where cid=1111;
   
   -- 查询男女学生的人数(分组和聚合函数)
   select if(stusex, '男', '女') as 性别, count(stusex) as 人数 
   from tb_student group by stusex order by 人数 desc;
   
   -- 查询学号为1001的学生所有课程的总成绩(筛选和聚合函数)
   select sum(score) as 总成绩 from tb_score where sid=1001;
   
   -- 查询每个学生的学号和平均成绩(分组和聚合函数)
   select sid as 学号, avg(score) as 平均分 from tb_score 
   where score is not null 
   group by sid 
   order by 平均分 desc;
   
   -- 查询平均成绩大于等于80分的学生的学号和平均成绩(分组后的筛选)
   select sid as 学号, avg(score) as 平均分 from tb_score 
   group by sid having 平均分>=80 
   order by 平均分 desc;
   
   -- 查询年龄最大的学生的姓名(子查询)
   select stuname from tb_student 
   where stubirth=(select min(stubirth) from tb_student);
   
   -- 查询选了三门及以上的课程的学生姓名(子查询/分组条件/集合运算)
   select stuname from tb_student where stuid in 
   (select sid from tb_score group by sid having count(sid)>=3);
   
   -- 查询课程名称、学分、授课老师的名字和职称
   select cname, ccredit, tname, ttitle 
   from tb_course, tb_teacher 
   where tid=teacherid;
   
   select cname, ccredit, tname, ttitle from tb_course 
   inner join tb_teacher on tid=teacherid;
   
   -- 查询学生姓名和所在学院名称
   select stuname, collname 
   from tb_student t1, tb_college t2 
   where t1.collid=t2.collid;
   
   select stuname, collname from tb_student t1 
   inner join tb_college t2 on t1.collid=t2.collid;
   
   -- 查询学生姓名、课程名称以及考试成绩
   select stuname, cname, score 
   from tb_student, tb_course, tb_score 
   where stuid=sid and courseid=cid 
   and score is not null;
   
   select stuname, cname, score from tb_student 
   inner join tb_score on stuid=sid
   inner join tb_course on courseid=cid 
   where score is not null;
   
   -- 查询选课学生的姓名和平均成绩(子查询和连接查询)
   select stuname, avgscore from tb_student,
   (select sid, avg(score) as avgscore from tb_score 
   group by sid) temp where sid=stuid;
   
   select stuname, avgscore from tb_student 
   inner join (select sid, avg(score) as avgscore 
   from tb_score group by sid) temp on sid=stuid;
   
   -- 查询每个学生的姓名和选课数量(左外连接和子查询)
   select stuname as 姓名, ifnull(total, 0) as 选课数量 
   from tb_student left outer join (select sid, count(sid) as total 
   from tb_score group by sid) temp on stuid=sid;
   ```

4. DCL

   ```SQL
   
   -- 创建名为hellokitty的用户
   create user 'hellokitty'@'localhost' identified by '123123';
   
   -- 将对SRS数据库所有对象的所有操作权限授予hellokitty
   grant all privileges on SRS.* to 'hellokitty'@'localhost';
   
   -- 召回hellokitty对SRS数据库所有对象的insert/delete/update权限
   revoke insert, delete, update on SRS.* from 'hellokitty'@'localhost';
   ```

###  相关知识

#### 范式理论

#### 数据完整性

1. 实体完整性 - 每个实体都是独一无二的
   - 主键 / 唯一约束 / 唯一索引
2. 引用完整性（参照完整性）
   - 外键
3. 域完整性 - 数据是有效的
   - 数据类型
   - 非空约束
   - 默认值约束
   - 检查约束

### Python数据库编程

1. MySQLdb
2. PyMySQL


