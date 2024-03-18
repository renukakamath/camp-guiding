/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - online_crime
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`online_crime` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `online_crime`;

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `station_id` int(11) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `datetime` datetime DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

LOCK TABLES `complaints` WRITE;

insert  into `complaints`(`complaint_id`,`user_id`,`station_id`,`description`,`datetime`,`status`) values (1,1,1,'Complaint1','2020-03-05 09:03:58','solved');

UNLOCK TABLES;

/*Table structure for table `crime_type` */

DROP TABLE IF EXISTS `crime_type`;

CREATE TABLE `crime_type` (
  `crime_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `crime_type_name` varchar(50) DEFAULT NULL,
  `minimum_penalty` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`crime_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `crime_type` */

LOCK TABLES `crime_type` WRITE;

insert  into `crime_type`(`crime_type_id`,`crime_type_name`,`minimum_penalty`) values (1,'Antisocial Behaviour','100000');

UNLOCK TABLES;

/*Table structure for table `crimes` */

DROP TABLE IF EXISTS `crimes`;

CREATE TABLE `crimes` (
  `crime_id` int(11) NOT NULL AUTO_INCREMENT,
  `station_id` int(11) DEFAULT NULL,
  `crime_type_id` int(11) DEFAULT NULL,
  `crime_title` varchar(50) DEFAULT NULL,
  `crime_description` varchar(100) DEFAULT NULL,
  `date_time_occurred` varchar(100) DEFAULT NULL,
  `date_time_reported` varchar(100) DEFAULT NULL,
  `crime_status` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `image` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`crime_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `crimes` */

LOCK TABLES `crimes` WRITE;

insert  into `crimes`(`crime_id`,`station_id`,`crime_type_id`,`crime_title`,`crime_description`,`date_time_occurred`,`date_time_reported`,`crime_status`,`place`,`district`,`image`) values (1,1,1,'as','asdds','01:00','01:00','crime','Kochi','Eranakulam','static/uploads/8f55b4ad-2915-4250-8b64-439d0f75eee0500_F_275093125_8TiaxOAX0dpPiC5LhVzm82rBelTXZqdY.jpg');

UNLOCK TABLES;

/*Table structure for table `criminals` */

DROP TABLE IF EXISTS `criminals`;

CREATE TABLE `criminals` (
  `criminal_id` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `photo` varchar(500) DEFAULT NULL,
  `thumb_impression` varchar(50) DEFAULT NULL,
  `identify_mark_1` varchar(50) DEFAULT NULL,
  `identify_mark_2` varchar(50) DEFAULT NULL,
  `house_name` varchar(50) DEFAULT NULL,
  `father_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`criminal_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `criminals` */

LOCK TABLES `criminals` WRITE;

insert  into `criminals`(`criminal_id`,`fname`,`lname`,`gender`,`dob`,`photo`,`thumb_impression`,`identify_mark_1`,`identify_mark_2`,`house_name`,`father_name`,`place`,`district`) values (1,'Govind','gs','male','1973-09-25','static/uploads/37ebcf84-c33a-43ba-9f34-eef6cf5d5c2aabd.jpg','as','as1','as1','as','asas','ass','as');

UNLOCK TABLES;

/*Table structure for table `evidences` */

DROP TABLE IF EXISTS `evidences`;

CREATE TABLE `evidences` (
  `evidence_id` int(11) NOT NULL AUTO_INCREMENT,
  `complaint_id` int(11) DEFAULT NULL,
  `file_path` varchar(500) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `datetime` datetime DEFAULT NULL,
  PRIMARY KEY (`evidence_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `evidences` */

LOCK TABLES `evidences` WRITE;

insert  into `evidences`(`evidence_id`,`complaint_id`,`file_path`,`description`,`datetime`) values (3,1,'static/uploads/d7e8f8fb-4bfd-4d3d-a8b3-f71b89f5300fasw.jpg','			asas','2020-03-05 00:00:00');

UNLOCK TABLES;

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `feed_description` varchar(200) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `datetime` datetime DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

LOCK TABLES `feedback` WRITE;

insert  into `feedback`(`feedback_id`,`user_id`,`feed_description`,`reply`,`datetime`) values (1,1,'Feedback1','Sample1','2020-03-05 09:04:42');

UNLOCK TABLES;

/*Table structure for table `found_report` */

DROP TABLE IF EXISTS `found_report`;

CREATE TABLE `found_report` (
  `found_id` int(11) NOT NULL AUTO_INCREMENT,
  `criminal_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `datetime` datetime DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`found_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `found_report` */

LOCK TABLES `found_report` WRITE;

UNLOCK TABLES;

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

LOCK TABLES `login` WRITE;

insert  into `login`(`log_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'police','Police123','station');

UNLOCK TABLES;

/*Table structure for table `message` */

DROP TABLE IF EXISTS `message`;

CREATE TABLE `message` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `message_description` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `datetime` datetime DEFAULT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `message` */

LOCK TABLES `message` WRITE;

UNLOCK TABLES;

/*Table structure for table `stations` */

DROP TABLE IF EXISTS `stations`;

CREATE TABLE `stations` (
  `station_id` int(11) NOT NULL AUTO_INCREMENT,
  `log_id` int(11) DEFAULT NULL,
  `station_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `pincode` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `fax_no` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`station_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `stations` */

LOCK TABLES `stations` WRITE;

insert  into `stations`(`station_id`,`log_id`,`station_name`,`place`,`district`,`pincode`,`phone`,`email`,`fax_no`) values (1,2,'Aluvapolice','Kochi','Eranakulam','690890','9656323079','as@asd.as','1234567890');

UNLOCK TABLES;

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `log_id` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `hname` varchar(100) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `pincode` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `users` */

LOCK TABLES `users` WRITE;

insert  into `users`(`user_id`,`log_id`,`fname`,`lname`,`hname`,`place`,`pincode`,`phone`,`email`) values (1,3,'Bency','Baby','Modiyil','Kollakaadavu','690509','9656323878','as@asd.as');

UNLOCK TABLES;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
