-- creates a second table in the database
CREATE TABLE IF NOT EXISTS second_table(
       id INT
       name VARCHAR(256)
       score INT
);
INSERT INTO second_table
VALUES ROW(1,2,3,4), ROW("John", "Alex", "Bob", "George"), ROW(10,3,14,8);
