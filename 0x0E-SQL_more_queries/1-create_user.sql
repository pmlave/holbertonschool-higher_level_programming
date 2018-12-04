-- Create a new user with a specific password
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON localhost.* TO user_0d_1@localhost;
