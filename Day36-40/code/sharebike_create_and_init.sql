drop database if exists sharebike;

create database sharebike default charset utf8;

use sharebike;

create table tb_city
(
    cityid integer not null auto_increment,
    cityname varchar(20) not null,
    primary key (cityid)
);

create table tb_user
(
    userid integer not null auto_increment,
    nickname varchar(50) not null,
    tel char(11) not null,
    cityid integer not null,
    regdate date,
    primary key (userid)
);

create table tb_bike
(
    bikeid integer not null auto_increment,
    statecode integer default 0,
    broken bit default 0,
    primary key (bikeid)
);

create table tb_record
(
    recordid integer not null auto_increment,
    userid integer not null,
    bikeid integer not null,
    begintime datetime not null,
    endtime datetime,
    payway integer,
    cost float,
    primary key (recordid)
);

alter table tb_record add constraint fk_record_userid foreign key (userid) references tb_user (userid);

alter table tb_record add constraint fk_record_bikeid foreign key (bikeid) references tb_bike (bikeid);

select cityname, total from (select cityid, count(cityid) as total from tb_user group by cityid) t1 inner join tb_city t2 on t1.cityid=t2.cityid;

select max(total) from (select userid, count(userid) as total from tb_record group by userid) t1

select nickname, cityname from (select userid, count(userid) as total from tb_record group by userid having total=(select max(total) from (select userid, count(userid) as total from tb_record group by userid) t1)) t2 inner join tb_user as t3 on t2.userid=t3.userid inner join tb_city as t4 on t3.cityid=t4.cityid;

select bikeid, broken from tb_bike 