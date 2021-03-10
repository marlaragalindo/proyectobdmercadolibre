-- upgrade --
CREATE TABLE IF NOT EXISTS `category` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `customer` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `address` VARCHAR(255) NOT NULL,
    `phone` INT NOT NULL,
    `password` VARCHAR(64) NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `seller` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `address` VARCHAR(255) NOT NULL,
    `phone` INT NOT NULL,
    `password` VARCHAR(64) NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `product` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(128) NOT NULL,
    `price` DOUBLE NOT NULL,
    `date` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `category_id` INT NOT NULL,
    `seller_id` INT NOT NULL,
    CONSTRAINT `fk_product_category_b9cd9984` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_product_seller_1f8f1dd6` FOREIGN KEY (`seller_id`) REFERENCES `seller` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `purchaseproduct` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `quantity` INT NOT NULL,
    `discount` DOUBLE NOT NULL,
    `payment_method` VARCHAR(16) NOT NULL  COMMENT 'transfer: transfer\ncredit: credit\ndebit: debit',
    `date` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `customer_id` INT NOT NULL,
    `product_id` INT NOT NULL,
    CONSTRAINT `fk_purchase_customer_a2a65872` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_purchase_product_ffe5024a` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(20) NOT NULL,
    `content` TEXT NOT NULL
) CHARACTER SET utf8mb4;
