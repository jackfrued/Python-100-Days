-- 关系型数据库可以保证数据的完整性
-- 实体完整性：每条记录都是独一无二的没有冗余 - 主键/唯一索引
-- 参照完整性（引用完整性）：外键
-- 域完整性：数据类型、非空约束、默认值约束、检查约束


-- 创建SRS数据库
drop database if exists SRS;
create database SRS default charset utf8 collate utf8_bin;

-- 切换到SRS数据库
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

-- 添加唯一约束
alter table tb_college add constraint uni_college_collname unique (collname);

-- 创建学生表
create table tb_student
(
stuid int not null comment '学号',
sname varchar(20) not null comment '学生姓名',
gender bit default 1 comment '性别',
birth date not null comment '出生日期',
addr varchar(255) default '' comment '籍贯',
collid int not null comment '所属学院编号',
primary key (stuid)
);

-- 检查约束（MySQL不支持它）
alter table tb_student add constraint ck_student_birth 
check (birth between '1990-1-1' and '1999-12-31');

-- 添加外键约束
alter table tb_student add constraint fk_student_collid foreign key (collid) references tb_college (collid);

-- 创建教师表
create table tb_teacher
(
teaid int not null comment '教师工号',
tname varchar(20) not null comment '教师姓名',
title varchar(10) default '' comment '职称',
collid int not null comment '所属学院编号'
);

-- 添加主键约束
alter table tb_teacher add constraint pk_teacher primary key (teaid);

-- 添加外键约束
alter table tb_teacher add constraint fk_teacher_collid foreign key (collid) references tb_college (collid);

-- 创建课程表
create table tb_course
(
couid int not null comment '课程编号',
cname varchar(50) not null comment '课程名称',
credit tinyint not null comment '学分',
teaid int not null comment '教师工号',
primary key (couid)
);

-- 添加外键约束
alter table tb_course add constraint fk_course_tid foreign key (teaid) references tb_teacher (teaid);

-- 创建学生选课表
create table tb_score
(
scid int not null auto_increment comment '选课编号',
sid int not null comment '学号',
cid int not null comment '课程编号',
seldate date comment '选课时间日期',
mark decimal(4,1) comment '考试成绩',
primary key (scid)
);

-- 添加外键约束
alter table tb_score add constraint fk_score_sid foreign key (sid) references tb_student (stuid);
alter table tb_score add constraint fk_score_cid foreign key (cid) references tb_course (couid);
-- 添加唯一约束
alter table tb_score add constraint uni_score_sid_cid unique (sid, cid);


-- 插入学院数据
insert into tb_college (collname, collmaster, collweb) values 
('计算机学院', '左冷禅', 'http://www.abc.com'),
('外国语学院', '岳不群', 'http://www.xyz.com'),
('经济管理学院', '风清扬', 'http://www.foo.com');

-- 插入学生数据
insert into tb_student (stuid, sname, gender, birth, addr, collid) values
(1001, '杨逍', 1, '1990-3-4', '四川成都', 1),
(1002, '任我行', 1, '1992-2-2', '湖南长沙', 1),
(1033, '王语嫣', 0, '1989-12-3', '四川成都', 1),
(1572, '岳不群', 1, '1993-7-19', '陕西咸阳', 1),
(1378, '纪嫣然', 0, '1995-8-12', '四川绵阳', 1),
(1954, '林平之', 1, '1994-9-20', '福建莆田', 1),
(2035, '东方不败', 1, '1988-6-30', null, 2),
(3011, '林震南', 1, '1985-12-12', '福建莆田', 3),
(3755, '项少龙', 1, '1993-1-25', null, 3),
(3923, '杨不悔', 0, '1985-4-17', '四川成都', 3);

-- 插入老师数据
insert into tb_teacher (teaid, tname, title, collid) values 
(1122, '张三丰', '教授', 1),
(1133, '宋远桥', '副教授', 1),
(1144, '杨逍', '副教授', 1),
(2255, '范遥', '副教授', 2),
(3366, '韦一笑', '讲师', 3);

-- 插入课程数据
insert into tb_course (couid, cname, credit, teaid) values 
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
insert into tb_score (sid, cid, seldate, mark) values 
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

-- 查询所有学生信息
select * from tb_student;
-- 查询所有课程名称及学分(投影和别名)
select cname as 课程名称, credit as 学分 from tb_course;
-- 查询所有女学生的姓名和出生日期(筛选)
select sname as 姓名, birth as 出生日期 from tb_student where gender=0;
-- 查询所有80后学生的姓名、性别和出生日期(筛选)
select sname, gender, birth from tb_student where birth between '1980-1-1' and '1989-12-31';
-- 查询姓”杨“的学生姓名和性别(模糊)
select sname, gender from tb_student where sname like '杨%';
-- 查询姓”杨“名字两个字的学生姓名和性别(模糊)
select sname, gender from tb_student where sname like '杨_';
-- 查询姓”杨“名字三个字的学生姓名和性别(模糊)
select sname, gender from tb_student where sname like '杨__';
-- 查询名字中有”不“字或“嫣”字的学生的姓名(模糊)
select sname from tb_student where sname like '%不%' or sname like '%嫣%';
-- 查询没有录入家庭住址的学生姓名(空值)
select sname from tb_student where addr is null or addr='';
-- 查询录入了家庭住址的学生姓名(空值)
select sname from tb_student where addr is not null and addr<>'';
-- 查询学生选课的所有日期(去重)
select distinct seldate from tb_score;
-- 查询学生的家庭住址(去重)
select distinct addr from tb_student where addr is not null and addr<>'';
-- 查询男学生的姓名和生日按年龄从大到小排列(排序)
select sname, birth from tb_student where gender=1 order by birth asc;
-- max() / min() / sum() / avg() / count()
-- 查询年龄最大的学生的出生日期(聚合函数)
select min(birth) from tb_student;
-- 查询年龄最小的学生的出生日期(聚合函数)
select max(birth) from tb_student;
-- 查询男女学生的人数(分组和聚合函数)
select if(gender, '男', '女') as 性别, count(gender) as 人数 
from tb_student group by gender;
-- 查询课程编号为1111的课程的平均成绩(筛选和聚合函数)
select avg(mark) as 平均分 from tb_score where cid=1111;
-- 查询学号为1001的学生所有课程的平均分(筛选和聚合函数)
select avg(mark) as 平均分 from tb_score where sid=1001;
-- 查询每个学生的学号和平均成绩(分组和聚合函数)
select sid, avg(mark) from tb_score where mark is not null group by sid;
-- 查询平均成绩大于等于90分的学生的学号和平均成绩
select sid, avg(mark) from tb_score group by sid having avg(mark)>=90;
-- 子查询 - 在一个查询中又使用到了另外一个查询的结果
-- 查询年龄最大的学生的姓名(子查询)
select sname from tb_student where birth=(select min(birth) from tb_student);
-- 查询年龄最大的学生姓名和年龄(子查询+运算)
select sname as 姓名, year(now()) - year(birth) as 年龄 
from tb_student where birth=(select min(birth) from tb_student);
-- 查询选了两门以上的课程的学生姓名(子查询/分组条件/集合运算)
select sname from tb_student where stuid in ( 
select sid from tb_score group by sid having count(sid)>2);
-- 连接查询（联结查询/联接查询）
-- 查询学生姓名、课程名称以及成绩
select sname, cname, mark 
from tb_score t1, tb_student t2, tb_course t3 
where t2.stuid=t1.sid and t3.couid=t1.cid and mark is not null;

select sname, cname, mark from tb_student t1 
inner join tb_score t2 on t1.stuid=t2.sid 
inner join tb_course t3 on t3.couid=t2.cid 
where mark is not null;
-- 查询选课学生的姓名和平均成绩(子查询和连接查询)
select sname, avgmark from tb_student t1, 
(select sid, avg(mark) as avgmark from tb_score group by sid) t2 
where stuid=sid;

select sname, avgmark from tb_student inner join 
(select sid, avg(mark) as avgmark from tb_score group by sid) t2 
on stuid=sid;
-- 注意：在连接查询时如果没有给出连接条件就会形成笛卡尔积

-- 查询每个学生的姓名和选课数量(左外连接和子查询)
-- 左外连接 - 把左表(写在前面的表)不满足连接条件的记录也查出来对应记录补null值
-- 右外连接 - 把右表(写在后面的表)不满足连接条件的记录也查出来对应记录补null值
select sname, total from tb_student left join 
(select sid, count(sid) as total from tb_score group by sid) tb_temp 
on stuid=sid;

-- DDL (Data Definition Language)
-- DML (Data Manipulation Language)
-- DCL (Data Control Language)

-- 创建名为hellokitty的用户并设置口令
create user 'hellokitty'@'%' identified by '123123';

-- 授权
grant select on srs.* to 'hellokitty'@'%';
grant insert, delete, update on srs.* to 'hellokitty'@'%';
grant create, drop, alter on srs.* to 'hellokitty'@'%';

grant all privileges on srs.* to 'hellokitty'@'%';
grant all privileges on srs.* to 'hellokitty'@'%' with grant option;

-- 召回
revoke all privileges on srs.* from 'hellokitty'@'%';

-- 事务控制
-- 开启事务环境
begin;
-- start transaction;
update tb_score set mark=mark-2 where sid=1001 and mark is not null;
update tb_score set mark=mark+2 where sid=1002 and mark is not null;
-- 事务提交
commit;
 -- 事务回滚
rollback;

begin;
delete from tb_score;
rollback;
