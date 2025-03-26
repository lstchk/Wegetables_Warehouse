CREATE SCHEMA IF NOT EXISTS shop;

CREATE TABLE IF NOT EXISTS shop.units
(
    id   serial,
    name varchar(10) not null,
    CONSTRAINT  units_pk
        PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS shop.categories
(
    id          serial,
    name        varchar(50) not null,
    description text,
    CONSTRAINT categories_pk
        PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS shop.goods
(
    id          serial,
    category_id serial,
    name        varchar(100)     not null,
    quantity    double precision not null,
    unit_type   serial,
    price       double precision not null,
    description text,
    image_link  text,
    CONSTRAINT goods_pk
        PRIMARY KEY (id),
    CONSTRAINT goods_categories_id_fk
        FOREIGN KEY  (category_id) REFERENCES shop.categories,
    CONSTRAINT goods_units_id_fk
        FOREIGN KEY (unit_type) REFERENCES shop.units
);