-- Create CDC tracking table
CREATE TABLE cdc_tracking (
    id INT AUTO_INCREMENT PRIMARY KEY,
    table_name VARCHAR(100),
    change_type VARCHAR(10), -- Changed ENUM to VARCHAR
    change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INT, 
);

-- Create trigger for INSERTs
DELIMITER $$
CREATE TRIGGER cdc_trigger_insert AFTER INSERT ON employee
FOR EACH ROW
BEGIN
    INSERT INTO cdc_tracking (table_name, change_type, user_id, status)
    VALUES ('employee', 'INSERT', 1234, 'new'); -- Set user_id appropriately
END$$
DELIMITER ;-- 

-- Create trigger for UPDATEs
DELIMITER $$
CREATE TRIGGER cdc_trigger_update AFTER UPDATE ON employee
FOR EACH ROW
BEGIN
    INSERT INTO cdc_tracking (table_name, change_type, user_id)
    VALUES ('employee', 'UPDATE', 1234, 'new'); -- Set user_id appropriately
END$$
DELIMITER ;

-- -- Create trigger for DELETEs
DELIMITER $$
CREATE TRIGGER cdc_trigger_delete AFTER DELETE ON employee
FOR EACH ROW
BEGIN
    INSERT INTO cdc_tracking (table_name, change_type, user_id)
    VALUES ('employee', 'DELETE', 1234, 'new'); -- Set user_id appropriately
END$$
DELIMITER ;
