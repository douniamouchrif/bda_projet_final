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


# Données Pop_Commune

cursor.close()
conn.commit()
conn.close()
