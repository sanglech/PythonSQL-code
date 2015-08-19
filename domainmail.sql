-- MySQL dump 10.13  Distrib 5.6.26, for osx10.8 (x86_64)
--
-- Host: localhost    Database: domainmail
-- ------------------------------------------------------
-- Server version	5.6.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `domainaddr`
--

DROP TABLE IF EXISTS `domainaddr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `domainaddr` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mailaddr` varchar(255) NOT NULL,
  `domainname` varchar(255) NOT NULL,
  `datecreated` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `domainaddr`
--

LOCK TABLES `domainaddr` WRITE;
/*!40000 ALTER TABLE `domainaddr` DISABLE KEYS */;
INSERT INTO `domainaddr` VALUES (1,'a@gmail.com','gmail','2015-01-15'),(2,'b@gmail.com','gmail','2015-08-15'),(3,'c@gmail.com','gmail','2015-08-01'),(4,'d@hotmail.com','hotmail','1999-01-01'),(5,'e@hotmail.com','hotmail','2002-07-01'),(6,'f@sql.com','sql','2013-10-15'),(7,'g@sql.com','sql','2015-08-18'),(8,'h@sql.com','sql','2015-08-01'),(9,'i@sql.com','sql','2015-08-10'),(10,'j@gmail.com','gmail','2015-07-15'),(11,'k@gmail.com','gmail','2014-08-20');
/*!40000 ALTER TABLE `domainaddr` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mailing`
--

DROP TABLE IF EXISTS `mailing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mailing` (
  `addr` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mailing`
--

LOCK TABLES `mailing` WRITE;
/*!40000 ALTER TABLE `mailing` DISABLE KEYS */;
INSERT INTO `mailing` VALUES ('a@gmail.com'),('b@gmail.com'),('c@gmail.com'),('e@hotmail.com'),('d@hotmail.com'),('f@sql.com'),('g@sql.com'),('h@sql.com'),('i@sql.com'),('j@gmail.com'),('k@gmail.com');
/*!40000 ALTER TABLE `mailing` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-08-18 19:09:25
