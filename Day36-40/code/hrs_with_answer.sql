drop database if exists hrs;
create database hrs default charset utf8mb4;

use hrs;

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
primary key (eno),
foreign key (dno) references tb_dept (dno)
);

-- alter table tb_emp add constraint pk_emp_eno primary key (eno);
-- alter table tb_emp add constraint uk_emp_ename unique (ename);
-- alter table tb_emp add constraint fk_emp_mgr foreign key (mgr) references tb_emp (eno);
-- alter table tb_emp add constraint fk_emp_dno foreign key (dno) references tb_dept (dno);

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


-- 查询月薪最高的员工姓名和月薪
select ename, sal from tb_emp where sal=(select max(sal) from tb_emp);

select ename, sal from tb_emp where sal>=all(select sal from tb_emp);

-- 查询员工的姓名和年薪((月薪+补贴)*13)
select ename, (sal+ifnull(comm,0))*13 as ann_sal from tb_emp order by ann_sal desc;

-- 查询有员工的部门的编号和人数
select dno, count(*) as total from tb_emp group by dno;

-- 查询所有部门的名称和人数
select dname, ifnull(total,0) as total from tb_dept left join 
(select dno, count(*) as total from tb_emp group by dno) tb_temp 
on tb_dept.dno=tb_temp.dno;

-- 查询月薪最高的员工(Boss除外)的姓名和月薪
select ename, sal from tb_emp where sal=(
	select max(sal) from tb_emp where mgr is not null
);

-- 查询月薪排第2名的员工的姓名和月薪
select ename, sal from tb_emp where sal=(
	select distinct sal from tb_emp order by sal desc limit 1,1
);

select ename, sal from tb_emp where sal=(
	select max(sal) from tb_emp where sal<(select max(sal) from tb_emp)
);

-- 查询月薪超过平均月薪的员工的姓名和月薪
select ename, sal from tb_emp where sal>(select avg(sal) from tb_emp);

-- 查询月薪超过其所在部门平均月薪的员工的姓名、部门编号和月薪
select ename, t1.dno, sal from tb_emp t1 inner join 
(select dno, avg(sal) as avg_sal from tb_emp group by dno) t2
on t1.dno=t2.dno and sal>avg_sal;

-- 查询部门中月薪最高的人姓名、月薪和所在部门名称
select ename, sal, dname 
from tb_emp t1, tb_dept t2, (
	select dno, max(sal) as max_sal from tb_emp group by dno
) t3 where t1.dno=t2.dno and t1.dno=t3.dno and sal=max_sal;

-- 查询主管的姓名和职位
-- 提示：尽量少用in/not in运算，尽量少用distinct操作
-- 可以使用存在性判断（exists/not exists）替代集合运算和去重操作
select ename, job from tb_emp where eno in (
	select distinct mgr from tb_emp where mgr is not null
);

select ename, job from tb_emp where eno=any(
	select distinct mgr from tb_emp where mgr is not null
);

select ename, job from tb_emp t1 where exists (
	select 'x' from tb_emp t2 where t1.eno=t2.mgr
);

-- MySQL8有窗口函数：row_number() / rank() / dense_rank()
-- 查询月薪排名4~6名的员工的排名、姓名和月薪
select ename, sal from tb_emp order by sal desc limit 3,3;

select row_num, ename, sal from 
(select @a:=@a+1 as row_num, ename, sal 
from tb_emp, (select @a:=0) t1 order by sal desc) t2 
where row_num between 4 and 6;

-- 窗口函数不适合业务数据库，只适合做离线数据分析
select 
	ename, sal, 
	row_number() over (order by sal desc) as row_num,
    rank() over (order by sal desc) as ranking,
    dense_rank() over (order by sal desc) as dense_ranking
from tb_emp limit 3 offset 3;

select ename, sal, ranking from (
	select ename, sal, dense_rank() over (order by sal desc) as ranking from tb_emp
) tb_temp where ranking between 4 and 6;

-- 窗口函数主要用于解决TopN查询问题
-- 查询每个部门月薪排前2名的员工姓名、月薪和部门编号
select ename, sal, dno from (
	select ename, sal, dno, rank() over (partition by dno order by sal desc) as ranking
	from tb_emp
) tb_temp where ranking<=2;

select ename, sal, dno from tb_emp t1 
where (select count(*) from tb_emp t2 where t1.dno=t2.dno and t2.sal>t1.sal)<2 
order by dno asc, sal desc;
