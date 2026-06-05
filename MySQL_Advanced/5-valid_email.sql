DELIMITER $$
-- Trigger that update the validity boolean of an email for an user on update
CREATE TRIGGER valid_email23
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;