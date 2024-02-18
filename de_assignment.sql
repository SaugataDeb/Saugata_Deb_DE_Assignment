-- CREATE TABLE IF NOT EXISTS customers (
--     customer_id TEXT PRIMARY KEY,
--     age INTEGER
-- );

-- CREATE TABLE IF NOT EXISTS sales (
--     sales_id INTEGER PRIMARY KEY,
--     customer_id TEXT,
--     FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
-- );

-- CREATE TABLE IF NOT EXISTS items (
--     item_id INTEGER PRIMARY KEY,
--     item_name TEXT
-- );

-- CREATE TABLE IF NOT EXISTS orders (
--     order_id INTEGER PRIMARY KEY,
--     sales_id INTEGER,
--     item_id INTEGER,
--     quantity INTEGER,
--     FOREIGN KEY (sales_id) REFERENCES sales(sales_id),
--     FOREIGN KEY (item_id) REFERENCES items(item_id)
-- );

-- INSERT INTO customers (customer_id, age) VALUES
-- ('C001', 30), ('C002', 25), ('C003', 40), ('C004', 22), ('C005', 28);

-- INSERT INTO sales (sales_id, customer_id) VALUES
-- (1, 'C001'), (2, 'C002'), (3, 'C003'), (4, 'C004'), (5, 'C005');

-- INSERT INTO items (item_id, item_name) VALUES
-- (101, 'Laptop'), (102, 'Smartphone'), (103, 'Tablet'), (104, 'Headphones'), (105, 'Mouse');

-- INSERT INTO orders (order_id, sales_id, item_id, quantity) VALUES
-- (1001, 1, 101, 1), (1002, 1, 102, NULL), (1003, 1, 103, NULL),
-- (1004, 2, 101, 2), (1005, 2, 102, 1), (1006, 3, 103, 3),
-- (1007, 4, 104, 1), (1008, 4, 105, 2), (1009, 5, 101, 1),
-- (1010, 5, 103, NULL), (1011, 5, 104, 2), (1012, 5, 105, 3);


-- SELECT * FROM customers

-- SELECT * FROM sales;

-- SELECT * FROM items;

-- SELECT * FROM orders;
