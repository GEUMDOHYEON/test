CREATE TABLE Users (
    user_id BIGINT(20) NOT NULL AUTO_INCREMENT,
    user_email VARCHAR(200) NOT NULL,
    user_password VARCHAR(200) NOT NULL,
    user_name VARCHAR(200) NOT NULL,
    PRIMARY KEY (user_id),
    UNIQUE(user_email)
);