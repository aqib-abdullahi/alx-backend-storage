-- Create the ComputeAverageScoreForUser stored procedure
-- computes student's average
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_count INT;
    
    SELECT SUM(score) INTO total_score, COUNT(*) INTO total_count
    FROM corrections
    WHERE user_id = user_id;
    
    DECLARE avg_score FLOAT;
    IF total_count > 0 THEN
        SET avg_score = total_score / total_count;
    ELSE
        SET avg_score = 0;
    END IF;
    
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END $$

DELIMITER ;
