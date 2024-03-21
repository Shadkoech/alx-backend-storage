-- SQL script creating a trigger that decreases the quantity 
-- of an item after addition of a new order
-- Quantity in the table items can be negative.
-- New & OLD are MySQL extensions to triggers
-- enable to access columns in the rows affected by a trigger

DELIMITER //
CREATE TRIGGER decrease_quantity AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
//

DELIMITER ;