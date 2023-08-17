-- Create user if not exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user
GRANT USAGE ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
