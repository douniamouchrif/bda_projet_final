# bda_projet_final

 étape 1 : 
    - si la database n'est pas créée :
        * connect.py : Création de la bdd + Connexion à la base de données
    - si la database est déjà créée :
        * connect.py : Connexion à la base de données

étape 2 : 
    - si les tables ne sont pas créées :
        * créer les tables avec database.py (lancer le fichier) -> pour voir si elles sont bien créées, on peut regarder à l'aide de pgAdmin 
    - si les tables sont déjà créées :
        * passer à l'étape 3

étape 3 : 
    - si les données n'ont pas été importées :
        * importer les données dans les tables avec import_data.py (lancer le fichier) -> pour voir si elles ont bien été importées, on peut regarder à l'aide du terminal SQL shell (voir l'intermède 1) 
    - si les tables sont déjà créées :
        * passer à l'étape 4

intermède 1 (terminal SQL shell) :
    - utiliser notre base de données : \c bda1
    - visionner les tables créées : \dt
    - voir le contenu d'une table : select * from region;

pour drop les tables à partir du terminale :
drop table stats_mar1 ;
drop table stats_mar2 ;
drop table stats_mar3 ;
drop table stats_mar4 ;
drop table pop_commune;
drop table stats_var ;
drop table commune;
drop table departement;
drop table region;