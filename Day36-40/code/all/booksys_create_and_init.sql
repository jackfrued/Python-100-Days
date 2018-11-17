drop database if exists booksys;

create database booksys default charset utf8;

use booksys;

create table tb_book
(
bookid integer not null,
isbn char(13) not null,
bname varchar(100) not null,
price decimal(8,2) not null,
author varchar(100) not null,
publisher varchar(50) not null,
pubdate date,
intro varchar(500),
lended bit default 0,
counter integer default 0,
primary key (bookid)
);

create table tb_reader
(
readerid integer not null,
rname varchar(20) not null,
gender bit not null,
tel char(11) not null,
birth date,
regdate date not null,
available bit default 1,
primary key (readerid)
);

create table tb_record
(
recordid integer not null auto_increment,
bid integer not null,
rid integer not null,
lenddate datetime not null,
backdate datetime,
pulishment decimal(6,2),
primary key (recordid)
);

alter table tb_record add constraint fk_record_bid foreign key (bid) references tb_book (bookid) on update cascade;
alter table tb_record add constraint fk_record_rid foreign key (rid) references tb_reader (readerid) on update cascade;