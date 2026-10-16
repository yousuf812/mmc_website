-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: mmc_website
-- ------------------------------------------------------
-- Server version	8.0.46

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=133 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',3,'add_permission'),(6,'Can change permission',3,'change_permission'),(7,'Can delete permission',3,'delete_permission'),(8,'Can view permission',3,'view_permission'),(9,'Can add group',2,'add_group'),(10,'Can change group',2,'change_group'),(11,'Can delete group',2,'delete_group'),(12,'Can view group',2,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Homepage',7,'add_homepage'),(26,'Can change Homepage',7,'change_homepage'),(27,'Can delete Homepage',7,'delete_homepage'),(28,'Can view Homepage',7,'view_homepage'),(29,'Can add Impact Statistic',8,'add_impactstatistic'),(30,'Can change Impact Statistic',8,'change_impactstatistic'),(31,'Can delete Impact Statistic',8,'delete_impactstatistic'),(32,'Can view Impact Statistic',8,'view_impactstatistic'),(33,'Can add Site Settings',9,'add_sitesettings'),(34,'Can change Site Settings',9,'change_sitesettings'),(35,'Can delete Site Settings',9,'delete_sitesettings'),(36,'Can view Site Settings',9,'view_sitesettings'),(37,'Can add Strategic Priority',10,'add_strategicpriority'),(38,'Can change Strategic Priority',10,'change_strategicpriority'),(39,'Can delete Strategic Priority',10,'delete_strategicpriority'),(40,'Can view Strategic Priority',10,'view_strategicpriority'),(41,'Can add Team Member',11,'add_teammember'),(42,'Can change Team Member',11,'change_teammember'),(43,'Can delete Team Member',11,'delete_teammember'),(44,'Can view Team Member',11,'view_teammember'),(45,'Can add Partner',12,'add_partner'),(46,'Can change Partner',12,'change_partner'),(47,'Can delete Partner',12,'delete_partner'),(48,'Can view Partner',12,'view_partner'),(49,'Can add Project',14,'add_project'),(50,'Can change Project',14,'change_project'),(51,'Can delete Project',14,'delete_project'),(52,'Can view Project',14,'view_project'),(53,'Can add SDG',17,'add_sdg'),(54,'Can change SDG',17,'change_sdg'),(55,'Can delete SDG',17,'delete_sdg'),(56,'Can view SDG',17,'view_sdg'),(57,'Can add Delivery Engine',13,'add_deliveryengine'),(58,'Can change Delivery Engine',13,'change_deliveryengine'),(59,'Can delete Delivery Engine',13,'delete_deliveryengine'),(60,'Can view Delivery Engine',13,'view_deliveryengine'),(61,'Can add Project Sector',16,'add_projectsector'),(62,'Can change Project Sector',16,'change_projectsector'),(63,'Can delete Project Sector',16,'delete_projectsector'),(64,'Can view Project Sector',16,'view_projectsector'),(65,'Can add Project Priority',15,'add_projectpriority'),(66,'Can change Project Priority',15,'change_projectpriority'),(67,'Can delete Project Priority',15,'delete_projectpriority'),(68,'Can view Project Priority',15,'view_projectpriority'),(69,'Can add News Article',18,'add_newsarticle'),(70,'Can change News Article',18,'change_newsarticle'),(71,'Can delete News Article',18,'delete_newsarticle'),(72,'Can view News Article',18,'view_newsarticle'),(73,'Can add gallery item',19,'add_galleryitem'),(74,'Can change gallery item',19,'change_galleryitem'),(75,'Can delete gallery item',19,'delete_galleryitem'),(76,'Can view gallery item',19,'view_galleryitem'),(77,'Can add press kit item',20,'add_presskititem'),(78,'Can change press kit item',20,'change_presskititem'),(79,'Can delete press kit item',20,'delete_presskititem'),(80,'Can view press kit item',20,'view_presskititem'),(81,'Can add publication',21,'add_publication'),(82,'Can change publication',21,'change_publication'),(83,'Can delete publication',21,'delete_publication'),(84,'Can view publication',21,'view_publication'),(85,'Can add Engagement Page',22,'add_engagementpage'),(86,'Can change Engagement Page',22,'change_engagementpage'),(87,'Can delete Engagement Page',22,'delete_engagementpage'),(88,'Can view Engagement Page',22,'view_engagementpage'),(89,'Can add job vacancy',23,'add_jobvacancy'),(90,'Can change job vacancy',23,'change_jobvacancy'),(91,'Can delete job vacancy',23,'delete_jobvacancy'),(92,'Can view job vacancy',23,'view_jobvacancy'),(93,'Can add volunteer opportunity',24,'add_volunteeropportunity'),(94,'Can change volunteer opportunity',24,'change_volunteeropportunity'),(95,'Can delete volunteer opportunity',24,'delete_volunteeropportunity'),(96,'Can view volunteer opportunity',24,'view_volunteeropportunity'),(97,'Can add Contact Enquiry',25,'add_contactenquiry'),(98,'Can change Contact Enquiry',25,'change_contactenquiry'),(99,'Can delete Contact Enquiry',25,'delete_contactenquiry'),(100,'Can view Contact Enquiry',25,'view_contactenquiry'),(101,'Can add Contact Settings',26,'add_contactsettings'),(102,'Can change Contact Settings',26,'change_contactsettings'),(103,'Can delete Contact Settings',26,'delete_contactsettings'),(104,'Can view Contact Settings',26,'view_contactsettings'),(105,'Can add About Page',27,'add_aboutpage'),(106,'Can change About Page',27,'change_aboutpage'),(107,'Can delete About Page',27,'delete_aboutpage'),(108,'Can view About Page',27,'view_aboutpage'),(109,'Can add Governance Overview',28,'add_governanceoverview'),(110,'Can change Governance Overview',28,'change_governanceoverview'),(111,'Can delete Governance Overview',28,'delete_governanceoverview'),(112,'Can view Governance Overview',28,'view_governanceoverview'),(113,'Can add Journey Milestone',29,'add_journeymilestone'),(114,'Can change Journey Milestone',29,'change_journeymilestone'),(115,'Can delete Journey Milestone',29,'delete_journeymilestone'),(116,'Can view Journey Milestone',29,'view_journeymilestone'),(117,'Can add Cross-Cutting Commitment',30,'add_crosscuttingcommitment'),(118,'Can change Cross-Cutting Commitment',30,'change_crosscuttingcommitment'),(119,'Can delete Cross-Cutting Commitment',30,'delete_crosscuttingcommitment'),(120,'Can view Cross-Cutting Commitment',30,'view_crosscuttingcommitment'),(121,'Can add What We Do Page',32,'add_whatwedopage'),(122,'Can change What We Do Page',32,'change_whatwedopage'),(123,'Can delete What We Do Page',32,'delete_whatwedopage'),(124,'Can view What We Do Page',32,'view_whatwedopage'),(125,'Can add Priority Action',31,'add_priorityaction'),(126,'Can change Priority Action',31,'change_priorityaction'),(127,'Can delete Priority Action',31,'delete_priorityaction'),(128,'Can view Priority Action',31,'view_priorityaction'),(129,'Can add Tender',33,'add_tender'),(130,'Can change Tender',33,'change_tender'),(131,'Can delete Tender',33,'delete_tender'),(132,'Can view Tender',33,'view_tender');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$1500000$zNLWG6aJlxMjJhsiBwGNGi$nn6GOPkNAz5uEWwfZ7kWMxnq0bS6MvzXjYLNGQVJ+/w=','2026-10-11 15:14:31.521597',1,'admin','','','admin@gmail.com',1,1,'2026-10-09 00:10:41.673319');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact_contactenquiry`
--

DROP TABLE IF EXISTS `contact_contactenquiry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contact_contactenquiry` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `organization` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `subject` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `admin_notes` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_contactenquiry`
--

LOCK TABLES `contact_contactenquiry` WRITE;
/*!40000 ALTER TABLE `contact_contactenquiry` DISABLE KEYS */;
/*!40000 ALTER TABLE `contact_contactenquiry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact_contactsettings`
--

DROP TABLE IF EXISTS `contact_contactsettings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contact_contactsettings` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone_1` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone_2` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `office_address` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `contact_intro` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_contactsettings`
--

LOCK TABLES `contact_contactsettings` WRITE;
/*!40000 ALTER TABLE `contact_contactsettings` DISABLE KEYS */;
INSERT INTO `contact_contactsettings` VALUES (1,'connect@mmcintnl.org','(+254) 728478178','(+252) 618472031','Airport Road, Wadajir District, Mogadishu, Banadir, Somalia','LetΓÇÖs talk about whatΓÇÖs possible. Whether you are a donor, a partner, a volunteer, client, or someone who simply wants to understand our work better, we would love to hear from you.',1,'2026-10-11 15:24:57.552602');
/*!40000 ALTER TABLE `contact_contactsettings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2026-10-10 15:15:17.944705','1','Mission for Meaningful Change',1,'[{\"added\": {}}]',9,1),(2,'2026-10-10 16:07:58.139667','1','From vulnerability to self-reliance',1,'[{\"added\": {}}]',7,1),(3,'2026-10-10 16:09:09.844339','1','1. Protect and Stabilize',1,'[{\"added\": {}}]',10,1),(4,'2026-10-10 16:09:59.155668','2','2. Recover and Build Resilience',1,'[{\"added\": {}}]',10,1),(5,'2026-10-10 16:10:32.803077','3','3. Strengthen Systems and Expand Opportunity',1,'[{\"added\": {}}]',10,1),(6,'2026-10-10 16:11:58.222293','1','17+ - Years of continuous field operations since 2009',1,'[{\"added\": {}}]',8,1),(7,'2026-10-10 16:12:25.774111','2','32 - Independently documented institutional projects',1,'[{\"added\": {}}]',8,1),(8,'2026-10-10 16:12:51.674436','3','13+ - Donor and institutional funding relationships',1,'[{\"added\": {}}]',8,1),(9,'2026-10-10 16:13:17.550594','4','12 of 17 - Sustainable Development Goals contributed to',1,'[{\"added\": {}}]',8,1),(10,'2026-10-10 16:15:04.466309','1','Mrs Asha Ahmed Duale - Board Chair',1,'[{\"added\": {}}]',11,1),(11,'2026-10-10 16:15:45.770357','2','Mr David Ndwiga - Treasurer',1,'[{\"added\": {}}]',11,1),(12,'2026-10-10 16:16:31.783003','3','Mrs Amina Yusuf Ali - Secretary',1,'[{\"added\": {}}]',11,1),(13,'2026-10-10 16:17:08.898139','4','Mr Hassan Barre - Board Member / Strategic Advisor',1,'[{\"added\": {}}]',11,1),(14,'2026-10-10 16:19:31.002495','5','Abdi Issac Mohamed - Founder & Executive Director',1,'[{\"added\": {}}]',11,1),(15,'2026-10-10 16:20:01.089330','6','Abdikani Sheikh Abdirahman - Finance Manager',1,'[{\"added\": {}}]',11,1),(16,'2026-10-10 16:20:32.722022','7','Abdi Mohamed Kheir - Program Manager',1,'[{\"added\": {}}]',11,1),(17,'2026-10-10 16:21:06.013474','8','Mohamed Issack Mohamed - Operations & Compliance Manager',1,'[{\"added\": {}}]',11,1),(18,'2026-10-10 16:21:35.972347','9','Halima Adan Ali - Fundraising & Communications Manager',1,'[{\"added\": {}}]',11,1),(19,'2026-10-10 16:22:11.809989','10','Mr Bashir Jama Hassan - Field Program Coordinator',1,'[{\"added\": {}}]',11,1),(20,'2026-10-11 12:49:06.270030','1','Partner-1',1,'[{\"added\": {}}]',12,1),(21,'2026-10-11 12:49:38.202543','2','Partner-2',1,'[{\"added\": {}}]',12,1),(22,'2026-10-11 12:50:07.800876','3','Partner-3',1,'[{\"added\": {}}]',12,1),(23,'2026-10-11 12:55:24.581868','1','Protect and Stabilize',1,'[{\"added\": {}}]',15,1),(24,'2026-10-11 12:56:44.281239','1','Project-1',1,'[{\"added\": {}}]',14,1),(25,'2026-10-11 12:57:41.858056','2','Recover and Build Resilience',1,'[{\"added\": {}}]',15,1),(26,'2026-10-11 12:58:02.619239','2','Project-2',1,'[{\"added\": {}}]',14,1),(27,'2026-10-11 12:58:50.801397','3','Strengthen Systems and Expand Opportunity',1,'[{\"added\": {}}]',15,1),(28,'2026-10-11 12:59:11.012111','3','Project-3',1,'[{\"added\": {}}]',14,1),(29,'2026-10-11 12:59:53.550871','1','Direct Programme Delivery',1,'[{\"added\": {}}]',13,1),(30,'2026-10-11 13:00:05.668978','2','Technical Consulting',1,'[{\"added\": {}}]',13,1),(31,'2026-10-11 13:00:19.631070','3','Social Enterprise Solutions',1,'[{\"added\": {}}]',13,1),(32,'2026-10-11 13:00:31.493904','4','Policy Advocacy',1,'[{\"added\": {}}]',13,1),(33,'2026-10-11 13:01:17.647784','1','Emergency Cash & Food Assistance',1,'[{\"added\": {}}]',16,1),(34,'2026-10-11 13:01:33.326543','2','Shelter & Settlement',1,'[{\"added\": {}}]',16,1),(35,'2026-10-11 13:01:49.653620','3','Health & Nutrition',1,'[{\"added\": {}}]',16,1),(36,'2026-10-11 13:07:30.779980','1','Volunteer',1,'[{\"added\": {}}]',22,1),(37,'2026-10-11 13:08:02.011681','2','Careers',1,'[{\"added\": {}}]',22,1),(38,'2026-10-11 13:08:27.480500','3','Partnerships',1,'[{\"added\": {}}]',22,1),(39,'2026-10-11 13:08:49.623896','4','Donate & Support',1,'[{\"added\": {}}]',22,1),(40,'2026-10-11 13:09:21.345935','5','Customers / Clients',1,'[{\"added\": {}}]',22,1),(41,'2026-10-11 13:09:40.597405','6','Suppliers & Contractors',1,'[{\"added\": {}}]',22,1),(42,'2026-10-11 13:12:25.397562','6','Suppliers & Contractors',2,'[{\"changed\": {\"fields\": [\"Call to action\"]}}]',22,1),(43,'2026-10-11 13:15:58.210573','1','Who We Are',1,'[{\"added\": {}}]',27,1),(44,'2026-10-11 13:18:32.619627','1','Who We Are',2,'[{\"changed\": {\"fields\": [\"About content\", \"Purpose content\", \"Mission content\", \"Vision content\", \"Commitment content\"]}}]',27,1),(45,'2026-10-11 13:19:46.646853','1','2009 - Foundation',1,'[{\"added\": {}}]',29,1),(46,'2026-10-11 13:20:31.854399','2','2014 - Labour Force Survey',1,'[{\"added\": {}}]',29,1),(47,'2026-10-11 13:21:17.017409','3','2019 - Institutional Scaling',1,'[{\"added\": {}}]',29,1),(48,'2026-10-11 13:22:06.269682','4','2026 - Transition to MMC',1,'[{\"added\": {}}]',29,1),(49,'2026-10-11 13:24:16.664516','1','Governance & Structural Overview',1,'[{\"added\": {}}]',28,1),(50,'2026-10-11 13:27:42.767785','1','What We Do',1,'[{\"added\": {}}]',32,1),(51,'2026-10-11 15:16:08.764002','1','MMC/T/2026/011 ΓÇö Supply of office and IT equipment',1,'[{\"added\": {}}]',33,1),(52,'2026-10-11 15:16:46.431678','2','MMC/T/2026/012 ΓÇö Venue and catering for training workshops',1,'[{\"added\": {}}]',33,1),(53,'2026-10-11 15:17:31.966035','3','MMC/T/2026/013 ΓÇö Independent evaluation consultancy',1,'[{\"added\": {}}]',33,1),(54,'2026-10-11 15:22:17.388747','2','MMC/T/2026/012 ΓÇö Venue and catering for training workshops',2,'[{\"changed\": {\"fields\": [\"Is published\"]}}]',33,1),(55,'2026-10-11 15:22:17.391571','3','MMC/T/2026/013 ΓÇö Independent evaluation consultancy',2,'[{\"changed\": {\"fields\": [\"Is published\"]}}]',33,1),(56,'2026-10-11 15:24:57.554912','1','MMC Contact Settings',1,'[{\"added\": {}}]',26,1),(57,'2026-10-12 00:25:33.901556','1','news-1',1,'[{\"added\": {}}]',18,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(25,'contact','contactenquiry'),(26,'contact','contactsettings'),(5,'contenttypes','contenttype'),(22,'engagement','engagementpage'),(23,'engagement','jobvacancy'),(24,'engagement','volunteeropportunity'),(18,'news','newsarticle'),(27,'pages','aboutpage'),(28,'pages','governanceoverview'),(7,'pages','homepage'),(8,'pages','impactstatistic'),(29,'pages','journeymilestone'),(9,'pages','sitesettings'),(10,'pages','strategicpriority'),(12,'partners','partner'),(30,'projects','crosscuttingcommitment'),(13,'projects','deliveryengine'),(31,'projects','priorityaction'),(14,'projects','project'),(15,'projects','projectpriority'),(16,'projects','projectsector'),(17,'projects','sdg'),(32,'projects','whatwedopage'),(19,'resources','galleryitem'),(20,'resources','presskititem'),(21,'resources','publication'),(6,'sessions','session'),(11,'team','teammember'),(33,'tenders','tender');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2026-10-09 00:09:31.052937'),(2,'auth','0001_initial','2026-10-09 00:09:32.688923'),(3,'admin','0001_initial','2026-10-09 00:09:33.081207'),(4,'admin','0002_logentry_remove_auto_add','2026-10-09 00:09:33.102362'),(5,'admin','0003_logentry_add_action_flag_choices','2026-10-09 00:09:33.125749'),(6,'contenttypes','0002_remove_content_type_name','2026-10-09 00:09:33.480381'),(7,'auth','0002_alter_permission_name_max_length','2026-10-09 00:09:33.680301'),(8,'auth','0003_alter_user_email_max_length','2026-10-09 00:09:33.767774'),(9,'auth','0004_alter_user_username_opts','2026-10-09 00:09:33.801981'),(10,'auth','0005_alter_user_last_login_null','2026-10-09 00:09:34.135402'),(11,'auth','0006_require_contenttypes_0002','2026-10-09 00:09:34.143275'),(12,'auth','0007_alter_validators_add_error_messages','2026-10-09 00:09:34.202929'),(13,'auth','0008_alter_user_username_max_length','2026-10-09 00:09:34.450182'),(14,'auth','0009_alter_user_last_name_max_length','2026-10-09 00:09:34.715936'),(15,'auth','0010_alter_group_name_max_length','2026-10-09 00:09:34.794214'),(16,'auth','0011_update_proxy_permissions','2026-10-09 00:09:34.825373'),(17,'auth','0012_alter_user_first_name_max_length','2026-10-09 00:09:35.086637'),(18,'sessions','0001_initial','2026-10-09 00:09:35.208173'),(19,'pages','0001_initial','2026-10-09 00:49:06.347468'),(20,'team','0001_initial','2026-10-09 00:53:10.747813'),(21,'partners','0001_initial','2026-10-09 00:55:47.000285'),(22,'projects','0001_initial','2026-10-09 01:08:44.979715'),(23,'news','0001_initial','2026-10-09 01:16:16.866203'),(24,'resources','0001_initial','2026-10-09 01:16:17.121067'),(25,'engagement','0001_initial','2026-10-09 01:21:25.882018'),(26,'contact','0001_initial','2026-10-09 01:24:22.044874'),(27,'pages','0002_aboutpage_governanceoverview_journeymilestone','2026-10-09 01:33:10.645868'),(28,'projects','0002_crosscuttingcommitment_whatwedopage_priorityaction','2026-10-09 12:40:09.524937'),(29,'news','0002_alter_newsarticle_slug','2026-10-09 14:47:19.022802'),(30,'resources','0002_alter_publication_slug','2026-10-09 14:47:19.236546'),(31,'tenders','0001_initial','2026-10-10 02:43:33.254659');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('8gih3xuepp04nk4e5ctpbstu69te2pax','.eJxVjDEOwjAMAP_iGUW4dkLakZ03VE7s0AJqpaadEH9HlTrAene6N_SyrUO_VVv6UaEDhNMvS5KfNu1CHzLdZ5fnaV3G5PbEHba626z2uh7t32CQOkAH5KkkL2wlKGVrSdtzKiFGlMRRI2vObeO5QR8iKRIbC9rFMGvAwPD5AvBfN9k:1xFYif:3n_42AEM-0t53t9EsnMSKZApENfczngARn6gW0mrBQ4','2026-10-24 15:10:41.205405'),('en2le6ul5dnboqk5qnb18ignhxnotj14','.eJxVjDEOwjAMAP_iGUW4dkLakZ03VE7s0AJqpaadEH9HlTrAene6N_SyrUO_VVv6UaEDhNMvS5KfNu1CHzLdZ5fnaV3G5PbEHba626z2uh7t32CQOkAH5KkkL2wlKGVrSdtzKiFGlMRRI2vObeO5QR8iKRIbC9rFMGvAwPD5AvBfN9k:1xFvFv:yqQ_CscKDou69zCrfLlBKHt7YitY8M6OpqBARWIWeaQ','2026-10-25 15:14:31.530429');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `engagement_engagementpage`
--

DROP TABLE IF EXISTS `engagement_engagementpage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `engagement_engagementpage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `page_type` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `title` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(220) COLLATE utf8mb4_unicode_ci NOT NULL,
  `short_description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `why_engage` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `process` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `requirements` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `call_to_action` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `call_to_action_url` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `featured_image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image_alt_text` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_published` tinyint(1) NOT NULL,
  `ordering` int unsigned NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `page_type` (`page_type`),
  UNIQUE KEY `slug` (`slug`),
  CONSTRAINT `engagement_engagementpage_chk_1` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `engagement_engagementpage`
--

LOCK TABLES `engagement_engagementpage` WRITE;
/*!40000 ALTER TABLE `engagement_engagementpage` DISABLE KEYS */;
INSERT INTO `engagement_engagementpage` VALUES (1,'volunteer','Volunteer','volunteer','Leave empty for now.','Leave empty for now.','Leave empty for now.','Leave empty for now.','Leave empty for now.','','','','',1,1,'2026-10-11 13:07:30.776417','2026-10-11 13:07:30.776490'),(2,'careers','Careers','careers','Careers','','','','','','','','',1,1,'2026-10-11 13:08:02.010662','2026-10-11 13:08:02.010687'),(3,'partnerships','Partnerships','partnerships','Partnerships','','','','','','','','',1,3,'2026-10-11 13:08:27.479553','2026-10-11 13:08:27.479577'),(4,'donate','Donate & Support','donate-support','Donate & Support','','','','','','','','',1,4,'2026-10-11 13:08:49.621524','2026-10-11 13:08:49.621578'),(5,'clients','Customers / Clients','customers-clients','Customers / Clients','','','','','','','','',1,5,'2026-10-11 13:09:21.344960','2026-10-11 13:09:21.344985'),(6,'suppliers','Suppliers & Contractors','suppliers-contractors','Suppliers & Contractors','','','','','More Info','','','',1,0,'2026-10-11 13:09:40.596219','2026-10-11 13:12:25.385902');
/*!40000 ALTER TABLE `engagement_engagementpage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `engagement_jobvacancy`
--

DROP TABLE IF EXISTS `engagement_jobvacancy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `engagement_jobvacancy` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(220) COLLATE utf8mb4_unicode_ci NOT NULL,
  `department` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `location` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `employment_type` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `responsibilities` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `qualifications` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `experience` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `application_instructions` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `application_email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `application_url` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `closing_date` date DEFAULT NULL,
  `is_open` tinyint(1) NOT NULL,
  `ordering` int unsigned NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  CONSTRAINT `engagement_jobvacancy_chk_1` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `engagement_jobvacancy`
--

LOCK TABLES `engagement_jobvacancy` WRITE;
/*!40000 ALTER TABLE `engagement_jobvacancy` DISABLE KEYS */;
/*!40000 ALTER TABLE `engagement_jobvacancy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `engagement_volunteeropportunity`
--

DROP TABLE IF EXISTS `engagement_volunteeropportunity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `engagement_volunteeropportunity` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(220) COLLATE utf8mb4_unicode_ci NOT NULL,
  `location` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `responsibilities` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `requirements` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `application_instructions` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `application_email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `application_url` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `deadline` date DEFAULT NULL,
  `is_open` tinyint(1) NOT NULL,
  `ordering` int unsigned NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  CONSTRAINT `engagement_volunteeropportunity_chk_1` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `engagement_volunteeropportunity`
--

LOCK TABLES `engagement_volunteeropportunity` WRITE;
/*!40000 ALTER TABLE `engagement_volunteeropportunity` DISABLE KEYS */;
/*!40000 ALTER TABLE `engagement_volunteeropportunity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news_newsarticle`
--

DROP TABLE IF EXISTS `news_newsarticle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `news_newsarticle` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `category` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `excerpt` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `featured_image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image_alt_text` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `author_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `published_at` datetime(6) DEFAULT NULL,
  `is_featured` tinyint(1) NOT NULL,
  `is_published` tinyint(1) NOT NULL,
  `ordering` int unsigned NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  CONSTRAINT `news_newsarticle_chk_1` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news_newsarticle`
--

LOCK TABLES `news_newsarticle` WRITE;
/*!40000 ALTER TABLE `news_newsarticle` DISABLE KEYS */;
INSERT INTO `news_newsarticle` VALUES (1,'news-1','news-1','news','lorem.....','lorem..','','','','2026-10-12 00:25:30.000000',1,1,1,'2026-10-12 00:25:33.899011','2026-10-12 00:25:33.899041');
/*!40000 ALTER TABLE `news_newsarticle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pages_aboutpage`
--

DROP TABLE IF EXISTS `pages_aboutpage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pages_aboutpage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `subtitle` varchar(300) COLLATE utf8mb4_unicode_ci NOT NULL,
  `about_title` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `about_content` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `purpose_title` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `purpose_content` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `mission_title` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `mission_content` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `vision_title` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `vision_content` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `commitment_title` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `commitment_content` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `featured_image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image_alt_text` varchar(300) COLLATE utf8mb4_unicode_ci NOT NULL,
  `organogram_image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `organogram_alt_text` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `organogram_description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_published` tinyint(1) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pages_aboutpage`
--

LOCK TABLES `pages_aboutpage` WRITE;
/*!40000 ALTER TABLE `pages_aboutpage` DISABLE KEYS */;
INSERT INTO `pages_aboutpage` VALUES (1,'Who We Are','One institution. A new legal form. A lasting mission.','About MMC','Mission for Meaningful Change (MMC) is an established Somali humanitarian and development NGO, not a newly founded entity or a start-up. MMC is the direct institutional evolution of Modern Management Company International (MMCI), which operated for 17 years as a registered not-for-profit national consulting entity before formally transitioning, in September 2026, into a registered not-for-profit Humanitarian and Development NGO.\r\n\r\nThis transition changed MMCΓÇÖs legal form and mandate from an entity structured for advisory and technical-service delivery to one structured to directly execute humanitarian and development programming. It did not change the institutionΓÇÖs people, technical expertise, field presence, or values.\r\n\r\nMMCΓÇÖs current capability is built directly on the institutional projects, technical delivery specialisms, and donor and INGO partnerships that MMCI established over 17 years of continuous operations.\r\n\r\nSince 2019, the organisation has significantly scaled its institutional capacity to address acute, climate-induced, and socio-economic vulnerabilities across fragile operating environments in Somalia.','Our Purpose','MMC connects humanitarian action, resilience, systems strengthening, social enterprise, and policy influence to help crisis-affected people and communities move from survival to self-reliance and inclusive prosperity.','Our Mission','Our mission is to work with crisis-affected people and partners to save lives, protect dignity, build resilience, strengthen local systems, create decent work, and advance self-reliance and inclusive prosperity.','Our Vision','Our vision is a peaceful, resilient, and prosperous Somalia where all people can thrive.','Our Commitment','Professional and technically sound.','','','','','',1,'2026-10-11 13:18:32.617516');
/*!40000 ALTER TABLE `pages_aboutpage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pages_governanceoverview`
--

DROP TABLE IF EXISTS `pages_governanceoverview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pages_governanceoverview` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `introduction` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `strategic_governing_tier` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `executive_secretariat` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `field_management` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `reporting_structure` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `governance_note` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_published` tinyint(1) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pages_governanceoverview`
--

LOCK TABLES `pages_governanceoverview` WRITE;
/*!40000 ALTER TABLE `pages_governanceoverview` DISABLE KEYS */;
INSERT INTO `pages_governanceoverview` VALUES (1,'Governance & Structural Overview','Mission for Meaningful Change (MMC) is a locally led national humanitarian and development NGO operating a clear, audit-ready governance and matrix management structure. The organisational design separates long-term strategic oversight from daily executive execution and supports independent fiduciary controls, transparency, and accountable field delivery.','The independent Board of Directors/Trustees holds fiduciary, legal, and statutory accountability for MMC. It exercises oversight through the Finance, Audit and Risk Committee and the Governance and People Committee.','The Board appoints the Executive Director (ED) to handle daily leadership and project execution. The Partnerships, Fundraising and Communications Unit reports directly to the ED to support coordination across the organisation.','The Field Program Coordinator manages and maps activities across the Federal Member States of Somalia under the direct leadership supervision of the Executive Director and coordinated guidance of the central directorates and units.','Field programme personnel report directly to the Directorate of Programmes for technical implementation quality and Monitoring, Evaluation, Accountability, and Learning (MEAL). Field finance and logistics staff maintain a technical reporting line to their respective central Finance and Operations functions.','',1,'2026-10-11 13:24:16.636612');
/*!40000 ALTER TABLE `pages_governanceoverview` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pages_homepage`
--

DROP TABLE IF EXISTS `pages_homepage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pages_homepage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `hero_title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `hero_description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `hero_image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `hero_primary_button_text` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `hero_primary_button_url` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `hero_secondary_button_text` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `hero_secondary_button_url` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `hero_donate_button_text` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `hero_donate_button_url` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `mission_title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `mission_text` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `vision_title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `vision_text` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `closing_cta_title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `closing_cta_text` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `closing_cta_button_text` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `closing_cta_button_url` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pages_homepage`
--

LOCK TABLES `pages_homepage` WRITE;
/*!40000 ALTER TABLE `pages_homepage` DISABLE KEYS */;
INSERT INTO `pages_homepage` VALUES (1,'From vulnerability to self-reliance','We work with crisis-affected people and partners to save lives, protect dignity, build resilience, strengthen local systems, create decent work, advance self-reliance and contribute to inclusive prosperity.','','Explore our work','/our-work/','Partner with MMC','/get-involved/partnerships/','Donate','/get-involved/donate/','Our Mission','','Our Vision','','','','','',1,'2026-10-10 16:07:58.133223');
/*!40000 ALTER TABLE `pages_homepage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pages_impactstatistic`
--

DROP TABLE IF EXISTS `pages_impactstatistic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pages_impactstatistic` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `value` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `label` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `icon` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ordering` int unsigned NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `pages_impactstatistic_chk_1` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pages_impactstatistic`
--

LOCK TABLES `pages_impactstatistic` WRITE;
/*!40000 ALTER TABLE `pages_impactstatistic` DISABLE KEYS */;
INSERT INTO `pages_impactstatistic` VALUES (1,'17+','Years of continuous field operations since 2009','','',1,1),(2,'32','Independently documented institutional projects','','',2,1),(3,'13+','Donor and institutional funding relationships','','',0,1),(4,'12 of 17','Sustainable Development Goals contributed to','','',4,1);
/*!40000 ALTER TABLE `pages_impactstatistic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pages_journeymilestone`
--

DROP TABLE IF EXISTS `pages_journeymilestone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pages_journeymilestone` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `year` int unsigned NOT NULL,
  `title` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `short_description` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image_alt_text` varchar(300) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ordering` int unsigned NOT NULL,
  `is_published` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `pages_journeymilestone_chk_1` CHECK ((`year` >= 0)),
  CONSTRAINT `pages_journeymilestone_chk_2` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pages_journeymilestone`
--

LOCK TABLES `pages_journeymilestone` WRITE;
/*!40000 ALTER TABLE `pages_journeymilestone` DISABLE KEYS */;
INSERT INTO `pages_journeymilestone` VALUES (1,2009,'Foundation','MMCI begins operating as a national technical consultancy in Somalia.','MMCΓÇÖs roots go back to 2009, when its predecessor organisation, Modern Management Company International (MMCI), began operating as a national technical consultancy in Somalia.','','',1,1,'2026-10-11 13:19:46.621754','2026-10-11 13:19:46.621782'),(2,2014,'Labour Force Survey','SomaliaΓÇÖs first official national Labour Force Survey.','MMCI delivered SomaliaΓÇÖs first official national Labour Force Survey for the International Labour Organization in 2014.','','',2,1,'2026-10-11 13:20:31.852970','2026-10-11 13:20:31.852999'),(3,2019,'Institutional Scaling','MMCI significantly scaled its institutional capacity and expanded direct delivery.','By 2019, MMCI had significantly scaled its institutional capacity, moving beyond advisory work to increasingly direct, hands-on delivery for communities affected by displacement, drought, and economic hardship.','','',3,1,'2026-10-11 13:21:17.015954','2026-10-11 13:21:17.015979'),(4,2026,'Transition to MMC','MMCI formally transitions into MMC, a registered not-for-profit humanitarian and development NGO.','In September 2026, MMCI formally transitioned into MMC, a registered not-for-profit humanitarian and development NGO. MMC builds on this operational and technical foundation while expanding its work in humanitarian response, climate resilience, livelihoods, institutional strengthening, social enterprise, and policy advocacy.','','',4,1,'2026-10-11 13:22:06.268040','2026-10-11 13:22:06.268067');
/*!40000 ALTER TABLE `pages_journeymilestone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pages_sitesettings`
--

DROP TABLE IF EXISTS `pages_sitesettings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pages_sitesettings` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `site_name` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tagline` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `logo` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `favicon` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `announcement_enabled` tinyint(1) NOT NULL,
  `announcement_text` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone_1` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone_2` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `address` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `facebook_url` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `linkedin_url` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `youtube_url` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pages_sitesettings`
--

LOCK TABLES `pages_sitesettings` WRITE;
/*!40000 ALTER TABLE `pages_sitesettings` DISABLE KEYS */;
INSERT INTO `pages_sitesettings` VALUES (1,'Mission for Meaningful Change','From vulnerability to self-reliance','site/mmc-logo.jpg','site/favicon.png',1,'MMCI is now MMC: same people, same mission, new legal form','connect@mmcintnl.org','(+254) 728478178','(+252) 618472031','Airport Road, Wadajir District, Mogadishu, Banadir, Somalia','','','',1,'2026-10-10 15:15:17.943189');
/*!40000 ALTER TABLE `pages_sitesettings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pages_strategicpriority`
--

DROP TABLE IF EXISTS `pages_strategicpriority`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pages_strategicpriority` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `number` int unsigned NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `short_description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `full_description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `icon` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `ordering` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `pages_strategicpriority_chk_1` CHECK ((`number` >= 0)),
  CONSTRAINT `pages_strategicpriority_chk_2` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pages_strategicpriority`
--

LOCK TABLES `pages_strategicpriority` WRITE;
/*!40000 ALTER TABLE `pages_strategicpriority` DISABLE KEYS */;
INSERT INTO `pages_strategicpriority` VALUES (1,1,'Protect and Stabilize','Provide timely humanitarian assistance and protection while helping crisis-affected communities stabilize and prepare for recovery.','','','',1,1),(2,2,'Recover and Build Resilience','Support climate resilience, livelihoods, infrastructure, environmental restoration, disaster risk management and social cohesion.','','','',1,2),(3,3,'Strengthen Systems and Expand Opportunity','Strengthen human capital, local organisations, governance, public services, markets, MSMEs, research and systems transformation.','','','',1,3);
/*!40000 ALTER TABLE `pages_strategicpriority` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `partners_partner`
--

DROP TABLE IF EXISTS `partners_partner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `partners_partner` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `partner_type` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `logo` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `website_url` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `accessibility_alt_text` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ordering` int unsigned NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `partners_partner_chk_1` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `partners_partner`
--

LOCK TABLES `partners_partner` WRITE;
/*!40000 ALTER TABLE `partners_partner` DISABLE KEYS */;
INSERT INTO `partners_partner` VALUES (1,'Partner-1','client','Action Against Hunger\r\nConcern Worldwide\r\nCOOPI\r\nSave the Children International\r\nDanish Refugee Council\r\nADRA\r\nPolish Humanitarian Action\r\nSOS ChildrenΓÇÖs Villages\r\nIBTCI\r\nNordic International Support Foundation','','','',1,1,'2026-10-11 12:49:06.235920','2026-10-11 12:49:06.235941'),(2,'Partner-2','client','BRCiS\r\nSoMREP\r\nDanwadaag\r\nUNJPLG','','','',2,1,'2026-10-11 12:49:38.201507','2026-10-11 12:49:38.201531'),(3,'Partner-3','funder','UNDP\r\nUNHCR\r\nEuropean Union\r\nGIZ\r\nSDC\r\nAICS\r\nDFAT\r\nAfrican Development Bank\r\nSida\r\nGovernment of Japan\r\nGovernment of Norway\r\nSomali Stability Fund','','','',3,1,'2026-10-11 12:50:07.799876','2026-10-11 12:50:07.799899');
/*!40000 ALTER TABLE `partners_partner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_crosscuttingcommitment`
--

DROP TABLE IF EXISTS `projects_crosscuttingcommitment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_crosscuttingcommitment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `standard` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `icon` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ordering` int unsigned NOT NULL,
  `is_published` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `projects_crosscuttingcommitment_chk_1` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_crosscuttingcommitment`
--

LOCK TABLES `projects_crosscuttingcommitment` WRITE;
/*!40000 ALTER TABLE `projects_crosscuttingcommitment` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_crosscuttingcommitment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_deliveryengine`
--

DROP TABLE IF EXISTS `projects_deliveryengine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_deliveryengine` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `ordering` int unsigned NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  CONSTRAINT `projects_deliveryengine_chk_1` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_deliveryengine`
--

LOCK TABLES `projects_deliveryengine` WRITE;
/*!40000 ALTER TABLE `projects_deliveryengine` DISABLE KEYS */;
INSERT INTO `projects_deliveryengine` VALUES (1,'Direct Programme Delivery','',1,1),(2,'Technical Consulting','',2,1),(3,'Social Enterprise Solutions','',3,1),(4,'Policy Advocacy','',4,1);
/*!40000 ALTER TABLE `projects_deliveryengine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_priorityaction`
--

DROP TABLE IF EXISTS `projects_priorityaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_priorityaction` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `ordering` int unsigned NOT NULL,
  `is_published` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `priority_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `projects_priorityact_priority_id_1be7b359_fk_pages_str` (`priority_id`),
  CONSTRAINT `projects_priorityact_priority_id_1be7b359_fk_pages_str` FOREIGN KEY (`priority_id`) REFERENCES `pages_strategicpriority` (`id`),
  CONSTRAINT `projects_priorityaction_chk_1` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_priorityaction`
--

LOCK TABLES `projects_priorityaction` WRITE;
/*!40000 ALTER TABLE `projects_priorityaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_priorityaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_project`
--

DROP TABLE IF EXISTS `projects_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_project` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `project_code` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `short_description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `featured_image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image_alt_text` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `location` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `country` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `client_donor` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `project_status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `outcomes` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `impact_summary` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `beneficiaries` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `success_story` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `testimonial` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `testimonial_name` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `testimonial_role` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `video_url` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `baseline_report` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `final_report` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `endline_report` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `predecessor_note` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_featured` tinyint(1) NOT NULL,
  `is_published` tinyint(1) NOT NULL,
  `ordering` int unsigned NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `priority_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `projects_project_priority_id_31c57a01_fk_projects_` (`priority_id`),
  CONSTRAINT `projects_project_priority_id_31c57a01_fk_projects_` FOREIGN KEY (`priority_id`) REFERENCES `projects_projectpriority` (`id`),
  CONSTRAINT `projects_project_chk_1` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_project`
--

LOCK TABLES `projects_project` WRITE;
/*!40000 ALTER TABLE `projects_project` DISABLE KEYS */;
INSERT INTO `projects_project` VALUES (1,'Project-1','project-1','','Lorem.......','','','','','Somalia','',NULL,NULL,'active','','','','','','','','','','','','',1,1,0,'2026-10-11 12:56:44.229881','2026-10-11 12:56:44.229906',1),(2,'Project-2','project-2','','Lorem....','','','','','Somalia','',NULL,NULL,'active','','','','','','','','','','','','',1,1,0,'2026-10-11 12:58:02.610942','2026-10-11 12:58:02.610968',2),(3,'Project-3','project-3','','Lorem...','','','','','Somalia','',NULL,NULL,'active','','','','','','','','','','','','',0,1,0,'2026-10-11 12:59:11.006313','2026-10-11 12:59:11.006333',3);
/*!40000 ALTER TABLE `projects_project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_project_delivery_engines`
--

DROP TABLE IF EXISTS `projects_project_delivery_engines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_project_delivery_engines` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `project_id` bigint NOT NULL,
  `deliveryengine_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `projects_project_deliver_project_id_deliveryengin_f276480a_uniq` (`project_id`,`deliveryengine_id`),
  KEY `projects_project_del_deliveryengine_id_593c1d54_fk_projects_` (`deliveryengine_id`),
  CONSTRAINT `projects_project_del_deliveryengine_id_593c1d54_fk_projects_` FOREIGN KEY (`deliveryengine_id`) REFERENCES `projects_deliveryengine` (`id`),
  CONSTRAINT `projects_project_del_project_id_ac0a9440_fk_projects_` FOREIGN KEY (`project_id`) REFERENCES `projects_project` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_project_delivery_engines`
--

LOCK TABLES `projects_project_delivery_engines` WRITE;
/*!40000 ALTER TABLE `projects_project_delivery_engines` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_project_delivery_engines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_project_sdgs`
--

DROP TABLE IF EXISTS `projects_project_sdgs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_project_sdgs` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `project_id` bigint NOT NULL,
  `sdg_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `projects_project_sdgs_project_id_sdg_id_54a2eca2_uniq` (`project_id`,`sdg_id`),
  KEY `projects_project_sdgs_sdg_id_cc0d5c5f_fk_projects_sdg_id` (`sdg_id`),
  CONSTRAINT `projects_project_sdgs_project_id_5afd4325_fk_projects_project_id` FOREIGN KEY (`project_id`) REFERENCES `projects_project` (`id`),
  CONSTRAINT `projects_project_sdgs_sdg_id_cc0d5c5f_fk_projects_sdg_id` FOREIGN KEY (`sdg_id`) REFERENCES `projects_sdg` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_project_sdgs`
--

LOCK TABLES `projects_project_sdgs` WRITE;
/*!40000 ALTER TABLE `projects_project_sdgs` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_project_sdgs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_project_sectors`
--

DROP TABLE IF EXISTS `projects_project_sectors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_project_sectors` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `project_id` bigint NOT NULL,
  `projectsector_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `projects_project_sectors_project_id_projectsector_77b86ff7_uniq` (`project_id`,`projectsector_id`),
  KEY `projects_project_sec_projectsector_id_972e984f_fk_projects_` (`projectsector_id`),
  CONSTRAINT `projects_project_sec_project_id_7d77096e_fk_projects_` FOREIGN KEY (`project_id`) REFERENCES `projects_project` (`id`),
  CONSTRAINT `projects_project_sec_projectsector_id_972e984f_fk_projects_` FOREIGN KEY (`projectsector_id`) REFERENCES `projects_projectsector` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_project_sectors`
--

LOCK TABLES `projects_project_sectors` WRITE;
/*!40000 ALTER TABLE `projects_project_sectors` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_project_sectors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_projectpriority`
--

DROP TABLE IF EXISTS `projects_projectpriority`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_projectpriority` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `ordering` int unsigned NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  CONSTRAINT `projects_projectpriority_chk_1` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_projectpriority`
--

LOCK TABLES `projects_projectpriority` WRITE;
/*!40000 ALTER TABLE `projects_projectpriority` DISABLE KEYS */;
INSERT INTO `projects_projectpriority` VALUES (1,'Protect and Stabilize','Protect lives, dignity and basic needs while helping crisis-affected communities stabilize.',1,1),(2,'Recover and Build Resilience','Support recovery, climate resilience, livelihoods, infrastructure, environmental restoration and social cohesion.',2,1),(3,'Strengthen Systems and Expand Opportunity','Strengthen systems, human capital, local organisations, governance, markets and inclusive opportunity.',3,1);
/*!40000 ALTER TABLE `projects_projectpriority` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_projectsector`
--

DROP TABLE IF EXISTS `projects_projectsector`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_projectsector` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `ordering` int unsigned NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  CONSTRAINT `projects_projectsector_chk_1` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_projectsector`
--

LOCK TABLES `projects_projectsector` WRITE;
/*!40000 ALTER TABLE `projects_projectsector` DISABLE KEYS */;
INSERT INTO `projects_projectsector` VALUES (1,'Emergency Cash & Food Assistance','',1,1),(2,'Shelter & Settlement','',2,1),(3,'Health & Nutrition','',3,1);
/*!40000 ALTER TABLE `projects_projectsector` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_sdg`
--

DROP TABLE IF EXISTS `projects_sdg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_sdg` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `number` int unsigned NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `icon` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ordering` int unsigned NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `number` (`number`),
  CONSTRAINT `projects_sdg_chk_1` CHECK ((`number` >= 0)),
  CONSTRAINT `projects_sdg_chk_2` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_sdg`
--

LOCK TABLES `projects_sdg` WRITE;
/*!40000 ALTER TABLE `projects_sdg` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_sdg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_whatwedopage`
--

DROP TABLE IF EXISTS `projects_whatwedopage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_whatwedopage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `subtitle` varchar(300) COLLATE utf8mb4_unicode_ci NOT NULL,
  `why_mmc_title` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `why_mmc_content` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `model_title` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model_description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `priorities_intro` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `delivery_intro` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `commitments_title` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `commitments_intro` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_published` tinyint(1) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_whatwedopage`
--

LOCK TABLES `projects_whatwedopage` WRITE;
/*!40000 ALTER TABLE `projects_whatwedopage` DISABLE KEYS */;
INSERT INTO `projects_whatwedopage` VALUES (1,'What We Do','From humanitarian action to resilience, opportunity and self-reliance.','Why MMC Exists','Mission for Meaningful Change (MMC) is an established Somali humanitarian and development NGO and the direct institutional evolution of Modern Management Company International (MMCI), which operated for 17 years as a registered not-for-profit national consulting entity before formally transitioning in September 2026 into a registered not-for-profit Humanitarian and Development NGO.\r\n\r\nMMC exists because people and communities in Somalia face interconnected and recurring pressures, including conflict, insecurity and displacement; droughts, floods, environmental degradation and climate uncertainty; poverty, food insecurity and limited access to essential services; weak or overstretched public systems; limited access to education, skills, decent work, finance and markets; social exclusion and unequal participation in economic, civic and community life; and repeated humanitarian needs and constrained international resources.\r\n\r\nThese pressures reinforce one another. MMC therefore connects immediate humanitarian assistance with the longer-term conditions required for people and communities to recover, adapt, prosper and shape their own future.\r\n\r\nWe exist to save lives, protect dignity, build climate and economic resilience, strengthen local systems, create decent work through social enterprise, and help crisis-affected people and communities in Somalia achieve self-reliance and inclusive prosperity.','The MMC Model of Change 2026-2030','The MMC Model of Change 2026-2030 is a Somalia-rooted, locally led humanitarian-development-peace framework that connects emergency response, climate resilience, livelihoods, peacebuilding, institutional strengthening, social enterprise, and policy influence.\r\n\r\nIt responds to conflict, displacement, climate shocks, poverty, unemployment, weak services, environmental degradation, and constrained humanitarian resources.\r\n\r\nMMC organises its substantive work around three mutually reinforcing strategic priorities. Together, they create a pathway from immediate protection to resilience, stronger systems, expanded opportunity and progressively reduced dependence on repeated humanitarian assistance.\r\n\r\nThe pathway is not rigidly linear. Humanitarian assistance may continue while resilience and systems strengthening are underway; stronger systems can improve emergency response; social enterprise can reinforce employment and service access; and evidence can inform policy.','MMC organises its substantive work around three mutually reinforcing strategic priorities. Together, they connect immediate protection with resilience, stronger systems, expanded opportunity and progressively reduced dependence on repeated humanitarian assistance.','MMC delivers its mission through complementary operational and delivery engines that combine direct programme implementation, technical expertise, social enterprise and evidence-based policy influence.','Cross-Cutting Commitments','MMCΓÇÖs work is guided by cross-cutting commitments that apply across all strategic priorities, delivery and operational engines, and interventions. Together, they ensure that MMCΓÇÖs work is shaped by communities, protects dignity, strengthens capacity, responds to evidence, supports positive behaviour and social change, and contributes to lasting self-reliance.',1,'2026-10-11 13:27:42.732245');
/*!40000 ALTER TABLE `projects_whatwedopage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resources_galleryitem`
--

DROP TABLE IF EXISTS `resources_galleryitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resources_galleryitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `media_type` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `video_file` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `video_url` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `caption` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `alt_text` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `consent_cleared` tinyint(1) NOT NULL,
  `is_published` tinyint(1) NOT NULL,
  `ordering` int unsigned NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `resources_galleryitem_chk_1` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resources_galleryitem`
--

LOCK TABLES `resources_galleryitem` WRITE;
/*!40000 ALTER TABLE `resources_galleryitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `resources_galleryitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resources_presskititem`
--

DROP TABLE IF EXISTS `resources_presskititem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resources_presskititem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `item_type` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `file` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `external_url` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `alt_text` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `consent_cleared` tinyint(1) NOT NULL,
  `is_published` tinyint(1) NOT NULL,
  `ordering` int unsigned NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `resources_presskititem_chk_1` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resources_presskititem`
--

LOCK TABLES `resources_presskititem` WRITE;
/*!40000 ALTER TABLE `resources_presskititem` DISABLE KEYS */;
/*!40000 ALTER TABLE `resources_presskititem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resources_publication`
--

DROP TABLE IF EXISTS `resources_publication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resources_publication` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `cover_image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image_alt_text` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `document` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `access_level` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `published_at` datetime(6) DEFAULT NULL,
  `is_featured` tinyint(1) NOT NULL,
  `is_published` tinyint(1) NOT NULL,
  `ordering` int unsigned NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  CONSTRAINT `resources_publication_chk_1` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resources_publication`
--

LOCK TABLES `resources_publication` WRITE;
/*!40000 ALTER TABLE `resources_publication` DISABLE KEYS */;
/*!40000 ALTER TABLE `resources_publication` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team_teammember`
--

DROP TABLE IF EXISTS `team_teammember`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `team_teammember` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `category` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `photograph` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `academic_qualification` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `technical_background` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `mandate` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `linkedin_url` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `accessibility_alt_text` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `biography` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `ordering` int unsigned NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `team_teammember_chk_1` CHECK ((`ordering` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team_teammember`
--

LOCK TABLES `team_teammember` WRITE;
/*!40000 ALTER TABLE `team_teammember` DISABLE KEYS */;
INSERT INTO `team_teammember` VALUES (1,'Mrs Asha Ahmed Duale','Board Chair','board','','','','','','','',1,1,'2026-10-10 16:15:04.442191','2026-10-10 16:15:04.442294'),(2,'Mr David Ndwiga','Treasurer','board','','','','','','','',2,1,'2026-10-10 16:15:45.768665','2026-10-10 16:15:45.768691'),(3,'Mrs Amina Yusuf Ali','Secretary','board','','','','','','','',0,1,'2026-10-10 16:16:31.781799','2026-10-10 16:16:31.781823'),(4,'Mr Hassan Barre','Board Member / Strategic Advisor','board','','','','','','','',4,1,'2026-10-10 16:17:08.896806','2026-10-10 16:17:08.896865'),(5,'Abdi Issac Mohamed','Founder & Executive Director','management','','','','','','','',0,1,'2026-10-10 16:19:31.000758','2026-10-10 16:19:31.000890'),(6,'Abdikani Sheikh Abdirahman','Finance Manager','management','','','','','','','',0,1,'2026-10-10 16:20:01.088001','2026-10-10 16:20:01.088037'),(7,'Abdi Mohamed Kheir','Program Manager','management','','','','','','','',0,1,'2026-10-10 16:20:32.720021','2026-10-10 16:20:32.720047'),(8,'Mohamed Issack Mohamed','Operations & Compliance Manager','management','','','','','','','',0,1,'2026-10-10 16:21:06.011156','2026-10-10 16:21:06.011178'),(9,'Halima Adan Ali','Fundraising & Communications Manager','management','','','','','','','',0,1,'2026-10-10 16:21:35.971057','2026-10-10 16:21:35.971084'),(10,'Mr Bashir Jama Hassan','Field Program Coordinator','field','','','','','','','',0,1,'2026-10-10 16:22:11.808558','2026-10-10 16:22:11.808599');
/*!40000 ALTER TABLE `team_teammember` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tenders_tender`
--

DROP TABLE IF EXISTS `tenders_tender`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tenders_tender` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `reference` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `category` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `published_date` date NOT NULL,
  `closing_date` date NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `document` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_published` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `reference` (`reference`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tenders_tender`
--

LOCK TABLES `tenders_tender` WRITE;
/*!40000 ALTER TABLE `tenders_tender` DISABLE KEYS */;
INSERT INTO `tenders_tender` VALUES (1,'MMC/T/2026/011','Supply of office and IT equipment','mmct2026011','goods','','2026-10-11','2026-10-31','open','',1,'2026-10-11 15:16:08.761734','2026-10-11 15:16:08.761769'),(2,'MMC/T/2026/012','Venue and catering for training workshops','mmct2026012','services','','2026-10-11','2026-10-24','open','',1,'2026-10-11 15:16:46.430568','2026-10-11 15:22:17.387195'),(3,'MMC/T/2026/013','Independent evaluation consultancy','mmct2026013','consultancy','','2026-10-11','2026-11-13','awarded','',1,'2026-10-11 15:17:31.964915','2026-10-11 15:22:17.390246');
/*!40000 ALTER TABLE `tenders_tender` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-10-12 20:04:19
