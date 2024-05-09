from datas.connect import conn
cursor = conn.cursor()

#print('Après la mise à jour dans Pop_Commune pour l'année 2020 pour la region Auvergne-Rhône-Alpes :')
cursor.execute("""update pop_commune set valeur = 4134  where num_com = '01009' and id_stat = 'P20_POP';""")

##on peut voir que la valeur de Auvergne-Rhône-Alpes pour D99_POP s'est mise à jour.
cursor.execute("""SELECT num_reg , nom_reg, pop2020 FROM Region where num_reg = '84';""")
results_6 = cursor.fetchall()

conn.commit()