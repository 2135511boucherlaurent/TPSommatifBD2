USE tpsommatif_bd2;

DELIMITER $$
    CREATE TRIGGER personnage_avant_insert BEFORE INSERT ON fiche_personnage FOR EACH ROW
        BEGIN
        IF NEW.bourse > 50 THEN
            SET NEW.bourse = 50;
        END IF;
    END $$
DELIMITER ;

DELIMITER $$
    CREATE PROCEDURE `prendreArmes`()
        BEGIN
        SELECT * FROM `armes`;
    END $$
DELIMITER ;