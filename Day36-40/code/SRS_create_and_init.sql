-- 如果存在名为school的数据库就删除它
drop database if exists `school`;

-- 创建名为school的数据库并设置默认的字符集和排序方式
create database `school` default charset utf8mb4;

-- 切换到school数据库上下文环境
use `school`;

-- 创建学院表
create table `tb_college`
(
`col_id` int unsigned auto_increment comment '编号',
`col_name` varchar(50) not null comment '名称',
`col_intro` varchar(5000) default '' comment '介绍',
primary key (`col_id`)
) engine=innodb comment '学院表';

-- 创建学生表
create table `tb_student`
(
`stu_id` int unsigned not null comment '学号',
`stu_name` varchar(20) not null comment '姓名',
`stu_sex` boolean default 1 comment '性别',
`stu_birth` date not null comment '出生日期',
`stu_addr` varchar(255) default '' comment '籍贯',
`col_id` int unsigned not null comment '所属学院',
primary key (`stu_id`),
foreign key (`col_id`) references `tb_college` (`col_id`)
) engine=innodb comment '学生表';

-- 创建教师表
create table `tb_teacher`
(
`tea_id` int unsigned not null comment '工号',
`tea_name` varchar(20) not null comment '姓名',
`tea_title` varchar(10) default '助教' comment '职称',
`col_id` int unsigned not null comment '所属学院',
primary key (`tea_id`),
foreign key (`col_id`) references `tb_college` (`col_id`)
) engine=innodb comment '老师表';

-- 创建课程表
create table `tb_course`
(
`cou_id` int unsigned not null comment '编号',
`cou_name` varchar(50) not null comment '名称',
`cou_credit` int unsigned not null comment '学分',
`tea_id` int unsigned not null comment '授课老师',
primary key (`cou_id`),
foreign key (`tea_id`) references `tb_teacher` (`tea_id`)
) engine=innodb comment '课程表';

-- 创建选课记录表
create table `tb_record`
(
`rec_id` bigint unsigned auto_increment comment '选课记录号',
`sid` int unsigned not null comment '学号',
`cid` int unsigned not null comment '课程编号',
`sel_date` date not null comment '选课日期',
`score` decimal(4,1) comment '考试成绩',
primary key (`rec_id`),
foreign key (`sid`) references `tb_student` (`stu_id`),
foreign key (`cid`) references `tb_course` (`cou_id`),
unique (`sid`, `cid`)
) engine=innodb comment '选课记录表';

-- 插入学院数据
insert into `tb_college` 
    (`col_name`, `col_intro`) 
values 
    ('计算机学院', '计算机学院1958年设立计算机专业，1981年建立计算机科学系，1998年设立计算机学院，2005年5月，为了进一步整合教学和科研资源，学校决定，计算机学院和软件学院行政班子合并统一运作、实行教学和学生管理独立运行的模式。 学院下设三个系：计算机科学与技术系、物联网工程系、计算金融系；两个研究所：图象图形研究所、网络空间安全研究院（2015年成立）；三个教学实验中心：计算机基础教学实验中心、IBM技术中心和计算机专业实验中心。'),
    ('外国语学院', '外国语学院设有7个教学单位，6个文理兼收的本科专业；拥有1个一级学科博士授予点，3个二级学科博士授予点，5个一级学科硕士学位授权点，5个二级学科硕士学位授权点，5个硕士专业授权领域，同时还有2个硕士专业学位（MTI）专业；有教职员工210余人，其中教授、副教授80余人，教师中获得中国国内外名校博士学位和正在职攻读博士学位的教师比例占专任教师的60%以上。'),
    ('经济管理学院', '经济学院前身是创办于1905年的经济科；已故经济学家彭迪先、张与九、蒋学模、胡寄窗、陶大镛、胡代光，以及当代学者刘诗白等曾先后在此任教或学习。');

-- 插入学生数据
insert into `tb_student` 
    (`stu_id`, `stu_name`, `stu_sex`, `stu_birth`, `stu_addr`, `col_id`) 
values
    (1001, '杨过', 1, '1990-3-4', '湖南长沙', 1),
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
insert into `tb_teacher` 
    (`tea_id`, `tea_name`, `tea_title`, `col_id`) 
values 
    (1122, '张三丰', '教授', 1),
    (1133, '宋远桥', '副教授', 1),
    (1144, '杨逍', '副教授', 1),
    (2255, '范遥', '副教授', 2),
    (3366, '韦一笑', default, 3);

-- 插入课程数据
insert into `tb_course` 
    (`cou_id`, `cou_name`, `cou_credit`, `tea_id`) 
values 
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
insert into `tb_record` 
    (`sid`, `cid`, `sel_date`, `score`) 
values 
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
    (2035, 9999, '2019-09-02', null),
    (3755, 1111, '2019-09-02', null),
    (3755, 8888, '2019-09-02', null),
    (3755, 9999, '2017-09-01', 92);
