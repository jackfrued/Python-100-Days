drop database if exists Bank;

create database Bank default charset utf8;

use Bank;

create table TbAccount
(
accid char(8) primary key,
accowner varchar(20) not null,
accbalance float not null default 0
);

insert into TbAccount values (11223344, '王大锤', 1000);
insert into TbAccount values (22334455, '李小龙', 1000);