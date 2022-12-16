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

CREATE TABLE booking(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_date DATE NOT NULL,
    to_date DATE NOT NULL,
    price INTEGER NOT NULL,
    customer_id INTEGER,
    room_id INTEGER,
    FOREIGN KEY(customer_id) REFERENCES customer(id),
    FOREIGN KEY(room_id) REFERENCES room(id)
);

INSERT INTO booking
    (from_date, to_date, price,customer_id,room_id)
VALUES
    ('15', 35, 550);
