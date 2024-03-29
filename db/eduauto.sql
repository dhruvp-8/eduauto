-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 31, 2018 at 08:01 PM
-- Server version: 10.1.29-MariaDB
-- PHP Version: 7.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `eduauto`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add ea attendance', 7, 'add_eaattendance'),
(20, 'Can change ea attendance', 7, 'change_eaattendance'),
(21, 'Can delete ea attendance', 7, 'delete_eaattendance'),
(22, 'Can add ea student details', 8, 'add_eastudentdetails'),
(23, 'Can change ea student details', 8, 'change_eastudentdetails'),
(24, 'Can delete ea student details', 8, 'delete_eastudentdetails'),
(25, 'Can add ea teacher details', 9, 'add_eateacherdetails'),
(26, 'Can change ea teacher details', 9, 'change_eateacherdetails'),
(27, 'Can delete ea teacher details', 9, 'delete_eateacherdetails'),
(28, 'Can add ea user mapping', 10, 'add_eausermapping'),
(29, 'Can change ea user mapping', 10, 'change_eausermapping'),
(30, 'Can delete ea user mapping', 10, 'delete_eausermapping'),
(31, 'Can add ea academic history', 11, 'add_eaacademichistory'),
(32, 'Can change ea academic history', 11, 'change_eaacademichistory'),
(33, 'Can delete ea academic history', 11, 'delete_eaacademichistory'),
(34, 'Can add ea news comments', 12, 'add_eanewscomments'),
(35, 'Can change ea news comments', 12, 'change_eanewscomments'),
(36, 'Can delete ea news comments', 12, 'delete_eanewscomments'),
(37, 'Can add ea news feed', 13, 'add_eanewsfeed'),
(38, 'Can change ea news feed', 13, 'change_eanewsfeed'),
(39, 'Can delete ea news feed', 13, 'delete_eanewsfeed'),
(40, 'Can add ea fees accounts', 14, 'add_eafeesaccounts'),
(41, 'Can change ea fees accounts', 14, 'change_eafeesaccounts'),
(42, 'Can delete ea fees accounts', 14, 'delete_eafeesaccounts');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$100000$6eYueyDCh8yS$mtlj70TIKnAB0VZC7SAtxXPLY5FiNxuT2vSJmhhMP0c=', '2018-04-25 08:01:54.100544', 1, 'dhruv', 'Dhruv', 'Patel', 'dhruvpatel5738@gmail.com', 1, 1, '2018-04-16 09:20:13.403775'),
(2, 'pbkdf2_sha256$100000$2EfZQTt3LfH2$ox457lAv6EHT3C9iPIQmW24xf/qtkA7EuG9yFpsmuak=', NULL, 1, 'bhaumik', 'Bhaumik', 'Ichhaporia', 'bhaumik.ichhaporia59@gmail.com', 1, 1, '2018-04-25 08:02:19.000000'),
(3, 'pbkdf2_sha256$100000$0OE7W3YnCC4w$3ogWwdhUVcocTBM4D7l2pkO1Ded2Jo5r64fwpRtos/c=', NULL, 1, 'prit123', 'Prit', 'Thakkar', 'pritthakkar@gmail.com', 0, 1, '2018-05-04 10:09:12.074985'),
(4, 'pbkdf2_sha256$100000$yy6xIu84CdXa$/EwWng/QUkCr+eBkydg3lj/hZCdTBpvTudEU1owFJfQ=', NULL, 0, 'shail123', 'Shail', 'Shah', 'shailshah@gmail.com', 0, 1, '2018-05-04 10:09:59.379928'),
(6, 'pbkdf2_sha256$100000$gL4aejiPEiLD$I2MMcC2670Kpo3taol98MVWOKwzOiHlP1LFqGkwcW4s=', NULL, 0, 'daxa123', 'Dxa', 'Patel', 'dxapatel0910@gmail.com', 0, 1, '2018-05-27 09:10:33.827874');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2018-04-25 08:02:20.057022', '2', 'bhaumik', 1, '[{\"added\": {}}]', 4, 1),
(2, '2018-04-25 08:02:56.172527', '2', 'bhaumik', 2, '[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"email\"]}}]', 4, 1),
(3, '2018-04-25 08:19:52.252538', '2', 'bhaumik', 2, '[{\"changed\": {\"fields\": [\"is_superuser\"]}}]', 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(11, 'api', 'eaacademichistory'),
(7, 'api', 'eaattendance'),
(14, 'api', 'eafeesaccounts'),
(12, 'api', 'eanewscomments'),
(13, 'api', 'eanewsfeed'),
(8, 'api', 'eastudentdetails'),
(9, 'api', 'eateacherdetails'),
(10, 'api', 'eausermapping'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2018-04-16 09:17:58.309376'),
(2, 'auth', '0001_initial', '2018-04-16 09:18:05.212724'),
(3, 'admin', '0001_initial', '2018-04-16 09:18:07.874726'),
(4, 'admin', '0002_logentry_remove_auto_add', '2018-04-16 09:18:07.940728'),
(5, 'contenttypes', '0002_remove_content_type_name', '2018-04-16 09:18:09.036731'),
(6, 'auth', '0002_alter_permission_name_max_length', '2018-04-16 09:18:09.691727'),
(7, 'auth', '0003_alter_user_email_max_length', '2018-04-16 09:18:10.627727'),
(8, 'auth', '0004_alter_user_username_opts', '2018-04-16 09:18:10.687728'),
(9, 'auth', '0005_alter_user_last_login_null', '2018-04-16 09:18:11.122733'),
(10, 'auth', '0006_require_contenttypes_0002', '2018-04-16 09:18:11.169735'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2018-04-16 09:18:11.231729'),
(12, 'auth', '0008_alter_user_username_max_length', '2018-04-16 09:18:12.783728'),
(13, 'auth', '0009_alter_user_last_name_max_length', '2018-04-16 09:18:13.606727'),
(14, 'sessions', '0001_initial', '2018-04-16 09:18:14.058729'),
(15, 'api', '0001_initial', '2018-05-04 09:44:45.963653'),
(16, 'api', '0002_eanewscomments_eanewsfeed', '2018-05-15 10:53:09.962826'),
(17, 'api', '0003_eafeesaccounts', '2018-05-27 09:08:51.362791');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('8w48kwz697s438ciezbsw87n5e3zshjp', 'ODBmNzM0MzIxODUxNzVlYjE3ZTM4MmQwOTVjZGM2ZTZhNGQ1YzRjYzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2hhc2giOiIyY2FhM2ZmNzAzZjMxNzlhZjAyMTY5NWVjNjVkNjIwNjQzMDYyODM4In0=', '2018-05-09 08:01:54.168537'),
('o0xqcdv52bu5pzu8vf4cviaq6b7z3f7z', 'MjRiOTI1YzAwZTRiNGIyYzJjN2M3OTA4N2U2NGM2N2U1YmNkOGJkNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiMmNhYTNmZjcwM2YzMTc5YWYwMjE2OTVlYzY1ZDYyMDY0MzA2MjgzOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2018-04-30 09:20:39.129279');

-- --------------------------------------------------------

--
-- Table structure for table `ea_academic_history`
--

CREATE TABLE `ea_academic_history` (
  `user_id` int(11) NOT NULL,
  `university` varchar(255) DEFAULT NULL,
  `year_of_passing` date DEFAULT NULL,
  `percentage_scored` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ea_academic_history`
--

INSERT INTO `ea_academic_history` (`user_id`, `university`, `year_of_passing`, `percentage_scored`) VALUES
(5, '', NULL, NULL),
(6, '', NULL, NULL),
(20, '', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `ea_attendance`
--

CREATE TABLE `ea_attendance` (
  `att_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `user_type` varchar(255) NOT NULL,
  `attend_status` tinyint(1) NOT NULL,
  `roll_no` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ea_attendance`
--

INSERT INTO `ea_attendance` (`att_id`, `user_id`, `date`, `user_type`, `attend_status`, `roll_no`) VALUES
(3, 1, '2018-05-05 13:05:21', 'student', 0, 1),
(4, 3, '2018-05-05 13:05:21', 'student', 1, 3),
(5, 1, '2018-05-06 13:06:50', 'student', 0, 1),
(6, 3, '2018-05-05 13:06:50', 'student', 1, 3),
(7, 1, '2018-05-05 13:25:04', 'student', 0, 1),
(8, 3, '2018-05-05 13:25:04', 'student', 1, 3),
(9, 1, '2018-05-05 13:59:44', 'student', 1, 1),
(10, 3, '2018-05-05 13:59:44', 'student', 0, 3),
(11, 1, '2018-05-05 13:59:45', 'student', 1, 1),
(12, 3, '2018-05-05 13:59:45', 'student', 0, 3),
(13, 1, '2018-05-05 14:53:04', 'student', 1, 1),
(14, 3, '2018-05-05 14:53:04', 'student', 0, 3),
(15, 1, '2018-05-15 15:03:56', 'student', 0, 1),
(16, 3, '2018-05-15 15:03:56', 'student', 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `ea_fees_accounts`
--

CREATE TABLE `ea_fees_accounts` (
  `trans_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `paid_status` tinyint(1) NOT NULL DEFAULT '0',
  `fees_paid` int(11) DEFAULT NULL,
  `total_fees` int(11) DEFAULT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ea_fees_accounts`
--

INSERT INTO `ea_fees_accounts` (`trans_id`, `user_id`, `paid_status`, `fees_paid`, `total_fees`, `date`) VALUES
(1, 6, 0, 3000, 8000, '2018-05-27 14:45:33');

-- --------------------------------------------------------

--
-- Table structure for table `ea_news_comments`
--

CREATE TABLE `ea_news_comments` (
  `comment_id` int(11) NOT NULL,
  `news_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `description` text,
  `likes` tinyint(1) NOT NULL DEFAULT '0',
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ea_news_comments`
--

INSERT INTO `ea_news_comments` (`comment_id`, `news_id`, `user_id`, `description`, `likes`, `date`) VALUES
(9, 15, 4, 'Are classes cancelled tomorrow?', 1, '2018-05-31 19:17:59'),
(10, 15, 1, 'Yes, they are.', 0, '2018-05-31 19:18:20'),
(11, 15, 3, '', 1, '2018-05-31 21:16:53');

-- --------------------------------------------------------

--
-- Table structure for table `ea_news_feed`
--

CREATE TABLE `ea_news_feed` (
  `news_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `description` text,
  `file_name` varchar(255) DEFAULT NULL,
  `file_type` varchar(255) DEFAULT NULL,
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ea_news_feed`
--

INSERT INTO `ea_news_feed` (`news_id`, `user_id`, `description`, `file_name`, `file_type`, `date`) VALUES
(15, 1, 'Important Document regarding classes', '5_502012', 'jpg', '2018-05-31 19:14:36'),
(16, 1, 'No classes tomorrow', '', '', '2018-05-31 19:15:26'),
(17, 1, '', '11_260626', 'jpg', '2018-05-31 19:15:40');

-- --------------------------------------------------------

--
-- Table structure for table `ea_student_details`
--

CREATE TABLE `ea_student_details` (
  `user_id` int(11) NOT NULL,
  `standard` tinyint(4) DEFAULT NULL,
  `school` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `branch` varchar(255) DEFAULT NULL,
  `emergency_number` bigint(20) DEFAULT NULL,
  `roll_no` int(11) NOT NULL,
  `year_of_joining` varchar(4) DEFAULT NULL,
  `birthdate` date DEFAULT NULL,
  `contact_no` bigint(20) DEFAULT NULL,
  `refs` text,
  `subjects_enrolled` text,
  `year_of_leaving` varchar(4) DEFAULT NULL,
  `stream` varchar(255) DEFAULT NULL,
  `board` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ea_student_details`
--

INSERT INTO `ea_student_details` (`user_id`, `standard`, `school`, `address`, `branch`, `emergency_number`, `roll_no`, `year_of_joining`, `birthdate`, `contact_no`, `refs`, `subjects_enrolled`, `year_of_leaving`, `stream`, `board`) VALUES
(1, 8, 'Bright ', '24, Ram nagar Society', 'Devraj', 9825577083, 1, '2017', '1996-05-08', 8469905736, '', 'Maths;Science;English;', '2018', 'Science', 'CBSE'),
(3, 8, 'Bright', '34, Balajinagar Society ', 'Devraj', 8469905736, 5, '2018', '1997-03-03', 8469905736, '', 'Social Science;Maths;Science;', '2018', 'Science', 'CBSE'),
(4, 9, 'BHS', '29, Ram nagar Society', 'Pujer', 8469905736, 2, '2016', '1996-05-08', 9825577083, '', 'Physics;Chemistry;Maths', '2018', 'Science', 'GBSE'),
(6, 10, 'Navrachna', '45, Shanti Park Society', '', 9998262001, 6, '2018', '1998-12-12', 9998252004, 'Via Internet', 'Maths', '2019', 'Science', 'CBSE');

-- --------------------------------------------------------

--
-- Table structure for table `ea_teacher_details`
--

CREATE TABLE `ea_teacher_details` (
  `user_id` int(11) NOT NULL,
  `standard` int(11) DEFAULT NULL,
  `subject` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `birthdate` date DEFAULT NULL,
  `year_of_joining` datetime DEFAULT NULL,
  `activated_status` tinyint(1) DEFAULT NULL,
  `contact_no` bigint(20) DEFAULT NULL,
  `salary` int(11) DEFAULT NULL,
  `bank_details` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ea_user_mapping`
--

CREATE TABLE `ea_user_mapping` (
  `user_id` int(11) NOT NULL,
  `user_type` varchar(255) NOT NULL,
  `gender` tinyint(1) NOT NULL,
  `profile_pic` varchar(255) NOT NULL,
  `profile_pic_type` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ea_user_mapping`
--

INSERT INTO `ea_user_mapping` (`user_id`, `user_type`, `gender`, `profile_pic`, `profile_pic_type`) VALUES
(1, 'admin', 1, 'patel_dhruv_387802', 'jpg'),
(2, 'admin', 1, 'male', 'png'),
(3, 'student', 1, 'male', 'png'),
(4, 'student', 1, 'male', 'png'),
(6, 'student', 0, 'female', 'png');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `ea_academic_history`
--
ALTER TABLE `ea_academic_history`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `ea_attendance`
--
ALTER TABLE `ea_attendance`
  ADD PRIMARY KEY (`att_id`),
  ADD KEY `att_user` (`user_id`);

--
-- Indexes for table `ea_fees_accounts`
--
ALTER TABLE `ea_fees_accounts`
  ADD PRIMARY KEY (`trans_id`),
  ADD KEY `user_pays_fees` (`user_id`);

--
-- Indexes for table `ea_news_comments`
--
ALTER TABLE `ea_news_comments`
  ADD PRIMARY KEY (`comment_id`),
  ADD KEY `news_have_comments` (`news_id`),
  ADD KEY `comments_have_users` (`user_id`);

--
-- Indexes for table `ea_news_feed`
--
ALTER TABLE `ea_news_feed`
  ADD PRIMARY KEY (`news_id`),
  ADD KEY `user_creates_news` (`user_id`);

--
-- Indexes for table `ea_student_details`
--
ALTER TABLE `ea_student_details`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `ea_teacher_details`
--
ALTER TABLE `ea_teacher_details`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `ea_user_mapping`
--
ALTER TABLE `ea_user_mapping`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `ea_attendance`
--
ALTER TABLE `ea_attendance`
  MODIFY `att_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `ea_fees_accounts`
--
ALTER TABLE `ea_fees_accounts`
  MODIFY `trans_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `ea_news_comments`
--
ALTER TABLE `ea_news_comments`
  MODIFY `comment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `ea_news_feed`
--
ALTER TABLE `ea_news_feed`
  MODIFY `news_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `ea_student_details`
--
ALTER TABLE `ea_student_details`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `ea_teacher_details`
--
ALTER TABLE `ea_teacher_details`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `ea_fees_accounts`
--
ALTER TABLE `ea_fees_accounts`
  ADD CONSTRAINT `user_pays_fees` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ea_news_comments`
--
ALTER TABLE `ea_news_comments`
  ADD CONSTRAINT `comments_have_users` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `news_have_comments` FOREIGN KEY (`news_id`) REFERENCES `ea_news_feed` (`news_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ea_news_feed`
--
ALTER TABLE `ea_news_feed`
  ADD CONSTRAINT `user_creates_news` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ea_student_details`
--
ALTER TABLE `ea_student_details`
  ADD CONSTRAINT `student_user` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ea_teacher_details`
--
ALTER TABLE `ea_teacher_details`
  ADD CONSTRAINT `teacher_is_a_user` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ea_user_mapping`
--
ALTER TABLE `ea_user_mapping`
  ADD CONSTRAINT `user_type_mapping` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
