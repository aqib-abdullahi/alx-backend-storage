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
    
    SELECT SUM(score) INTO total_score
    FROM corrections
    WHERE corrections.user_id = user_id;
    
    SELECT COUNT(*) INTO total_count
    FROM corrections
    WHERE corrections.user_id = user_id;
    
    UPDATE users
    SET users.average_score = IF(total_count = 0, 0, total_score / total_count)
    WHERE users.id = user_id;
END $$

DELIMITER ;
