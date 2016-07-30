-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema LoginRegister
-- -----------------------------------------------------
-- changed name
-- 

-- -----------------------------------------------------
-- Schema LoginRegister
--
-- changed name
-- 
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `LoginRegister` DEFAULT CHARACTER SET utf8 ;
USE `LoginRegister` ;

-- -----------------------------------------------------
-- Table `LoginRegister`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LoginRegister`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(8) NOT NULL,
  `hint` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LoginRegister`.`table1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LoginRegister`.`table1` (
)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
