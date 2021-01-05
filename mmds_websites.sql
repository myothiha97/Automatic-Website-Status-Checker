-- MySQL dump 10.13  Distrib 8.0.22, for Linux (x86_64)
--
-- Host: localhost    Database: testing_webs
-- ------------------------------------------------------
-- Server version	8.0.22-0ubuntu0.20.04.3

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
-- Table structure for table `dashboards`
--

DROP TABLE IF EXISTS `dashboards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dashboards` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instance` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `user_name` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `destination_url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dashboards`
--

LOCK TABLES `dashboards` WRITE;
/*!40000 ALTER TABLE `dashboards` DISABLE KEYS */;
INSERT INTO `dashboards` VALUES (1,'Carsnet','https://carsnet.com.mm/dashboard/login','admin@admin.com','password','https://carsnet.com.mm/dashboard/login'),(2,'mandalay-capital','http://mandalay-capital-dev.mm-digital-solutions.com/admin','admin','password','https://mandalay-capital-dev.mm-digital-solutions.com/wp-admin/'),(3,'mm-classroom-staging','https://mm-classroom-staging.mm-digital-solutions.com/admin','admin@gmail.com','123456','https://mm-classroom-staging.mm-digital-solutions.com/courses'),(4,'5BB','https://sdm.5bb.com.mm/login','123@gmail.com','abc123456','https://sdm.5bb.com.mm/dashboard/report'),(5,'aml-staging','http://aml-staging.mm-digital-solutions.com/admin/login','admin@admin.com','password','https://aml-staging.mm-digital-solutions.com/admin'),(6,'jewellery-shop-staging','https://js-staging.mm-digital-solutions.com/login','admin@admin.com','admin123','https://js-staging.mm-digital-solutions.com/admin/goldPrices/goldPricesUpdate'),(7,'ywar-taw-staging','https://ywartaw-staging.mm-digital-solutions.com/login','09-123456','password','https://ywartaw-staging.mm-digital-solutions.com/admin'),(8,'gatsby-staging','https://gatsby-dev.mm-digital-solutions.com/admin','admin@admin.com','password','https://gatsby-dev.mm-digital-solutions.com/admin'),(9,'mmtutor-staging','https://dashboard.mmtutors.com/admin','mmtutors@mm-digital-solutions.com','\\#2m.im392tp`s^b^H','https://dashboard.mmtutors.com/admin'),(10,'Joy-production','https://joy.mm-digital-solutions.com/login','admin@admin.com','password','https://joy.mm-digital-solutions.com/admin/dashboard'),(11,'sfa-staging','https://sfa-staging.mm-digital-solutions.com/admin/dashboard','dsm@gmail.com','password','https://sfa-staging.mm-digital-solutions.com/admin/dashboard'),(12,'sfa-dev','https://sfa-dev.mm-digital-solutions.com/admin/dashboard','dsm@gmail.com','password','https://sfa-dev.mm-digital-solutions.com/admin/dashboard'),(13,'mmds-crawler-interface','https://crawler-dev.digi-zaay.com.mm/','admin@carsnet.com.mm','b6kf4iIMH7','https://crawler-dev.digi-zaay.com.mm/home/pages');
/*!40000 ALTER TABLE `dashboards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_pages`
--

DROP TABLE IF EXISTS `home_pages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_pages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instance` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_pages`
--

LOCK TABLES `home_pages` WRITE;
/*!40000 ALTER TABLE `home_pages` DISABLE KEYS */;
INSERT INTO `home_pages` VALUES (1,'Digi-Zaay-Dashboard','https://dev-branding.digi-zaay.com.mm'),(2,'AUKEY','https://aukey-production.mm-digital-solutions.com'),(3,'Carsnet','https://carsnet.com.mm/en/home'),(4,'HOB','https://house-of-bread.mm-digital-solutions.com/en/home'),(5,'A Were Taw','https://aweretaw.com.mm/en/home'),(6,'Quality-eMart','https://quality-emart.digi-zaay.com.mm/en/home'),(7,'mandalay-captial','http://mandalay-capital-dev.mm-digital-solutions.com/'),(8,'mm-classroom-staging','https://mm-classroom-staging.mm-digital-solutions.com/'),(9,'ICT','https://www.ict.com.mm/'),(10,'padc-production','http://padc.com.mm/'),(11,'digi-learning-staging-ubuntu-20-04-lts','https://dev.digi-learn.com.mm/'),(12,'mmds-crawler-interface','https://crawler-dev.digi-zaay.com.mm/'),(13,'Fungry Website','https://fungry.ai/');
/*!40000 ALTER TABLE `home_pages` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-05 14:46:14
