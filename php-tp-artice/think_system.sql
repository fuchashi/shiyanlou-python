/*
Navicat MySQL Data Transfer

Source Server         : xampp
Source Server Version : 100113
Source Host           : localhost:3306
Source Database       : think_system

Target Server Type    : MYSQL
Target Server Version : 100113
File Encoding         : 65001

Date: 2016-08-25 16:48:07
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for think_article
-- ----------------------------
DROP TABLE IF EXISTS `think_article`;
CREATE TABLE `think_article` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL DEFAULT '',
  `tagid` int(11) unsigned NOT NULL,
  `uid` int(11) unsigned NOT NULL DEFAULT '0',
  `publish` int(11) NOT NULL DEFAULT '0',
  `hits` int(11) unsigned NOT NULL DEFAULT '0',
  `content` text,
  `image` varchar(200) NOT NULL,
  `likes` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `title_name` (`title`) USING BTREE,
  KEY `tag_id` (`tagid`),
  KEY `user_id` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for think_comment
-- ----------------------------
DROP TABLE IF EXISTS `think_comment`;
CREATE TABLE `think_comment` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `pid` int(11) unsigned NOT NULL DEFAULT '0',
  `uid` int(11) NOT NULL DEFAULT '0',
  `aid` int(11) unsigned NOT NULL DEFAULT '0',
  `time` int(11) NOT NULL,
  `content` varchar(255) NOT NULL DEFAULT '',
  `reply_num` tinyint(4) unsigned NOT NULL DEFAULT '0',
  `ip` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `p_id` (`pid`),
  KEY `a_id` (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for think_like
-- ----------------------------
DROP TABLE IF EXISTS `think_like`;
CREATE TABLE `think_like` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `uid` int(11) unsigned DEFAULT '0',
  `aid` int(11) unsigned DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY ` article_id_like` (`aid`),
  KEY `user_id_like` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for think_log
-- ----------------------------
DROP TABLE IF EXISTS `think_log`;
CREATE TABLE `think_log` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `time` int(11) NOT NULL DEFAULT '0',
  `loginfo` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for think_session
-- ----------------------------
DROP TABLE IF EXISTS `think_session`;
CREATE TABLE `think_session` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL DEFAULT '0',
  `sessionid` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for think_tags
-- ----------------------------
DROP TABLE IF EXISTS `think_tags`;
CREATE TABLE `think_tags` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `tagname` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for think_user
-- ----------------------------
DROP TABLE IF EXISTS `think_user`;
CREATE TABLE `think_user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(20) NOT NULL,
  `birthday` int(11) NOT NULL DEFAULT '0',
  `gender` enum('2','1','0') NOT NULL DEFAULT '0' COMMENT '性别:0->未知,1->男,2->女',
  `login_count` int(11) unsigned NOT NULL DEFAULT '0',
  `ip` int(11) unsigned DEFAULT '0',
  `status` enum('1','0') NOT NULL DEFAULT '0',
  `imgpath` varchar(50) NOT NULL DEFAULT '',
  `createtime` int(11) unsigned NOT NULL DEFAULT '0',
  `last_login_time` int(11) unsigned NOT NULL DEFAULT '1',
  `last_login_ip` int(11) NOT NULL DEFAULT '0',
  `time` int(11) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`,`username`),
  UNIQUE KEY `user_name` (`username`) USING BTREE,
  KEY `email_sear` (`email`) USING BTREE,
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
SET FOREIGN_KEY_CHECKS=1;
