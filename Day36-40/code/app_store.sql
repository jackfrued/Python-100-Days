drop database if exists `app_store`;

create database `app_store` default character set utf8mb4;

use `app_store`;

create table `app_info` (
`id` bigint(20) not null auto_increment comment '自增id, app的id',
`app_name` varchar(255) default '' comment '名称',
`icon_url` varchar(255) default '' comment 'icon地址',
`version` varchar(32) default '' comment '版本号',
`app_size` varchar(32) default '' comment '包大小',
`banner_info` varchar(4096) default '' comment 'banner信息',
`developer_id` varchar(255) default '' comment '开发者id',
`summary` varchar(512) default '' comment '简介',
`app_desc` text comment '详细信息',
`download_url` varchar(255) default '' comment '下载链接',
`price` int(10) default '0' comment '价格，单位：分',
`status` tinyint(4) unsigned default '0' comment '状态，1：待审核，2：审核通过，3，已下线',
`version_desc` varchar(4096) default '' comment '',
`create_time` datetime not null default '0000-00-00 00:00:00' comment '创建时间',
`update_time` datetime not null default '0000-00-00 00:00:00' comment '更新时间',
primary key (`id`)
) engine=innodb auto_increment=100000 default charset=utf8mb4 comment='app基本信息表';

create table `app_ext_info` (
`id` bigint(20) not null auto_increment comment '自增id',
`app_id` bigint(20) not null default '0' comment 'app_id',
`install_count` bigint(20) unsigned not null default '0' comment 'app安装量',
`score` int(10) unsigned not null default '0' comment '评分',
`comment_count` int(10) unsigned not null default '0' comment '评论量',
`create_time` int(10) not null default 0 comment '创建时间',
`update_time` int(10) not null default 0 comment '更新时间',
primary key (`id`)
) engine=innodb default charset=utf8mb4 comment='App扩展信息表';

create table `app_category` (
`id` bigint(20) not null auto_increment comment '自增id',
`parent_id` bigint(20) not null default '0' comment '父分类id',
`name` varchar(64) not null default '' comment '分类名称',
`icon` varchar(512) not null default '' comment 'icon地址',
`category_desc` text comment '分类描述',
`category_level` tinyint(4) unsigned not null default '0' comment '分类级别',
`status` tinyint(4) unsigned not null default '0' comment '当前状态，1：使用中，隐藏',
`display_order` int(10) unsigned not null default '0' comment '排序，值越大越靠前',
`create_time` int(10) not null default 0 comment '创建时间',
`update_time` int(10) not null default 0 comment '更新时间',
primary key (`id`)
) engine=innodb default charset=utf8mb4 comment='分类信息表';

create table `app_category_rel` (
`id` bigint(20) not null auto_increment comment '自增id',
`app_id` bigint(20) not null default '0' comment 'app_id',
`category_id` bigint(20) unsigned not null default '0' comment '最低层分类id',
primary key (`id`),
unique key `idx_category_app` (`category_id`,`app_record_id`),
) engine=innodb default charset=utf8mb4 comment='App和分类关联表';

create table `app_comment` (
`id` bigint(20) not null auto_increment comment '自增id',
`app_id` bigint(20) not null default '0' comment 'app_id',
`title` varchar(255) default '' comment '评论标题',
`content` varchar(2048) default '' comment '评论内容',
`parent_id` bigint(20) default '0' comment '父评论id',
`commenter_uid` bigint(20) default '0' comment '评论用户id',
`commenter_name` varchar(255) default '' comment '评论用户名称',
`commenter_avatar` varchar(255) default '' comment '评论用户头像',
`top_flag` tinyint(4) default '0' comment '是否置顶',
`like_count` int(10) default '0' comment '评论的赞数量',
`status` tinyint(4) default '0' comment '评论状态',
`create_time` int(10) not null default 0 comment '创建时间',
`update_time` int(10) not null default 0 comment '更新时间',
primary key (`id`),
key `idx_app_status` (`app_id`, `status`, `top_flag`)
) engine=innodb default charset=utf8mb4 comment='评论信息表';

create table `user_app_relation` (
`id` bigint(20) not null auto_increment comment '自增id',
`user_id` bigint(20) unsigned not null default '0' comment '用户id',
`app_id` bigint(20) not null default '0' comment 'app_id',
`create_time` int(10) not null default 0 comment '创建时间',
`update_time` int(10) not null default 0 comment '更新时间',
`is_del` tinyint(4) not null default '0' comment '1：删除 0：未删除',
primary key (`id`),
key `idx_user_app` (`user_id`,`app_id`)
) engine=innodb auto_increment=8063 default charset=utf8mb4 comment='用户购买关系表';

create table `bot_score` (
`id` bigint(20) not null auto_increment comment '自增id',
`app_id` bigint(20) not null default '0' comment 'app_id',
`score` int(10) default '0' comment '用户评分',
`commenter_uid` bigint(20) default '0' comment '评分用户id',
`status` tinyint(4) default '0' comment '评分状态',
`create_time` int(10) not null default 0 comment '创建时间',
`update_time` int(10) not null default 0 comment '更新时间',
primary key (`id`),
unique key `idx_uid_score` (`app_id`,`commenter_uid`)
) engine=innodb default charset=utf8mb4 comment='App评分表';