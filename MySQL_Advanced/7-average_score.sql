DELIMITER $$
-- procedure to calculate avg score of an user
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    UPDATE users
    SET average_score = (
        SELECT AVG(score)
        FROM corrections c
        WHERE c.user_id = user_id
    )
    WHERE users.id = user_id;
END $$

DELIMITER ;