-- 交易表
CREATE TABLE `transaction` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_sn` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '交易单号',
  `member_id` bigint(20) NOT NULL COMMENT '交易的用户ID',
  `amount` decimal(8,2) NOT NULL COMMENT '交易金额',
  `integral` int(11) NOT NULL DEFAULT '0' COMMENT '使用的积分',
  `pay_state` tinyint(4) NOT NULL COMMENT '支付类型 0:余额 1:微信 2:支付宝 3:xxx',
  `source` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '支付来源 wx app web wap',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '支付状态 -1：取消 0 未完成 1已完成 -2:异常',
  `completion_time` int(11) NOT NULL COMMENT '交易完成时间',
  `note` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '备注',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `transaction_order_sn_member_id_pay_state_source_status_index` (`order_sn`(191),`member_id`,`pay_state`,`source`(191),`status`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 交易记录表
CREATE TABLE `transaction_record` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_sn` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `events` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '事件详情',
  `result` text COLLATE utf8mb4_unicode_ci COMMENT '结果详情',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- 订单表
CREATE TABLE `order` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_no` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '订单编号',
  `order_sn` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '交易号',
  `member_id` int(11) NOT NULL COMMENT '客户编号',
  `supplier_id` int(11) NOT NULL COMMENT '商户编码',
  `supplier_name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '商户名称',
  `order_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '订单状态 0未付款,1已付款,2已发货,3已签收,-1退货申请,-2退货中,-3已退货,-4取消交易',
  `after_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '用户售后状态 0 未发起售后 1 申请售后 -1 售后已取消 2 处理中 200 处理完毕',
  `product_count` int(11) NOT NULL DEFAULT '0' COMMENT '商品数量',
  `product_amount_total` decimal(12,4) NOT NULL COMMENT '商品总价',
  `order_amount_total` decimal(12,4) NOT NULL DEFAULT '0.0000' COMMENT '实际付款金额',
  `logistics_fee` decimal(12,4) NOT NULL COMMENT '运费金额',
  `address_id` int(11) NOT NULL COMMENT '收货地址编码',
  `pay_channel` tinyint(4) NOT NULL DEFAULT '0' COMMENT '支付渠道 0余额 1微信 2支付宝',
  `out_trade_no` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '订单支付单号',
  `escrow_trade_no` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '第三方支付流水号',
  `pay_time` int(11) NOT NULL DEFAULT '0' COMMENT '付款时间',
  `delivery_time` int(11) NOT NULL DEFAULT '0' COMMENT '发货时间',
  `order_settlement_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '订单结算状态 0未结算 1已结算',
  `order_settlement_time` int(11) NOT NULL DEFAULT '0' COMMENT '订单结算时间',
  `is_package` enum('0','1') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '0' COMMENT '是否是套餐',
  `is_integral` enum('0','1') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '0' COMMENT '是否是积分产品',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_order_sn_unique` (`order_sn`),
  KEY `order_order_sn_member_id_order_status_out_trade_no_index` (`order_sn`,`member_id`,`order_status`,`out_trade_no`(191))
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 售后申请表
CREATE TABLE `order_returns_apply` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_no` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '订单单号',
  `order_detail_id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '子订单编码',
  `return_no` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '售后单号',
  `member_id` int(11) NOT NULL COMMENT '用户编码',
  `state` tinyint(4) NOT NULL COMMENT '类型 0 仅退款 1退货退款',
  `product_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '货物状态 0:已收到货 1:未收到货',
  `why` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '退换货原因',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '审核状态 -1 拒绝 0 未审核 1审核通过',
  `audit_time` int(11) NOT NULL DEFAULT '0' COMMENT '审核时间',
  `audit_why` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '审核原因',
  `note` text COLLATE utf8mb4_unicode_ci COMMENT '备注',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 售后记录表
CREATE TABLE `order_returns` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `returns_no` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '退货编号 供客户查询',
  `order_id` int(11) NOT NULL COMMENT '订单编号',
  `express_no` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '物流单号',
  `consignee_realname` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '收货人姓名',
  `consignee_telphone` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '联系电话',
  `consignee_telphone2` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '备用联系电话',
  `consignee_address` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '收货地址',
  `consignee_zip` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '邮政编码',
  `logistics_type` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '物流方式',
  `logistics_fee` decimal(12,2) NOT NULL COMMENT '物流发货运费',
  `order_logistics_status` int(11) DEFAULT NULL COMMENT '物流状态',
  `logistics_settlement_status` int(11) DEFAULT NULL COMMENT '物流结算状态',
  `logistics_result_last` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '物流最后状态描述',
  `logistics_result` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '物流描述',
  `logistics_create_time` int(11) DEFAULT NULL COMMENT '发货时间',
  `logistics_update_time` int(11) DEFAULT NULL COMMENT '物流更新时间',
  `logistics_settlement_time` int(11) DEFAULT NULL COMMENT '物流结算时间',
  `returns_type` tinyint(4) NOT NULL DEFAULT '0' COMMENT '0全部退单 1部分退单',
  `handling_way` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'PUPAWAY:退货入库;REDELIVERY:重新发货;RECLAIM-REDELIVERY:不要求归还并重新发货; REFUND:退款; COMPENSATION:不退货并赔偿',
  `returns_amount` decimal(8,2) NOT NULL COMMENT '退款金额',
  `return_submit_time` int(11) NOT NULL COMMENT '退货申请时间',
  `handling_time` int(11) NOT NULL COMMENT '退货处理时间',
  `remark` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '退货原因',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 评价表
CREATE TABLE `order_appraise` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL COMMENT '订单编码',
  `info` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '评论内容',
  `level` enum('-1','0','1') COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '级别 -1差评 0中评 1好评',
  `desc_star` tinyint(4) NOT NULL COMMENT '描述相符 1-5',
  `logistics_star` tinyint(4) NOT NULL COMMENT '物流服务 1-5',
  `attitude_star` tinyint(4) NOT NULL COMMENT '服务态度 1-5',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `order_appraise_order_id_index` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;