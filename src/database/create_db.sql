-- SQL script to create PostgreSQL schema
CREATE DATABASE medical_data;

\c medical_data;

CREATE TABLE medical_businesses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    contact_info VARCHAR(255),
    description TEXT,
    image_url VARCHAR(255)
);

CREATE TABLE scraped_images (
    id SERIAL PRIMARY KEY,
    business_id INT REFERENCES medical_businesses(id),
    image_url VARCHAR(255),
    object_detected BOOLEAN
);
