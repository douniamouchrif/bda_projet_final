from datas.connect import conn

# Connexion à la base de données
cursor = conn.cursor()

# Plan d'exécution de la 1ère requête
nom_region = 'Nouvelle-Aquitaine'
exe_query1 = f"""
    EXPLAIN ANALYZE 
    SELECT d.num_dep, d.nom_dep, d.chef_lieu
    FROM Departement d
    JOIN Region r ON d.num_reg = r.num_reg
    WHERE r.nom_reg = '{nom_region}';
"""
cursor.execute(exe_query1)
explain_results_1 = cursor.fetchall()

"""for row in explain_results_1:
    print(row)
print()"""

'''analyse 1ère requête : 
- Utilisation d'une jointure entre Departement et Region basée sur num_reg.
- Filtre sur nom_reg = 'Nouvelle-Aquitaine'.
- Exécution efficace avec un coût faible (cost=0.16..18.63) et un temps d'exécution rapide (Execution Time: 0.163 ms).'''

# Plan d'exécution de la 2ème requête
num_dep = '33'
seuil_population = 30000
exe_query2 = f"""
    EXPLAIN ANALYZE 
    SELECT c.num_com, c.nom_com, pc.valeur AS population
    FROM Commune c
    JOIN Pop_Commune pc ON c.num_com = pc.num_com
    WHERE c.num_dep = '{num_dep}' AND pc.valeur > {seuil_population} AND pc.id_stat = 'P20_POP'
    ORDER BY pc.valeur DESC;
"""
cursor.execute(exe_query2)
explain_results_2 = cursor.fetchall()

"""for row in explain_results_2:
    print(row)
print()"""

'''analyse 2ème requête :
- Filtre sur num_dep = '33' et pc.valeur > 30000 dans une jointure entre Commune et Pop_Commune.
- Utilisation d'un tri par ordre décroissant des résultats (ORDER BY pc.valeur DESC).
- Le tri prend le plus de temps dans le temps total (Execution Time: 21.796 ms).'''

# Plan d'exécution de la 3ème requête
exe_query3 = """
    EXPLAIN ANALYZE 
    SELECT r.nom_reg, SUM(pc.valeur) AS population_totale
    FROM Region r
    JOIN Departement d ON r.num_reg = d.num_reg
    JOIN Commune c ON d.num_dep = c.num_dep
    JOIN Pop_Commune pc ON c.num_com = pc.num_com
    GROUP BY r.nom_reg
    ORDER BY population_totale DESC
    LIMIT 1;
"""
cursor.execute(exe_query3)
explain_results_3 = cursor.fetchall()

"""for row in explain_results_3:
    print(row)
print()"""

'''analyse 3ème requête :
- Agrégation par nom_reg avec SUM(pc.valeur) pour calculer la population totale par région.
- Utilisation de tri par ordre décroissant (ORDER BY population_totale DESC) et de limit (LIMIT 1).
- Coût élevé en raison de l'agrégation sur de grandes données de commune et pop_commune (cost=14377.66..14377.66).'''

# Plan d'exécution de la 4ème requête
exe_query4 = """
    EXPLAIN ANALYZE 
    SELECT r.nom_reg, SUM(pc.valeur) AS population_totale
    FROM Region r
    JOIN Departement d ON r.num_reg = d.num_reg
    JOIN Commune c ON d.num_dep = c.num_dep
    JOIN Pop_Commune pc ON c.num_com = pc.num_com
    GROUP BY r.nom_reg
    ORDER BY population_totale ASC
    LIMIT 1;
"""
cursor.execute(exe_query4)
explain_results_4 = cursor.fetchall()

"""for row in explain_results_4:
    print(row)
print()"""

'''analyse 4ème requête :
- Similaire à la requête 3 mais avec un tri différent, il est par ordre croissant (ORDER BY population_totale ASC).
- Coût autant élevé en raison de l'agrégation sur de grandes données (cost=14377.66..14377.66).'''

# Plan d'exécution de la 5ème requête
code_departement = '33'
exe_query5 = """
    EXPLAIN ANALYZE 
    SELECT c.nom_com, pc.valeur AS population
    FROM Commune c
    JOIN Pop_Commune pc ON c.num_com = pc.num_com
    WHERE c.num_dep = %s AND pc.id_stat = 'P20_POP'
    ORDER BY pc.valeur DESC
    LIMIT 10;
"""
cursor.execute(exe_query5, (code_departement,))
explain_results_5 = cursor.fetchall()

"""for row in explain_results_5:
    print(row)
print()"""

'''analyse 5ème requête :
- Filtres sur c.num_dep = '33' et pc.id_stat = 'P20_POP'.
- Tri de pc.valeur par ordre décroissant (ORDER BY pc.valeur DESC).
- Temps d'exécution assez rapide (Execution Time: 2.172 ms).'''

# Plan d'exécution de la 6ème requête
code_departement = '33'
exe_query6 = """
    EXPLAIN ANALYZE 
    SELECT c.nom_com, pc.valeur AS population
    FROM Commune c
    JOIN Pop_Commune pc ON c.num_com = pc.num_com
    WHERE c.num_dep = %s AND pc.id_stat = 'P20_POP'
    ORDER BY pc.valeur ASC
    LIMIT 10;
"""
cursor.execute(exe_query6, (code_departement,))
explain_results_6 = cursor.fetchall()

"""for row in explain_results_6:
    print(row)
print()
"""
'''analyse 6ème requête :
- Similaire à la requête 5 mais avec un tri différent, il est par ordre croissant (ORDER BY population_totale ASC).
- Temps d'exécution aussi rapide (Execution Time: 1.986 ms).'''

# Plan d'exécution de la 7ème requête
code_departement = '1177'
exe_query7 = """
    EXPLAIN ANALYZE 
    SELECT type_couple, SUM(nb_mar) AS total_mariages
    FROM Stats_Mar1
    WHERE dep = %s AND id_stat = 'MAR21AGE_2'
    GROUP BY type_couple
    ORDER BY total_mariages DESC;
"""
cursor.execute(exe_query7, (code_departement,))
explain_results_7 = cursor.fetchall()

"""for row in explain_results_7:
    print(row)
print()"""

'''analyse 7ème requête :
- Agrégation par type_couple avec SUM(nb_mar) pour obtenir le total de mariages par type de couple dans un département spécifique.
- Filtre sur dep = '1177' et id_stat = 'MAR21AGE_2'.
- Exécution rapide (Execution Time: 0.514 ms).'''


'''analyse générale :
- Toutes les requêtes ont des jointures entre au moins deux tables, parfois plus. Ces jointures peuvent être un point critique pour les performances.
- Chaque requête comporte des "WHERE" qui filtrent les données en fonction de certaines conditions.
- Plusieurs requêtes utilisent des fonctions d'agrégation comme SUM pour calculer des effectifs totaux.
- Certaines requêtes ont un tri des résultats, soit pour présenter les données (ORDER BY), soit pour limiter le nombre de résultats (LIMIT).

Pour conclure, les requêtes ont des schémas d'accès aux données similaires mais avec des besoins de traitement différents selon ceux rappelés ci-dessus. 
Une attention aux détails d'indexation, d'optimisation des requêtes ou encore des performances, 
contribuera à améliorer les performances de notre système de base de données.'''

cursor.close()
#conn.close()
