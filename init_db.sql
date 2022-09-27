-- SQLite
CREATE TABLE customer(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name CHAR(250) NOT NULL,
    last_name CHAR(250) NOT NULL,
    email_address CHAR(250) NOT NULL
);

INSERT INTO customer
    (first_name, last_name, email_address)
VALUES
    ('Andres', 'Cevilla', 'andy.cevilla@gmail.com');

CREATE TABLE room(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number CHAR(250) NOT NULL,
    size INTEGER NOT NULL,
    price INTEGER NOT NULL
);

INSERT INTO room
    (number, size, price)
VALUES
    ('15', 35, 550);
