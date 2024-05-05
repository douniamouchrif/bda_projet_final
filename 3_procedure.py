from datas.connect import conn

cursor = conn.cursor()

# N'oubliez pas de modifier au préalable la structure de la base pour accueillir ces nouvelles informations.
# (sans utiliser la commande drop table)

# à executer une fois si on lance plusieurs fois le fichier le mettre en commentaire pour tester les versions

pop_dep = """ALTER TABLE Departement 
ADD COLUMN pop2020 BIGINT,
ADD COLUMN pop2014 BIGINT,
ADD COLUMN pop2009 BIGINT,
ADD COLUMN pop1999 BIGINT,
ADD COLUMN pop1990 BIGINT,
ADD COLUMN pop1982 BIGINT,
ADD COLUMN pop1975 BIGINT,
ADD COLUMN pop1968 BIGINT;"""

pop_reg = """ALTER TABLE Region 
ADD COLUMN pop2020 BIGINT,
ADD COLUMN pop2014 BIGINT,
ADD COLUMN pop2009 BIGINT,
ADD COLUMN pop1999 BIGINT,
ADD COLUMN pop1990 BIGINT,
ADD COLUMN pop1982 BIGINT,
ADD COLUMN pop1975 BIGINT,
ADD COLUMN pop1968 BIGINT;"""

cursor.execute(pop_dep)
cursor.execute(pop_reg)

# Écrivez une procédure stockée qui fait ce calcul à partir de la population des communes.

# VERSION 1 : avec l'utilisation des vues créées

query1 = """CREATE OR REPLACE PROCEDURE calcul_pop_dep_reg1()
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Departement d
    SET pop2020 = (SELECT SUM(population) FROM Pop_Dep WHERE num_departement = d.num_dep AND id_stat = 'P20_POP'),
        pop2014 = (SELECT SUM(population) FROM Pop_Dep WHERE num_departement = d.num_dep AND id_stat = 'P14_POP'),
        pop2009 = (SELECT SUM(population) FROM Pop_Dep WHERE num_departement = d.num_dep AND id_stat = 'P09_POP'),
        pop1999 = (SELECT SUM(population) FROM Pop_Dep WHERE num_departement = d.num_dep AND id_stat = 'D99_POP'),
        pop1990 = (SELECT SUM(population) FROM Pop_Dep WHERE num_departement = d.num_dep AND id_stat = 'D90_POP'),
        pop1982 = (SELECT SUM(population) FROM Pop_Dep WHERE num_departement = d.num_dep AND id_stat = 'D82_POP'),
        pop1975 = (SELECT SUM(population) FROM Pop_Dep WHERE num_departement = d.num_dep AND id_stat = 'D75_POP'),
        pop1968 = (SELECT SUM(population) FROM Pop_Dep WHERE num_departement = d.num_dep AND id_stat = 'D68_POP');

    UPDATE Region r
    SET pop2020 = (SELECT SUM(population) FROM Pop_Reg WHERE num_region = r.num_reg AND id_stat = 'P20_POP'),
        pop2014 = (SELECT SUM(population) FROM Pop_Reg WHERE num_region = r.num_reg AND id_stat = 'P14_POP'),
        pop2009 = (SELECT SUM(population) FROM Pop_Reg WHERE num_region = r.num_reg AND id_stat = 'P09_POP'),
        pop1999 = (SELECT SUM(population) FROM Pop_Reg WHERE num_region = r.num_reg AND id_stat = 'D99_POP'),
        pop1990 = (SELECT SUM(population) FROM Pop_Reg WHERE num_region = r.num_reg AND id_stat = 'D90_POP'),
        pop1982 = (SELECT SUM(population) FROM Pop_Reg WHERE num_region = r.num_reg AND id_stat = 'D82_POP'),
        pop1975 = (SELECT SUM(population) FROM Pop_Reg WHERE num_region = r.num_reg AND id_stat = 'D75_POP'),
        pop1968 = (SELECT SUM(population) FROM Pop_Reg WHERE num_region = r.num_reg AND id_stat = 'D68_POP');

END;
$$;"""
cursor.execute(query1)
cursor.execute("""CALL calcul_pop_dep_reg1()""")


# VERSION 2 : sans l'utilisation des vues créées

'''query2 = """CREATE OR REPLACE PROCEDURE calcul_pop_dep_reg2()
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Departement d
    SET pop2020 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'P20_POP'),
        pop2014 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'P14_POP'),
        pop2009 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'P09_POP'),
        pop1999 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'D99_POP'),
        pop1990 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'D90_POP'),
        pop1982 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'D82_POP'),
        pop1975 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'D75_POP'),
        pop1968 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'D68_POP');

    UPDATE Region r
    SET pop2020 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'P20_POP'),
        pop2014 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'P14_POP'),
        pop2009 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'P09_POP'),
        pop1999 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'D99_POP'),
        pop1990 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'D90_POP'),
        pop1982 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'D82_POP'),
        pop1975 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'D75_POP'),
        pop1968 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'D68_POP');

END;
$$;"""
cursor.execute(query2)
cursor.execute("""CALL calcul_pop_dep_reg2()""")'''

conn.commit()
conn.close()
