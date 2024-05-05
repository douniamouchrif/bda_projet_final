from datas.connect import conn

# Connexion à la base de données
cursor = conn.cursor()


# 1ère requête SQL : liste des départements d'une région donnée
nom_region = 'Nouvelle-Aquitaine'
query_1 = f"""
    SELECT d.num_dep, d.nom_dep, d.chef_lieu
    FROM Departement d
    JOIN Region r ON d.num_reg = r.num_reg
    WHERE r.nom_reg = '{nom_region}';
"""
cursor.execute(query_1)
results_1 = cursor.fetchall()

"""print(f"Liste des départements de la région '{nom_region}':")
for row in results_1:
    num_dep, nom_dep, chef_lieu = row
    print(f"- Département {num_dep}: {nom_dep} (Chef-lieu: {chef_lieu})")
print()"""


# 2ème requête SQL : liste des communes de plus de X habitants d'un département donné en 2020
num_dep = '33'
seuil_population = 30000
query_2 = f"""
    SELECT c.num_com, c.nom_com, pc.valeur AS population
    FROM Commune c
    JOIN Pop_Commune pc ON c.num_com = pc.num_com
    WHERE c.num_dep = '{num_dep}' AND pc.valeur > {seuil_population} AND pc.id_stat = 'P20_POP'
    ORDER BY pc.valeur DESC;
"""
cursor.execute(query_2)
results_2 = cursor.fetchall()

"""print(
    f"Liste des communes de plus de {seuil_population} habitants dans le département '{num_dep}' en 2020:")
for row in results_2:
    num_com, nom_com, population = row
    print(
        f"- Commune {num_com}: {nom_com} (Population: {population} habitants)")
print()"""


# 3ème requête SQL : la région la plus peuplée
query_3 = """
    SELECT r.nom_reg, SUM(pc.valeur) AS population_totale
    FROM Region r
    JOIN Departement d ON r.num_reg = d.num_reg
    JOIN Commune c ON d.num_dep = c.num_dep
    JOIN Pop_Commune pc ON c.num_com = pc.num_com
    GROUP BY r.nom_reg
    ORDER BY population_totale DESC
    LIMIT 1;
"""
cursor.execute(query_3)
result_3 = cursor.fetchone()

"""if result_3 is not None:
    print("Région la plus peuplée:")
    print(f"Nom de la région: {result_3[0]}")
    print(f"Population totale: {result_3[1]} habitants")
else:
    print("Aucune région n'a été trouvée.")
print()"""

# 4ème requête SQL : la région la moins peuplée
query_4 = """
    SELECT r.nom_reg, SUM(pc.valeur) AS population_totale
    FROM Region r
    JOIN Departement d ON r.num_reg = d.num_reg
    JOIN Commune c ON d.num_dep = c.num_dep
    JOIN Pop_Commune pc ON c.num_com = pc.num_com
    GROUP BY r.nom_reg
    ORDER BY population_totale ASC
    LIMIT 1;
"""
cursor.execute(query_4)
result_4 = cursor.fetchone()

"""if result_4 is not None:
    print("Région la moins peuplée:")
    print(f"Nom de la région: {result_4[0]}")
    print(f"Population totale: {result_4[1]} habitants")
else:
    print("Aucune région n'a été trouvée.")
print()
"""

# 5ème requête SQL : les 10 communes les plus peuplées d'un département en 2020
code_departement = '33'
query_5 = """
    SELECT c.nom_com, pc.valeur AS population
    FROM Commune c
    JOIN Pop_Commune pc ON c.num_com = pc.num_com
    WHERE c.num_dep = %s AND pc.id_stat = 'P20_POP'
    ORDER BY pc.valeur DESC
    LIMIT 10;
"""
cursor.execute(query_5, (code_departement,))
results_5 = cursor.fetchall()

"""print(
    f"Communes les plus peuplées du département '{code_departement}' en 2020:")
for commune, population in results_5:
    print(f"{commune}: {population} habitants")
print()"""

# 6ème requête SQL : les 10 communes les moins peuplées d'un département en 2020
code_departement = '33'
query_6 = """
    SELECT c.nom_com, pc.valeur AS population
    FROM Commune c
    JOIN Pop_Commune pc ON c.num_com = pc.num_com
    WHERE c.num_dep = %s AND pc.id_stat = 'P20_POP'
    ORDER BY pc.valeur ASC
    LIMIT 10;
"""
cursor.execute(query_6, (code_departement,))
results_6 = cursor.fetchall()

"""print(
    f"Communes les moins peuplées du département '{code_departement}' en 2020:")
for commune, population in results_6:
    print(f"{commune}: {population} habitants")
print()"""


# 7ème requête : le nombre total de mariages pour la 1ère fois par type de couple dans le département spécifié
code_departement = '1177'
query_7 = """
    SELECT type_couple, SUM(nb_mar) AS total_mariages
    FROM Stats_Mar1
    WHERE dep = %s AND id_stat = 'MAR21AGE_2'
    GROUP BY type_couple
    ORDER BY total_mariages DESC;
"""
cursor.execute(query_7, (code_departement,))
results_7 = cursor.fetchall()

"""print(
    f"Nombre total de mariages par type de couple dans le département '{code_departement}':")
for type_couple, total_mariages in results_7:
    print(f"{type_couple}: {total_mariages} mariages")"""


