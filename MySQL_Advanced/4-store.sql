DELIMITER $$
-- Create a trigger updating the quantity
CREATE TRIGGER trig_Z
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

DELIMITER ;