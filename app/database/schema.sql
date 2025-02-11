create database Finapp;
use Finapp;

create table usuarios(
	UserID int auto_increment primary key,
    email varchar(100) not null,
    nome varchar(100) not null,
    senha varchar(100) not null
);

create table entrada (
    entradaID int auto_increment primary key,
    entrada_data datetime not null,
    categoria varchar(100) not null,
    valor double(10,2) not null,
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