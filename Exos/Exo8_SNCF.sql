-- a
SELECT c_nom, c_prenom FROM conducteur;

-- b
SELECT c_nom, c_prenom FROM conducteur WHERE c_num = 456;

-- c
SELECT t_num, t_localite FROM train WHERE t_type IN ('TGV' ,'TER');

-- d
SELECT ville_d FROM liaison;

-- e
SELECT t_num FROM train WHERE wagon_l = 'oui';

--f
SELECT t_num FROM liaison WHERE l_num = 626;

-- g 
SELECT c_num FROM liaison WHERE ville_d = 'Bordeaux' AND heurre_d BETWEEN 14 AND 16 ;

-- h
SELECT t_num FROM liaison WHERE ville_a = 'Loudun';

-- i 
SELECT ville_d FROM liaison WHERE l_num = 323;

-- j
SELECT c_ville FROM conducteur WHERE c_num = 46545;

-- k
SELECT t_num FROM train WHERE t_type IN ('TGV', 'Corail');

-- i
SELECT t_num FROM train 
WHERE (t_type = 'TGV' AND wagon_r = 'oui' AND wagon_l = 'non')
OR (t_type = 'Corail' AND wagon_r = 'non' AND wagon_l = 'oui') ;