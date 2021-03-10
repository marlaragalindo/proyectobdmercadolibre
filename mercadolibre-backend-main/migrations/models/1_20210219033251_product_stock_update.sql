-- upgrade --
ALTER TABLE `product` ADD `stock` INT NOT NULL;
-- downgrade --
ALTER TABLE `product` DROP COLUMN `stock`;
