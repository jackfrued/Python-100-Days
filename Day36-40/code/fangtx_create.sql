drop database if exists fangtx;

create database fangtx default charset utf8 collate utf8_bin;
	
use fangtx;

/* 创建用户表 */
create table `tb_user`
(
   `userid`               int auto_increment comment '编号',
   `username`             varchar(20) not null comment '用户名',
   `password`             char(32) not null comment '用户口令',
   `realname`             varchar(20) not null comment '真实姓名',
   `sex`                  bool default 1 comment '性别',
   `tel`                  varchar(20) not null comment '手机号',
   `email`                varchar(255) default '' comment '邮箱',
   `regdate`              datetime default now() comment '注册日期',
   `point`                int default 0 comment '积分',
   `lastvisit`            datetime default now() comment '最后访问时间',
   `is_authenticated`     bit default 0 comment '是否认证',
   primary key (`userid`)
);

/* 创建地区表 */
create table `tb_district`
(
   `distid`               int not null comment '编号',
   `pid`                  int comment '父级行政单位',
   `name`                 varchar(255) not null comment '名称',
   `ishot`                bool default 0 comment '是否为热门城市',
   `intro`                varchar(255) default '' comment '介绍',
   primary key (distid)
);

/* 创建经理人表 */
create table `tb_agent`
(
   `agentid`              int not null auto_increment comment '编号',
   `name`                 varchar(255) not null comment '姓名',
   `tel`                  varchar(20) not null comment '电话',
   `servstar`             int not null default 0 comment '满意度星级',
   `realstar`             int not null default 0 comment '真实度星级',
   `profstar`             int not null default 0 comment '专业度星级',
   `certificated`         bool not null default 0 comment '是否持有专业认证',
   primary key (`agentid`)
);

/* 创建用户登录日志表 */
create table `tb_login_log`
(
   `logid`                bigint auto_increment comment '编号',
   `userid`               int not null comment '用户',
   `ipaddr`               varchar(255) not null comment 'IP地址',
   `logdate`              datetime default now() comment '登录时间日期',
   `devcode`              varchar(255) default '' comment '设备代码',
   primary key (`logid`)
);

/* 创建楼盘表 */
create table `tb_estate`
(
   `estateid`             int not null auto_increment comment '编号',
   `distid`               int not null comment '所在三级行政区域',
   `name`                 varchar(255) not null comment '名称',
   `hot`                  int default 0 comment '热度',
   `intro`                varchar(511) default '' comment '介绍',
   primary key (`estateid`)
);

/* 创建经理人楼盘中间表 */
create table `tb_agent_estate`
(
   `agent_estate_id`      int not null auto_increment comment '编号',
   `agentid`              int not null comment '经理人',
   `estateid`             int not null comment '楼盘',
   primary key (`agent_estate_id`)
);

/* 创建户型表 */
create table `tb_house_type`
(
   `typeid`               int comment '编号',
   `name`                 varchar(255) not null comment '名称',
   primary key (`typeid`)
);

/* 创建房源信息表 */
create table `tb_house_info`
(
   `houseid`              int not null auto_increment comment '编号',
   `title`                varchar(50) not null comment '标题',
   `area`                 int not null comment '面积',
   `floor`                int not null comment '楼层',
   `totalfloor`           int not null comment '总楼层',
   `direction`            varchar(10) not null comment '朝向',
   `price`                int not null comment '价格',
   `priceunit`            varchar(10) not null comment '价格单位',
   `detail`               varchar(511) default '' comment '详情',
   `mainphoto`            varchar(255) not null comment '主图',
   `pubdate`              date not null comment '发布日期',
   `street`               varchar(255) not null comment '街道',
   `hassubway`            bool default 0 comment '是否有地铁',
   `isshared`             bool default 0 comment '是否支持合租',
   `hasagentfees`         bool default 0 comment '是否有中介费',
   `typeid`               int not null comment '户型',
   `userid`               int not null comment '发布用户',
   `distid2`              int not null comment '所在二级行政区域',
   `distid3`              int not null comment '所在三级行政区域',
   `estateid`             int comment '楼盘',
   `agentid`              int comment '经理人',
   primary key (`houseid`)
);

/* 创建房源照片表 */
create table `tb_house_photo`
(
   `photoid`              int not null auto_increment comment '编号',
   `houseid`              int not null comment '房源',
   `path`                 varchar(255) not null comment '资源路径',
   primary key (`photoid`)
);

/* 创建标签表 */
create table `tb_tag`
(
   `tagid`                int auto_increment comment '编号',
   `content`              varchar(20) not null comment '内容',
   primary key (`tagid`)
);

/* 创建房源标签中间表 */
create table `tb_house_tag`
(
   `house_tag_id`         int auto_increment comment '编号',
   `houseid`              int not null comment '房源',
   `tagid`                int not null comment '标签',
   primary key (`house_tag_id`)
);


/* 创建用户浏览历史记录表 */
create table `tb_record`
(
   `recordid`             bigint auto_increment comment '编号',
   `userid`               int not null comment '用户',
   `houseid`              int not null comment '房源',
   `recorddate`           datetime not null comment '浏览时间日期',
   primary key (`recordid`)
);

/* 创建用户令牌表 */
create table `tb_user_token`
(
   `tokenid`              int auto_increment comment '编号',
   `token`                char(32) not null comment '令牌',
   `userid`               int not null comment '用户',
   primary key (`tokenid`)
);

/* 创建角色表 */
create table `tb_role`
(
   `roleid`              int auto_increment comment '编号',
   `rolename`            varchar(255) not null comment '角色名',
   primary key (`roleid`)
);

/* 创建权限表 */
create table `tb_privilege`
(
   `privid`               int auto_increment comment '编号',
   `method`               varchar(15) not null comment '请求方法',
   `url`                  varchar(1024) not null comment '资源的URL',
   PRIMARY KEY (`privid`)
);

/* 创建用户角色中间表 */
create table `tb_user_role`
(
   `urid`                 int auto_increment comment '编号',
   `userid`               int not null comment '用户',
   `roleid`               int not null comment '角色',
   primary key (`urid`)
);

/* 创建角色权限中间表 */
create table `tb_role_privilege`
(
   `rpid`                 int auto_increment comment '编号',
   `roleid`               int not null comment '角色',
   `privid`               int not null comment '权限',
   primary key (`rpid`)
);

create unique index `uni_idx_agent_estate` on `tb_agent_estate` (`agentid`, `estateid`);

create unique index `uni_idx_record` on `tb_record` (`userid`, `houseid`);

create unique index `uni_idx_userid` on `tb_user_token` (`userid`);

create unique index `uni_idx_username` on `tb_user` (`username`);

create unique index `uni_idx_tel` on `tb_user` (`tel`);

create unique index `uni_idx_email` on `tb_user` (`email`);

create unique index `uni_idx_house_tag` on `tb_house_tag` (`houseid`, `tagid`);

alter table `tb_agent_estate` add constraint `fk_agent_estate_agentid` foreign key (`agentid`) references `tb_agent` (`agentid`);

alter table `tb_agent_estate` add constraint `fk_agent_estate_estateid` foreign key (`estateid`) references `tb_estate` (`estateid`);

alter table `tb_district` add constraint `fk_district_pid` foreign key (`pid`) references `tb_district` (`distid`);

alter table `tb_estate` add constraint `fk_estate_distid` foreign key (`distid`) references `tb_district` (`distid`);

alter table `tb_house_info` add constraint `fk_house_info_agentid` foreign key (`agentid`) references tb_agent (`agentid`);

alter table `tb_house_info` add constraint `fk_house_info_distid2` foreign key (`distid2`) references tb_district (`distid`);

alter table `tb_house_info` add constraint `fk_house_info_distid3` foreign key (`distid3`) references tb_district (`distid`);

alter table `tb_house_info` add constraint `fk_house_info_estateid` foreign key (`estateid`) references tb_estate (`estateid`);

alter table `tb_house_info` add constraint `fk_house_info_typeid` foreign key (`typeid`) references tb_house_type (`typeid`);

alter table `tb_house_info` add constraint `fk_house_info_userid` foreign key (`userid`) references tb_user (`userid`);

alter table `tb_house_photo` add constraint `fk_house_photo_houseid` foreign key (`houseid`) references `tb_house_info` (`houseid`);

alter table `tb_house_tag` add constraint `fk_house_tag_houseid` foreign key (`houseid`) references `tb_house_info` (`houseid`);

alter table `tb_house_tag` add constraint `fk_house_tag_tagid` foreign key (`tagid`) references `tb_tag` (`tagid`);

alter table `tb_login_log` add constraint `fk_login_log_userid` foreign key (`userid`) references `tb_user` (`userid`);

alter table `tb_record` add constraint `fk_record_houseid` foreign key (`houseid`) references `tb_house_info` (`houseid`);

alter table `tb_record` add constraint `fk_record_userid` foreign key (`userid`) references `tb_user` (`userid`);
			
alter table `tb_user_token` add constraint `fk_token_userid` foreign key (`userid`) references `tb_user` (`userid`);

alter table `tb_user_role` add constraint `uni_user_role` unique (`userid`, `roleid`);

alter table `tb_role_privilege` add constraint `uni_role_priv` unique (`roleid`, `privid`);

alter table `tb_role_privilege` add constraint `fk_role_privilege_privid` foreign key (`privid`) references `tb_privilege` (`privid`);

alter table `tb_role_privilege` add constraint `fk_role_privilege_roleid` foreign key (`roleid`) references `tb_role` (`roleid`);

alter table `tb_user_role` add constraint `fk_user_role_roleid` foreign key (`roleid`) references `tb_role` (`roleid`);

alter table `tb_user_role` add constraint `fk_user_role_userid` foreign key (`userid`) references `tb_user` (`userid`);
