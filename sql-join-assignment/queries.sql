CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name TEXT,
    signup_date DATE
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    amount INT
);

CREATE TABLE activity (
    user_id INT,
    login_count INT
);

INSERT INTO users VALUES
(1, 'Aarav', '2023-01-10'),
(2, 'Diya', '2023-02-14'),
(3, 'Rohan', '2023-03-01'),
(4, 'Meera', '2023-04-11'),
(5, 'Kabir', '2023-05-06');

INSERT INTO orders VALUES
(101, 1, 500),
(102, 1, 700),
(103, 2, 300),
(104, 4, 900),
(105, 4, 400);

INSERT INTO activity VALUES
(1, 25),
(2, 10),
(3, 5),
(5, 12);