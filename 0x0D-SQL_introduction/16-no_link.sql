-- lists records in Database
-- DML query to show results in DB, sorted by score 
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
