drop database if exists bank;

create database bank default charset utf8;

use bank;

create table tb_account
(
accid char(8) primary key,
accowner varchar(20) not null,
accbalance float not null default 0
);

insert into tb_account values (11223344, '王大锤', 1000);
insert into tb_account values (22334455, '李小龙', 1000);