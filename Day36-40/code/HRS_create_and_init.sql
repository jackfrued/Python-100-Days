drop database if exists hrs;
create database hrs default charset utf8;

use hrs;

drop table if exists tb_emp;
drop table if exists tb_dept;

create table tb_dept
(
dno int not null comment '编号',
dname varchar(10) not null comment '名称',
dloc varchar(20) not null comment '所在地',
primary key (dno)
);

insert into tb_dept values 
	(10, '会计部', '北京'),
	(20, '研发部', '成都'),
	(30, '销售部', '重庆'),
	(40, '运维部', '深圳');

create table tb_emp
(
eno int not null comment '员工编号',
ename varchar(20) not null comment '员工姓名',
job varchar(20) not null comment '员工职位',
mgr int comment '主管编号',
sal int not null comment '员工月薪',
comm int comment '每月补贴',
dno int comment '所在部门编号',
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


-- 查询月薪最高的员工姓名和工资

-- 查询员工的姓名和年薪((月薪+补贴)*13)

-- 查询有员工的部门的编号和人数

-- 查询所有部门的名称和人数

-- 查询月薪最高的员工(Boss除外)的姓名和工资

-- 查询薪水超过平均薪水的员工的姓名和工资

-- 查询薪水超过其所在部门平均薪水的员工的姓名、部门编号和工资

-- 查询部门中薪水最高的人姓名、工资和所在部门名称

-- 查询主管的姓名和职位

-- 查询月薪排名4~6名的员工姓名和工资
