DELIMITER $$
-- procedure :)
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    IF NOT EXISTS(
    SELECT 1
    FROM projects
    WHERE project_name = name
    ) THEN
        INSERT INTO projects(name)
        VALUES(project_name);
    END IF;

    INSERT INTO corrections(user_id, project_id, score)
    SELECT user_id, id, score 
    FROM projects
    WHERE project_name = projects.name;
END$$
DELIMITER ;