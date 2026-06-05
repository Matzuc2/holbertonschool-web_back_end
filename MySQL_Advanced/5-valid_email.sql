DELIMITER $$
-- Create a trigger updating the validity of an email
CREATE TRIGGER valid_email45
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    SET NEW.valid_email = 0;
END$$

DELIMITER ;