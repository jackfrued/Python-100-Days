drop database if exists shop;
create database shop default charset utf8;
	
use shop;

drop table if exists tb_goods;
create table tb_goods
(
gid int not null auto_increment,
gname varchar(50) not null,
gprice decimal(10,2) not null,
gimage varchar(255),
primary key (gid)
);

insert into tb_goods values 
(default, '乐事（Lay’s）无限薯片', 8.2, 'images/lay.jpg'),
(default, '旺旺 仙贝 加量装 540g', 18.5, 'images/wang.jpg'),
(default, '多儿比（Dolbee）黄桃水果罐头', 6.8, 'images/dolbee.jpg'),
(default, '王致和 精制料酒 500ml', 7.9, 'images/wine.jpg'),
(default, '陈克明 面条 鸡蛋龙须挂面', 1.0, 'images/noodle.jpg'),
(default, '鲁花 菜籽油 4L', 69.9, 'images/oil.jpg');