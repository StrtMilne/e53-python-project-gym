DROP TABLE IF EXISTS attendances;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    dob DATE,
    join_date DATE
);

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    date DATE,
    time TIME
);

CREATE TABLE attendances (
    id SERIAL PRIMARY KEY,
    class_id INT REFERENCES classes(id),
    member_id INT REFERENCES members(id)
);