DROP DATABASE IF EXISTS tpsommatif_bd2;
CREATE DATABASE tpsommatif_bd2;

USE tpsommatif_bd2;

CREATE TABLE IF NOT EXISTS livre (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `titre` VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS chapitre (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `livre_id` INT DEFAULT 1 NOT NULL,
    `no_chapitre` INTEGER NOT NULL,
    `texte` TEXT NOT NULL,
     FOREIGN KEY (`livre_id`) REFERENCES `livre`(`id`)
);

CREATE TABLE IF NOT EXISTS lien_chapitre (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `no_chapitre_origine` INT NOT NULL,
    `no_chapitre_destination` INT NOT NULL,
    FOREIGN KEY (`no_chapitre_origine`) REFERENCES `chapitre`(`id`),
    FOREIGN KEY (`no_chapitre_destination`) REFERENCES `chapitre`(`id`)
);

CREATE TABLE IF NOT EXISTS fiche_personnage (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `nom` VARCHAR(64) NOT NULL,
    `bourse` INT DEFAULT 0,
    `object` VARCHAR(255),
    `repas` VARCHAR(255),
    `object_speciaux` VARCHAR(255),
    `chapitre_id` INT NOT NULL,
    `livre_id` INT DEFAULT 1 NOT NULL,
    FOREIGN KEY (`chapitre_id`) REFERENCES `chapitre`(`id`),
    FOREIGN KEY (`livre_id`) REFERENCES `livre`(`id`) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS disciplines_kai (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `nom` VARCHAR(64),
    `livre_id` INT DEFAULT 1 NOT NULL,
    FOREIGN KEY (`livre_id`) REFERENCES `livre`(`id`)
);

CREATE TABLE IF NOT EXISTS disciplines_kai_fiche_personnage (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `fiche_personnage_id` INT NOT NULL,
    `disciplines_kai_id` INT NOT NULL,
    FOREIGN KEY (`fiche_personnage_id`) REFERENCES `fiche_personnage`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`disciplines_kai_id`) REFERENCES `disciplines_kai`(`id`) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS armes (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `nom` VARCHAR(64),
    `livre_id` INT DEFAULT 1 NOT NULL,
    FOREIGN KEY (`livre_id`) REFERENCES `livre`(`id`)
);

CREATE TABLE IF NOT EXISTS armes_fiche_personnage (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `fiche_personnage_id` INT NOT NULL,
    `armes_id` INT NOT NULL,
    FOREIGN KEY (`fiche_personnage_id`) REFERENCES `fiche_personnage`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`armes_id`) REFERENCES `armes`(`id`) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS sauvegarde (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `nom` VARCHAR(255),
    `no_chapitre_id` INT,
    `fiche_id` INT UNIQUE,
    `livre_id` INT,
    FOREIGN KEY (livre_id) REFERENCES livre(id) ON DELETE CASCADE,
    FOREIGN KEY (no_chapitre_id) REFERENCES chapitre(id) ON DELETE CASCADE,
    FOREIGN KEY (fiche_id) REFERENCES fiche_personnage(id) ON DELETE CASCADE,
    UNIQUE KEY unique_fiche_id (id, fiche_id)
);

DROP USER IF EXISTS 'root'@'localhost';
CREATE USER 'root'@'localhost' IDENTIFIED BY 'mysql';

GRANT SELECT ON *.* TO 'root'@'localhost';
GRANT INSERT, DELETE, UPDATE ON `fiche_personnage` TO 'root'@'localhost';
GRANT INSERT, DELETE, UPDATE ON 'disciplines_kai_fiche_personnage' TO 'root'@'localhost';
GRANT INSERT, DELETE, UPDATE ON 'sauvegarde' TO 'root'@'localhost';
GRANT INSERT, DELETE, UPDATE ON 'armes_fiche_personnage' TO 'root'@'localhost';