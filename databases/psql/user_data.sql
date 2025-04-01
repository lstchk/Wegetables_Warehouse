CREATE SCHEMA IF NOT EXISTS user_data;

CREATE TABLE IF NOT EXISTS  user_data.user_profile
(
    id            serial,
    phone_number  varchar(30),
    email         varchar(100),
    address       varchar(500),
    payment_cards integer[],
    CONSTRAINT user_profile_pk
        PRIMARY KEY (id)
);

