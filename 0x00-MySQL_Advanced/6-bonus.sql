-- SQL scritp that creates a stored procedure AddNonus
-- that adds a new correction for a student
/* Requirement */
-- Procedure AddBonus is taking 3 inputs: user_id, project_name, score

DELIMITER ##

DROP PROCEDURE IF EXISTS AddBonus;
CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score FLOAT
)
BEGIN
    DECLARE project_id INT;

    -- Check to verify if project exists
    SELECT id INTO project_id FROM projects WHERE name = project_name;

    -- In the case that project does not exist, creat one
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Finally insert the correction
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END;
##

DELIMITER ;