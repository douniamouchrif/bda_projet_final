from connect import conn
import pandas as pd
from io import StringIO

cursor = conn.cursor()

df = pd.read_csv('datas/v_region_2023.csv')

df_region = df[['REG','LIBELLE','CHEFLIEU']]
df_region.columns = ['num_reg', 'nom_reg', 'chef_lieu'] #renommage des colonnes 


# Création d'un buffer mémoire
buffer = StringIO()
df_region.to_csv(buffer, sep='\t', header=False, index=False)
buffer.seek(0)

# Copie des données depuis le buffer vers la base de données
copy_query = """
    COPY Region(num_reg, nom_reg, chef_lieu)
    FROM STDIN DELIMITER '\t' CSV;
"""
cursor.copy_expert(sql=copy_query, file=buffer)

# Fermeture du curseur et de la connexion
cursor.close()
conn.commit()
conn.close()



