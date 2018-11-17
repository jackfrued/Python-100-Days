-- 查看MySQL服务器所有数据库
show databases;
-- 删除SRS数据库
drop database if exists SRS;
-- 创建学生选课系统(SRS)数据库并指定默认字符集
create database SRS default charset utf8;
-- 切换至SRS数据库
use SRS;
-- 查看当前数据库中所有表
show tables;
-- 创建学生表
create table TbStudent
(
stuid integer not null,
stuname varchar(20) not null,
stusex bit default 1,
stubirth datetime not null,
stutel char(11),
stuaddr varchar(255),
stuphoto longblob,
primary key (stuid)
);
-- 修改学生表删除stutel列
alter table TbStudent drop column stutel;
-- 查看学生表结构
desc TbStudent;
-- 如果表TbCourse已经存在就删除它
drop table if exists TbCourse;
-- 创建课程表
create table TbCourse
(
cosid integer not null,
cosname varchar(50) not null,
coscredit tinyint not null,
cosintro varchar(255)
);
-- 给课程表指定主键
alter table TbCourse add constraint pk_course primary key (cosid);
-- 创建学生选课记录表
create table TbSC
(
scid integer primary key auto_increment,
sid integer not null,
cid integer,
scdate datetime not null,
score float
);
-- 给表TbSC添加外键约束
alter table TbSC add constraint fk_sid foreign key (sid) references TbStudent (stuid) on delete cascade on update cascade;
alter table TbSC add constraint fk_cid foreign key (cid) references TBCourse (cosid) on delete set null on update cascade;
-- 添加学生记录
insert into TbStudent values (1001, '张三丰', default, '1978-1-1', '成都市一环路西二段17号', null);
insert into TbStudent (stuid, stuname, stubirth) values (1002, '郭靖', '1980-2-2');
insert into TbStudent (stuid, stuname, stusex, stubirth, stuaddr) values (1003, '黄蓉', 0, '1982-3-3', '成都市二环路南四段123号');
insert into TbStudent values (1004, '张无忌', 1, '1990-4-4', null, null);
insert into TbStudent values 
(1005, '丘处机', 1, '1983-5-5', '北京市海淀区宝盛北里西区28号', null),
(1006, '王处一', 1, '1985-6-6', '深圳市宝安区宝安大道5010号', null),
(1007, '刘处玄', 1, '1987-7-7', '郑州市金水区纬五路21号', null),
(1008, '孙不二', 0, '1989-8-8', '武汉市光谷大道61号', null),
(1009, '平一指', 1, '1992-9-9', '西安市雁塔区高新六路52号', null),
(1010, '老不死', 1, '1993-10-10', '广州市天河区元岗路310号', null),
(1011, '王大锤', 0, '1994-11-11', null, null),
(1012, '隔壁老王', 1, '1995-12-12', null, null),
(1013, '郭啸天', 1, '1977-10-25', null, null);
-- 删除学生记录
delete from TbStudent where stuid=1004;
-- 更新学生记录
update TbStudent set stubirth='1980-12-12', stuaddr='上海市宝山区同济支路199号' where stuid=1002;
-- 添加课程记录
insert into TbCourse values 
(1111, 'C语言程序设计', 3, '大神级讲师授课需要抢座'),
(2222, 'Java程序设计', 3, null),
(3333, '数据库概论', 2, null),
(4444, '操作系统原理', 4, null);
-- 添加学生选课记录
insert into TbSC values 
(default, 1001, 1111, '2016-9-1', 95),
(default, 1002, 1111, '2016-9-1', 94),
(default, 1001, 2222, now(), null),
(default, 1001, 3333, '2017-3-1', 85),
(default, 1001, 4444, now(), null),
(default, 1002, 4444, now(), null),
(default, 1003, 2222, now(), null),
(default, 1003, 3333, now(), null),
(default, 1005, 2222, now(), null),
(default, 1006, 1111, now(), null),
(default, 1006, 2222, '2017-3-1', 80),
(default, 1006, 3333, now(), null),
(default, 1006, 4444, now(), null),
(default, 1007, 1111, '2016-9-1', null),
(default, 1007, 3333, now(), null),
(default, 1007, 4444, now(), null),
(default, 1008, 2222, now(), null),
(default, 1010, 1111, now(), null);
-- 查询所有学生信息
select * from TbStudent;
-- 查询所有课程名称及学分(投影和别名)
select cosname as `课程名称`, coscredit as `学分` from TbCourse;
-- 查询所有女学生的姓名和出生日期(筛选)
select stuname, stubirth from TbStudent where stusex=0;
-- 查询所有80后学生的姓名、性别和出生日期(筛选)
select stuname as `姓名`, if(stusex, '男', '女') as `性别`, stubirth as `出生日期`
from TbStudent where stubirth between '1980-1-1' and '1989-12-31';
-- 查询姓王的学生姓名和性别(模糊)
select stuname, stusex from TbStudent where stuname like '王%';
-- 查询姓郭名字总共两个字的学生的姓名(模糊)
select stuname from TbStudent where stuname like '郭_';
-- 查询姓郭名字总共三个字的学生的姓名(模糊)
select stuname from TbStudent where stuname like '郭__';
-- 查询名字中有王字的学生的姓名(模糊)
select stuname from TbStudent where stuname like '%王%';
-- 查询没有录入家庭住址和照片的学生姓名(多条件筛选和空值处理)
select stuname from TbStudent where stuaddr is null and stuphoto is null;
-- 查询学生选课的所有日期(去重)
select distinct scdate from TbSC;
-- 查询学生的姓名和生日按年龄从大到小排列(排序)
select stuname, stubirth from TbStudent order by stubirth;
-- 查询所有录入了家庭住址的男学生的姓名、出生日期和家庭住址按年龄从小到大排列(多条件筛选和排序)
select stuname, stubirth, stuaddr from TbStudent where stusex=1 and stuaddr is not null order by stubirth desc;
-- 查询年龄最大的学生的出生日期(聚合函数)
select min(stubirth) from TbStudent;
-- 查询年龄最小的学生的出生日期(聚合函数)
select max(stubirth) from TbStudent;
-- 查询男女学生的人数(分组和聚合函数)
select if(stusex, '男', '女') as `性别`, count(stusex) as `人数` from TbStudent group by stusex;
-- 查询课程编号为1111的课程的平均成绩(筛选和聚合函数)
select avg(score) as `平均成绩` from TbSC where cid=1111;
-- 查询学号为1001的学生所有课程的总成绩(筛选和聚合函数)
select sum(score) as `总成绩` from TbSC where sid=1001;
-- 查询每个学生的学号和平均成绩, null值处理成0(分组和聚合函数)
select sid as `学号`, ifnull(avg(score), 0) as `平均成绩` from TbSC group by sid;
-- 查询平均成绩大于等于90分的学生的学号和平均成绩
select sid as `学号`, avg(score) as `平均成绩` from TbSC group by sid having avg(score)>=90;


-- 查询年龄最大的学生的姓名(子查询)
select stuname from TbStudent where stubirth=(select min(stubirth) from TbStudent);
-- 查询选了两门以上的课程的学生姓名(子查询/分组条件/集合运算)
select stuname from TbStudent where stuid in 
(select sid from TbSC group by sid having count(sid)>2);
-- 查询选课学生的姓名和平均成绩(子查询和连接查询)
-- 写法1:
select stuname, avgscore from TbStudent t1 inner join
(select sid, avg(score) as avgscore from TbSC where score is not null group by sid) t2
on t1.stuid=t2.sid;
-- 写法2: 
select stuname, avgscore from TbStudent t1,
(select sid, avg(score) as avgscore from TbSC where score is not null group by sid) t2
where t1.stuid=t2.sid;
-- 查询学生姓名、所选课程名称和成绩(连接查询)
-- 写法1:
select stuname, cosname, score from 
TbStudent t1, TbCourse t2, TbSC t3
where t1.stuid=t3.sid and t2.cosid=t3.cid and t3.score is not null;
-- 写法2:
select stuname, cosname, score from TbStudent t1 inner join TbCourse t2
inner join (select sid, cid, score from TbSC where score is not null) t3 
on t1.stuid=t3.sid and t2.cosid=t3.cid;
-- 查询每个学生的姓名和选课数量(左外连接和子查询)
select stuname as `姓名`, ifnull(coscount, 0) as `选课数` from TbStudent t1
left outer join (select sid, count(sid) as coscount from TbSC group by sid) t2 
on t1.stuid=t2.sid;

-- 创建系统用户表(演示登录操作和SQL注入攻击)
create table TbUser
(
username varchar(20) primary key,
userpass varchar(20) not null
);
-- 插入用户数据
insert into TbUser values ('admin', 'admin');
insert into TbUser values ('hellokitty', '123123');

-- 创建根据学号查询课程平均成绩的存储过程
drop procedure if exists SpGetAvgScoreByStuId;

create procedure SpGetAvgScoreByStuId(stuId integer, out avgScore float)
begin 
    select avg(score) into avgScore from TbSC where sid=stuId;
end;

-- 调用上面的存储过程
-- set @stuId=1001;
call SpGetAvgScoreByStuId(1001, @avgScore);
select @avgScore as avgScore;