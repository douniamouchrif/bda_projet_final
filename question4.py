from datas.connect import conn

cursor = conn.cursor()

#Faire en sorte que les tables REGIONS et DEPARTEMENTS ne soit pas modifiables.
#Il faut bloquer les commandes INSERT, UPDATE et DELETE.
query5 = """
REVOKE INSERT, UPDATE, DELETE ON Region FROM PUBLIC;
"""
query6 = """
REVOKE INSERT, UPDATE, DELETE ON Departement FROM PUBLIC;
"""
cursor.execute(query5)
cursor.execute(query6)

#Ajoutez un trigger qui utilise la procédure stockée précédente pour mettre à jour 
#la population d'un département/région quand la population d'une ville est mise à jour.

conn.commit()
conn.close()