-- 创建人力资源管理系统数据库
drop database if exists HRS;
create database HRS default charset utf8;
-- 切换数据库上下文环境
use HRS;
-- 删除表
drop table if exists TbEmp;
drop table if exists TbDept;
-- 创建部门表
create table TbDept
(
deptno tinyint primary key,	-- 部门编号
dname varchar(10) not null,	-- 部门名称
dloc varchar(20) not null	-- 部门所在地
);
-- 添加部门记录
insert into TbDept values (10, '会计部', '北京');
insert into TbDept values (20, '研发部', '成都');
insert into TbDept values (30, '销售部', '重庆');
insert into TbDept values (40, '运维部', '深圳');
-- 创建员工表
create table TbEmp
(
empno int primary key,		-- 员工编号
ename varchar(20) not null,	-- 员工姓名
job varchar(20) not null,	-- 员工职位
mgr int,					-- 主管编号
sal int not null,			-- 员工月薪
comm int,					-- 每月补贴
dno tinyint					-- 所在部门编号
);
-- 添加外键约束
alter table TbEmp add constraint fk_dno foreign key (dno) references TbDept(deptno);
-- 添加员工记录
insert into TbEmp values (7800, '张三丰', '总裁', null, 9000, 1200, 20);
insert into TbEmp values (2056, '乔峰', '分析师', 7800, 5000, 1500, 20);
insert into TbEmp values (3088, '李莫愁', '设计师', 2056, 3500, 800, 20);
insert into TbEmp values (3211, '张无忌', '程序员', 2056, 3200, null, 20);
insert into TbEmp values (3233, '丘处机', '程序员', 2056, 3400, null, 20);
insert into TbEmp values (3251, '张翠山', '程序员', 2056, 4000, null, 20);
insert into TbEmp values (5566, '宋远桥', '会计师', 7800, 4000, 1000, 10);
insert into TbEmp values (5234, '郭靖', '出纳', 5566, 2000, null, 10);
insert into TbEmp values (3344, '黄蓉', '销售主管', 7800, 3000, 800, 30);
insert into TbEmp values (1359, '胡一刀', '销售员', 3344, 1800, 200, 30);
insert into TbEmp values (4466, '苗人凤', '销售员', 3344, 2500, null, 30);
insert into TbEmp values (3244, '欧阳锋', '程序员', 3088, 3200, null, 20);
insert into TbEmp values (3577, '杨过', '会计', 5566, 2200, null, 10);
insert into TbEmp values (3588, '朱九真', '会计', 5566, 2500, null, 10);

-- 查询薪资最高的员工姓名和工资

-- 查询员工的姓名和年薪((月薪+补贴)*12)

-- 查询有员工的部门的编号和人数

-- 查询所有部门的名称和人数

-- 查询薪资最高的员工(Boss除外)的姓名和工资

-- 查询薪水超过平均薪水的员工的姓名和工资

-- 查询薪水超过其所在部门平均薪水的员工的姓名、部门编号和工资

-- 查询部门中薪水最高的人姓名、工资和所在部门名称

-- 查询主管的姓名和职位

-- 查询薪资排名4~6名的员工姓名和工资

use HRS;

drop procedure if exists sp_avg_sal_by_dept;


create procedure sp_avg_sal_by_dept(deptno integer, out avg_sal float)
begin 
    select avg(sal) into avg_sal from TbEmp where dno=deptno;
end;




call sp_avg_sal_by_dept(10, @avgSal);

select @avgSal;



