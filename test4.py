from datas.connect import conn
cursor = conn.cursor()

query9 = """update pop_commune set valeur = 13469  where num_com = '01009' and id_stat = 'D99_POP';"""
cursor.execute(query9)
##on peut voir que la valeur de Auvergne-Rhône-Alpes pour D99_POP s'est mise à jour.
query10 =  """SELECT num_reg , nom_reg, pop1999 FROM Region where num_reg = '84';"""
cursor.execute(query10)
results_2 = cursor.fetchall()

conn.commit()