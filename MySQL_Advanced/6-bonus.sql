DELIMITER $$
-- procedure :)
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
AS
BEGIN
    IF NOT EXISTS(
    SELECT name
    FROM projects
    WHERE project_name = name
    )
    BEGIN
        INSERT INTO projects(name)
        VALUES(project_name);
    END
    INSERT INTO corrections(user_id, project_id, score)
    SELECT user_id, id, score 
    FROM projects
    WHERE project_name = projects.name;
END$$
DELIMITER ;
