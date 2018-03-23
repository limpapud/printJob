CREATE DATABASE IF NOT EXISTS `print` 
DEFAULT CHARACTER SET 
latin1 COLLATE 
latin1_swedish_ci;
USE `print`;

branch_list CREATE TABLE `branch_list` (
  `branch_name` text NOT NULL,
  `a_status` tinyint(1) NOT NULL,
  `last_active` datetime NOT NULL
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8 
printqueue CREATE TABLE `printqueue` (
  `fileLocation` text NOT NULL,
  `ShopName` text NOT NULL,
  `printStatus` tinyint(1) NOT NULL,
  `creationDate` datetime NOT NULL,
  `fileBlob` mediumblob
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8 
