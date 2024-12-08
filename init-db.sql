-- init-db.sql
CREATE DATABASE IF NOT EXISTS flaskdb;
USE flaskdb;

CREATE TABLE IF NOT EXISTS images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255) NOT NULL
);

INSERT INTO images (url) VALUES
    ('https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXpyZDlzODRsejNicHc4dDVvNXRscjdybDNldXc1eWhqejM3cjY4ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QvBoMEcQ7DQXK/giphy.gif'),
    ('https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXpyZDlzODJzOXZ6Z2VjMjEwZm5pNW9yazZyNTFqdmZqd2tqb2tqdzlqfGpqaGJtfnN0ZTJrYnpxNWRuNHRkYmN6g63wh7uQ9g/giphy.gif'),
    ('https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXpyZDlzODRsejNicHc4dDVvNXRscjdybDNldXc1eWhqejM3cjY4ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QvBoMEcQ7DQXK/giphy.gif');
