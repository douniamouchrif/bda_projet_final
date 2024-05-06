from datas.connect import conn

cursor = conn.cursor()

#Faire en sorte que les tables REGIONS et DEPARTEMENTS ne soit pas modifiables.
#Il faut bloquer les commandes INSERT, UPDATE et DELETE.
query5 = f"""
REVOKE INSERT, UPDATE, DELETE ON Region FROM PUBLIC;
"""
query6 = """
REVOKE INSERT, UPDATE, DELETE ON Departement FROM PUBLIC;
"""
cursor.execute(query5)
cursor.execute(query6)

#Ajoutez un trigger qui utilise la procédure stockée précédente pour mettre à jour 
#la population d'un département/région quand la population d'une ville est mise à jour.

query7 = """
CREATE OR REPLACE FUNCTION maj_pop()
RETURNS TRIGGER AS $$
BEGIN
    CALL calcul_pop_dep_reg2();
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_maj_pop
AFTER INSERT OR UPDATE OR DELETE ON Pop_Commune
FOR EACH STATEMENT EXECUTE FUNCTION maj_pop();
"""
cursor.execute(query7) 


### TEST pour vérifier que le trigger se déclanche bien (ou alors on pourra mettre juste un screen de la sortie du terminale)
 
cursor.execute("""SELECT num_reg , nom_reg, pop1999 FROM Region where num_reg = '84';""")
results_1 = cursor.fetchall()
for row in results_1:
    print(row)
cursor.execute("""update pop_commune set valeur = 6543  where num_com = '01009' and id_stat = 'D99_POP';""")
##on peut voir que la valeur de Auvergne-Rhône-Alpes pour D99_POP s'est mise à jour.
cursor.execute("""SELECT num_reg , nom_reg, pop1999 FROM Region where num_reg = '84';""")
results_2 = cursor.fetchall()
for row in results_2:
    print(row)

conn.commit()