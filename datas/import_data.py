from connect import conn
import pandas as pd
from io import StringIO

# Connextion à la BDD
cursor = conn.cursor()

# Données Region
df_reg = pd.read_csv('datas/files/v_region_2023.csv')
df_region = df_reg[['REG', 'LIBELLE', 'CHEFLIEU']]
df_region.columns = ['num_reg', 'nom_reg',
                     'chef_lieu']  # renommage des colonnes

buffer_reg = StringIO()  # création d'un buffer mémoire
df_region.to_csv(buffer_reg, sep='\t', header=False, index=False)
buffer_reg.seek(0)

copy_query = """
    COPY Region(num_reg, nom_reg, chef_lieu)
    FROM STDIN DELIMITER '\t' CSV;
"""
cursor.copy_expert(
    sql=copy_query, file=buffer_reg)  # copie des données depuis le buffer vers la bdd

# Données Departement
df_dep = pd.read_csv('datas/files/v_departement_2023.csv')
df_departement = df_dep[['DEP', 'LIBELLE', 'CHEFLIEU', 'REG']]
df_departement.columns = ['num_dep', 'nom_dep',
                          'chef_lieu', 'num_reg']

buffer_dep = StringIO()
df_departement.to_csv(buffer_dep, sep='\t', header=False, index=False)
buffer_dep.seek(0)

copy_query = """
    COPY Departement(num_dep, nom_dep, chef_lieu, num_reg)
    FROM STDIN DELIMITER '\t' CSV;
"""
cursor.copy_expert(
    sql=copy_query, file=buffer_dep)

# Données Commune
df_com = pd.read_csv('datas/files/v_commune_2023.csv')
# on filtre les lignes où 'TYPECOM' est égal à 'COM'
df_commune = df_com[df_com['TYPECOM'] == 'COM'][['COM', 'LIBELLE', 'DEP']]
df_commune.columns = ['num_com', 'nom_com', 'num_dep']

buffer_com = StringIO()
df_commune.to_csv(buffer_com, sep='\t', header=False, index=False)
buffer_com.seek(0)

copy_query = """
    COPY Commune(num_com, nom_com, num_dep)
    FROM STDIN DELIMITER '\t' CSV;
"""
cursor.copy_expert(sql=copy_query, file=buffer_com)

# Données Stats_var
data_to_insert = [
    ('P20_POP', 2020, 2020, 'Population en 2020'),
    ('P14_POP', 2014, 2014, 'Population en 2014'),
    ('P09_POP', 2009, 2009, 'Population en 2009'),
    ('D99_POP', 1999, 1999, 'Population en 1999'),
    ('D90_POP', 1990, 1990, 'Population sans les doubles comptes en 1990'),
    ('D82_POP', 1982, 1982, 'Population sans les doubles comptes en 1982'),
    ('D75_POP', 1975, 1975,
     'Population sans les doubles comptes en 1975 (en 1974 pour les DOM)'),
    ('D68_POP', 1968, 1968,
     'Population sans les doubles comptes en 1968 (en 1967 pour les DOM)'),
    ('NAIS1420', 2014, 2020, 'Nombre de naissances entre 2014 et 2020'),
    ('NAIS0914', 2009, 2014, 'Nombre de naissances entre 2009 et 2014'),
    ('NAIS9909', 1999, 2009, 'Nombre de naissances entre 1999 et 2009'),
    ('NAIS9099', 1990, 1999, 'Nombre de naissances entre 1990 et 1999'),
    ('NAIS8290', 1982, 1990, 'Nombre de naissances entre 1982 et 1990'),
    ('NAIS7582', 1975, 1982,
     'Nombre de naissances entre 1975 (en 1974 pour les DOM) et 1982'),
    ('NAIS6875', 1968, 1975,
     'Nombre de naissances entre 1968 et 1975 (en 1967 et 1974 pour les DOM)'),
    ('DECE1420', 2014, 2020, 'Nombre de décès entre 2014 et 2020'),
    ('DECE0914', 2009, 2014, 'Nombre de décès entre 2009 et 2014'),
    ('DECE9909', 1999, 2009, 'Nombre de décès entre 1999 et 2009'),
    ('DECE9099', 1990, 1999, 'Nombre de décès entre 1990 et 1999'),
    ('DECE8290', 1982, 1990, 'Nombre de décès entre 1982 et 1990'),
    ('DECE7582', 1975, 1982, 'Nombre de décès entre 1975 (en 1974 pour les DOM) et 1982'),
    ('DECE6875', 1968, 1975,
     'Nombre de décès entre 1968 et 1975 (en 1967 et 1974 pour les DOM)')
]

for row in data_to_insert:
    id_stat, annee_debut, annee_fin, libelle = row
    cursor.execute("""
        INSERT INTO Stats_Var (id_stat, annee_debut, annee_fin, libelle)
        VALUES (%s, %s, %s, %s);
    """, (id_stat, annee_debut, annee_fin, libelle))

# Données Pop_Commune

cursor.close()
conn.commit()
conn.close()
