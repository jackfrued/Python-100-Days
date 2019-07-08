drop database if exists library;

create database library default charset utf8;

use library;

create table tb_book
(
bookid integer primary key auto_increment,
title varchar(100) not null,
author varchar(50) not null,
publisher varchar(50) not null,
price float not null,
lendout bit default 0,
lenddate datetime,
lendcount integer default 0
);

insert into tb_book (title, author, publisher, price, lendcount) values ('Java核心技术(卷1)', '凯 S.霍斯特曼', '机械工业出版社', 98.2, 102);
insert into tb_book (title, author, publisher, price, lendcount) values ('Java编程思想', '埃史尔', '机械工业出版社', 86.4, 87);
insert into tb_book (title, author, publisher, price, lendcount) values ('深入理解Java虚拟机', '周志明', '机械工业出版社', 64.4, 32);
insert into tb_book (title, author, publisher, price, lendcount) values ('Effective Java中文版(第2版) ', '埃史尔', '机械工业出版社', 36.8, 200);
insert into tb_book (title, author, publisher, price, lendcount) values ('数据结构与算法分析:Java语言描述(原书第3版)', '马克·艾伦·维斯', '机械工业出版社', 51.0, 15);
insert into tb_book (title, author, publisher, price, lendcount) values ('Java 8实战', '厄马', '人民邮电出版社', 56.8, 25);
insert into tb_book (title, author, publisher, price, lendcount) values ('重构:改善既有代码的设计', '马丁·福勒', '人民邮电出版社', 53.1, 99);
insert into tb_book (title, author, publisher, price, lendcount) values ('代码大全(第2版)', '史蒂夫•迈克康奈尔', '电子工业出版社', 53.1, 99);
insert into tb_book (title, author, publisher, price, lendcount) values ('程序员修炼之道:从小工到专家', '亨特, 托马斯', '电子工业出版社', 45.4, 50);
insert into tb_book (title, author, publisher, price, lendcount) values ('代码整洁之道', '马丁', '人民邮电出版社', 45.4, 30);
insert into tb_book (title, author, publisher, price, lendcount) values ('设计模式 可复用面向对象软件的基础', 'Erich Gamma, Richard Helm', '机械工业出版社', 30.2, 77);
insert into tb_book (title, author, publisher, price, lendcount) values ('设计模式之禅(第2版)', '秦小波', '机械工业出版社', 70.4, 100);

