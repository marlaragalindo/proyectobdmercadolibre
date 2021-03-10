-- upgrade --
ALTER TABLE `purchaseproduct` DROP COLUMN `discount`;
-- downgrade --
ALTER TABLE `purchaseproduct` ADD `discount` DOUBLE NOT NULL;
