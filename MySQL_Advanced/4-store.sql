DELIMITER $$
-- Create a trigger updating the quantity
CREATE TRIGGER trig_Z
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - 1
    WHERE name = NEW.item_name;
END$$

DELIMITER ;