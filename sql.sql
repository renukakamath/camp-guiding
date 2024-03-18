/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - camp_guiding
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`camp_guiding` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `camp_guiding`;

/*Table structure for table `age_category` */

DROP TABLE IF EXISTS `age_category`;

CREATE TABLE `age_category` (
  `age_category_id` int(11) NOT NULL AUTO_INCREMENT,
  `age_category` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`age_category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `age_category` */

insert  into `age_category`(`age_category_id`,`age_category`) values 
(1,'dfdf');

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `photographer_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`booking_id`,`user_id`,`photographer_id`,`amount`,`date`,`status`) values 
(1,1,1,'		1000	','2024-03-07','pending'),
(2,1,1,'	120		','2024-03-07','pending'),
(3,1,1,'0','2024-03-07','paid');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `receiver_id` int(11) DEFAULT NULL,
  `msg` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`sender_id`,`receiver_id`,`msg`,`date`) values 
(1,1,3,'hai','2024-03-04 21:15:15'),
(2,1,3,'hello','2024-03-04 21:15:15'),
(3,1,3,'hai','2024-03-04 21:15:55'),
(4,3,1,'hai','2024-03-04 21:15:55'),
(5,3,1,'hia','2024-03-04 21:39:01'),
(6,5,1,'hai','2024-03-07'),
(7,5,1,'hai','2024-03-07'),
(8,5,1,'hai','2024-03-07'),
(9,5,1,'hello','2024-03-07'),
(10,3,5,'hai','2024-03-07 12:28:25'),
(11,3,5,'hello','2024-03-07 12:28:28'),
(12,5,1,'hai','2024-03-07'),
(13,5,1,'hello','2024-03-07'),
(14,5,1,'hello','2024-03-07'),
(15,5,1,'hello','2024-03-07'),
(16,5,1,'hello','2024-03-07'),
(17,5,1,'good','2024-03-07'),
(18,5,3,'hello','2024-03-07');

/*Table structure for table `competition` */

DROP TABLE IF EXISTS `competition`;

CREATE TABLE `competition` (
  `competition_id` int(11) NOT NULL AUTO_INCREMENT,
  `age_category_id` int(11) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `competition_date` varchar(100) DEFAULT NULL,
  `venu` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`competition_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `competition` */

insert  into `competition`(`competition_id`,`age_category_id`,`title`,`description`,`competition_date`,`venu`,`date`,`status`) values 
(3,1,'klsdjass','needed','2024-03-23','ssafaf','2024-03-04','pending');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`sender_id`,`description`,`reply`,`date`) values 
(1,1,'dffdsf','pending','2024-03-04'),
(2,1,'dfsdfsd','pending','2024-03-04'),
(3,1,'jdjkasd','ok','2024-03-04'),
(4,1,'ddas','pending','2024-03-04'),
(5,5,'good','pending','2024-03-07 13:26:24'),
(6,5,'gff','pending','2024-03-07 13:26:29');

/*Table structure for table `experts` */

DROP TABLE IF EXISTS `experts`;

CREATE TABLE `experts` (
  `experts_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`experts_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `experts` */

insert  into `experts`(`experts_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values 
(1,1,'jùjú','sea','jhwkj','2345678904','kjsjdksa@gmail.com');

/*Table structure for table `intership` */

DROP TABLE IF EXISTS `intership`;

CREATE TABLE `intership` (
  `intership_id` int(11) NOT NULL AUTO_INCREMENT,
  `experts_id` int(11) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`intership_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `intership` */

insert  into `intership`(`intership_id`,`experts_id`,`title`,`description`,`amount`,`date`,`status`) values 
(2,1,'klsdjass','needed','5001','2024-03-04','pending');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `user_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`user_type`) values 
(1,'expert','expert','expert'),
(3,'photo','photo','photo'),
(4,'admin','admin','admin'),
(5,'hello','hello','User'),
(6,'hai','hai','user'),
(7,'user','user','user'),
(8,'user','user','user'),
(9,'user','user','user'),
(10,'user','user','user'),
(11,'user','user','user'),
(12,'user','user','user'),
(13,'user','user','user');

/*Table structure for table `newproduct_techonology` */

DROP TABLE IF EXISTS `newproduct_techonology`;

CREATE TABLE `newproduct_techonology` (
  `product_techonology_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`product_techonology_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `newproduct_techonology` */

insert  into `newproduct_techonology`(`product_techonology_id`,`title`,`description`,`image`) values 
(2,'klsdjass','needed','static/dd826837-05cf-42d4-a36b-9379bb1bf34129d5b283-2f28-4bcc-b7a1-10827124629b64bcac22-a0c0-48b7-9e7c-271184f72e48abc.jpg');

/*Table structure for table `order_child` */

DROP TABLE IF EXISTS `order_child`;

CREATE TABLE `order_child` (
  `order_child_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_master_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`order_child_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `order_child` */

insert  into `order_child`(`order_child_id`,`order_master_id`,`product_id`,`quantity`,`amount`) values 
(1,1,3,'2','800'),
(2,2,3,'9','3600');

/*Table structure for table `order_master` */

DROP TABLE IF EXISTS `order_master`;

CREATE TABLE `order_master` (
  `order_master_id` int(11) NOT NULL AUTO_INCREMENT,
  `photographer_id` int(11) DEFAULT NULL,
  `total_amount` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`order_master_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `order_master` */

insert  into `order_master`(`order_master_id`,`photographer_id`,`total_amount`,`date`,`status`) values 
(1,1,800,'2024-03-04','Paid'),
(2,1,3600,'2024-03-04','Paid');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `payment_for_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`payment_for_id`,`amount`,`date`) values 
(1,1,'800','2024-03-04'),
(2,2,'3600','2024-03-04');

/*Table structure for table `photographer` */

DROP TABLE IF EXISTS `photographer`;

CREATE TABLE `photographer` (
  `photographer_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`photographer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `photographer` */

insert  into `photographer`(`photographer_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values 
(1,3,'p','hai','ernakaulams','2345678907','renukakamath2@gmail.com');

/*Table structure for table `phpayment` */

DROP TABLE IF EXISTS `phpayment`;

CREATE TABLE `phpayment` (
  `phpayment` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`phpayment`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `phpayment` */

insert  into `phpayment`(`phpayment`,`booking_id`,`amount`,`date`,`status`) values 
(1,1,'500','2024-03-07 13:25:50','paid'),
(2,3,'100','2024-03-07 13:35:35','paid');

/*Table structure for table `product_category` */

DROP TABLE IF EXISTS `product_category`;

CREATE TABLE `product_category` (
  `product_category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`product_category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `product_category` */

insert  into `product_category`(`product_category_id`,`category_name`) values 
(3,'hjgjhkj');

/*Table structure for table `products` */

DROP TABLE IF EXISTS `products`;

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_category_id` int(11) DEFAULT NULL,
  `product_name` varchar(100) DEFAULT NULL,
  `quality` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `products` */

insert  into `products`(`product_id`,`product_category_id`,`product_name`,`quality`,`amount`,`status`) values 
(3,3,'kjuik','1','400','rent'),
(4,3,'kjuik','2','400','sale');

/*Table structure for table `proposal` */

DROP TABLE IF EXISTS `proposal`;

CREATE TABLE `proposal` (
  `proposal_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`proposal_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `proposal` */

insert  into `proposal`(`proposal_id`,`booking_id`,`amount`,`date`,`status`) values 
(1,3,'500','2024-03-07','paid'),
(2,1,'501','2024-03-07','pending'),
(3,3,'100','2024-03-07','paid');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `photographer_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`request`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`request`,`product_id`,`photographer_id`,`date`,`status`) values 
(1,3,1,'2024-03-04','pending');

/*Table structure for table `scholarship` */

DROP TABLE IF EXISTS `scholarship`;

CREATE TABLE `scholarship` (
  `scholarship_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`scholarship_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `scholarship` */

insert  into `scholarship`(`scholarship_id`,`title`,`description`,`date`,`status`) values 
(1,'klsdjass','needed','2024-03-04','pending');

/*Table structure for table `tutorials` */

DROP TABLE IF EXISTS `tutorials`;

CREATE TABLE `tutorials` (
  `tutorials_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_techonology_id` int(11) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `video` varchar(100) DEFAULT NULL,
  `youtube_link` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`tutorials_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `tutorials` */

insert  into `tutorials`(`tutorials_id`,`product_techonology_id`,`title`,`video`,`youtube_link`) values 
(2,2,'klsdjass','static/fcbd0101-e066-4620-a180-0011272ea5bcpexels-tima-miroshnichenko-6201055-3840x2160-25fps.mp4','needed');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values 
(1,5,'hai','bab','plce','1234567890','re@gmail.com'),
(2,8,'hai','bab','plce','1234567890','re@gmail.com'),
(3,9,'hai','bab','plce','1234567890','re@gmail.com'),
(4,10,'hai','bab','plce','1234567890','re@gmail.com'),
(5,11,'hai','bab','plce','1234567890','re@gmail.com'),
(6,12,'hai','bab','plce','1234567890','re@gmail.com'),
(7,13,'hai','bab','plce','1234567890','re@gmail.com');

/*Table structure for table `works` */

DROP TABLE IF EXISTS `works`;

CREATE TABLE `works` (
  `works_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `caption` varchar(100) DEFAULT NULL,
  `file` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`works_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `works` */

insert  into `works`(`works_id`,`sender_id`,`caption`,`file`,`date`) values 
(2,1,'		lkfidslfa	','static/5a38dce6-fd35-4541-b534-2b25e0b0ff1bscott-webb-oRWRlTgBrPo-unsplash (2).jpg','2024-03-04'),
(4,1,'			ddsas','static/6c55cf99-aff5-474a-aa6f-ab63ef694453scott-graham-5fNmWej4tAA-unsplash.jpg','2024-03-04');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
