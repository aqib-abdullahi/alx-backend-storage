-- increates a trigger that decreases the quantity of an item
-- after adding a new order. Quantity in the table items can be negative.
DELIMITER $$
CREATE TRIGGER IF NOT EXISTS update_item $$
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE
		SET quantity = quantity - NEW.number
		WHERE name = NEW.item_name;
END $$
DELIMITER ;
