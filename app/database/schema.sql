create database Finapp;
use Finapp;


CREATE TABLE registroUsers(
	UserID int AUTO_INCREMENT primary key,
    email varchar(100) not null,
    nome varchar(100) not null,
    senha varchar(100) not null
);

CREATE TABLE login (
    LoginID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL,
    FOREIGN KEY (UserID) REFERENCES RegistroUsers(UserID)
);


DELIMITER //
CREATE TRIGGER `finapp`.`registrousers_BEFORE_DELETE` BEFORE DELETE ON `registrousers` FOR EACH ROW
BEGIN
	DELETE FROM Login WHERE UserID = OLD.UserID;
END;
//
CREATE TRIGGER `finapp`.`registrousers_AFTER_INSERT` AFTER INSERT ON `registrousers` FOR EACH ROW
BEGIN
	INSERT INTO Login (UserID, nome, senha) VALUES (NEW.UserID, NEW.nome, NEW.senha);
END;
//