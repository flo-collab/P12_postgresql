DROP TABLE IF EXISTS promoteur;
CREATE TABLE IF NOT EXISTS promoteur(
    id INTEGER,
    id_lot VARCHAR (255),
    nb_piece INTEGER,
    typologie VARCHAR (255),
    prix_tva_reduite FLOAT (12),
    prix_tva_normale FLOAT (12),
    prix_HT FLOAT (12),
    prix_m2_HT FLOAT (12),
    prix_m2_TTC FLOAT (12),
    orientation VARCHAR (255),
    exterieur VARCHAR (255),
    balcony VARCHAR (255),
    garden VARCHAR (255),
    parking INTEGER,
    ville VARCHAR (255),
    departement VARCHAR (255),
    date_fin_programme VARCHAR (255),
    adresse_entiere VARCHAR (255),
    date_extraction DATE,
    PRIMARY KEY (id)
);

-- SELECT * FROM promoteur;

