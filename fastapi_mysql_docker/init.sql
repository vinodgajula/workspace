CREATE DATABASE IF NOT EXISTS fastapi_db;
USE fastapi_db;

CREATE TABLE IF NOT EXISTS items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT
);
