-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: first4
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `Book_id` varchar(7) NOT NULL,
  `Title` varchar(20) DEFAULT NULL,
  `Author` varchar(20) DEFAULT NULL,
  `Subject` varchar(20) DEFAULT NULL,
  `Price` int DEFAULT NULL,
  PRIMARY KEY (`Book_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES ('bk01','Initial Mathamatics','Patra','Mathematics',800),('bk02','Funda of Stats','Matariya','Statistics',800),('bk03','Computer A B C D','Sinha','Computer Science',720),('bk04','Calculas Analysis','Abel','Mathematics',650),('bk05','Maths Analysis','Rudin','Mathematics',330),('bk06','Computer Fundamental','Simona','Computer Science',470);
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `borrower`
--

DROP TABLE IF EXISTS `borrower`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `borrower` (
  `B_id` varchar(5) NOT NULL,
  `B_name` varchar(20) NOT NULL,
  `Addr` varchar(10) DEFAULT NULL,
  `Contact` bigint DEFAULT NULL,
  `Age` int DEFAULT NULL,
  PRIMARY KEY (`B_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrower`
--

LOCK TABLES `borrower` WRITE;
/*!40000 ALTER TABLE `borrower` DISABLE KEYS */;
INSERT INTO `borrower` VALUES ('bo01','Saheb','Kolkata',9847752101,25),('bo02','Smita','Asam',7454845210,30),('bo03','Aman','Kolkata',9899845120,55),('bo04','Kabita','Kolkata',8958412561,45),('bo05','Sima','Krishnagar',8899747152,65),('bo06','Ananta','Bidhanpur',9932254125,20);
/*!40000 ALTER TABLE `borrower` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `borrows`
--

DROP TABLE IF EXISTS `borrows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `borrows` (
  `Book_id` varchar(7) DEFAULT NULL,
  `B_id` varchar(5) DEFAULT NULL,
  `Date_of_issue` date DEFAULT NULL,
  `Date_of_return` date DEFAULT NULL,
  `Fine` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrows`
--

LOCK TABLES `borrows` WRITE;
/*!40000 ALTER TABLE `borrows` DISABLE KEYS */;
INSERT INTO `borrows` VALUES ('bk05','b02','2019-05-14','2019-06-21',31),('bk04','b01','2018-07-14','2018-07-30',9),('bk05','b03','2019-05-14','2019-06-21',62),('bk02','b06','2018-11-22','2019-01-21',53),('bk05','b02','2019-05-15','2019-06-21',30),('bk05','b02','2019-10-19','2019-10-26',0);
/*!40000 ALTER TABLE `borrows` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-13 22:17:37
