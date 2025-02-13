create database Finapp;
use Finapp;

create table usuarios(
	UserID int auto_increment primary key,
    email varchar(100) not null,
    nome varchar(100) not null,
    senha varchar(100) not null
);

create table details_users(
	userID int primary key,
    date_birth date,
    mobile_number int,
    image mediumblob,
    first_name varchar(100),
    last_name varchar(100),
    FOREIGN KEY (userID) REFERENCES usuarios(userid) ON DELETE CASCADE
);

create table entrada (
    entradaID int auto_increment primary key,
    entrada_data datetime not null,
    categoria varchar(100) not null,
    valor double(10,2) not null,
    estado varchar(100) not null,
    remetente varchar(100)
);

create table saida (
	saidaID int auto_increment primary key,
    saida_data datetime not null,
    categoria varchar(100) not null,
    valor double(10,2) not null,
    estado varchar(100) not null,
    destinatario varchar(100)
);

DELIMITER $$

CREATE TRIGGER after_user_insert
AFTER INSERT ON usuarios
FOR EACH ROW
BEGIN
    INSERT INTO details_users (userID, first_name, last_name, date_birth, mobile_number, image)
    VALUES (NEW.UserID, NEW.nome, NULL, NULL, NULL, NULL);
END$$

DELIMITER ;