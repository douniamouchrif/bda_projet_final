from datas.connect import conn
cursor = conn.cursor()

pop_dep = """ALTER TABLE Departement 
ADD COLUMN pop1999 BIGINT,
ADD COLUMN pop1990 BIGINT,
ADD COLUMN pop1982 BIGINT,
ADD COLUMN pop1975 BIGINT,
ADD COLUMN pop1968 BIGINT;"""

pop_reg = """ALTER TABLE Region 
ADD COLUMN pop1999 BIGINT,
ADD COLUMN pop1990 BIGINT,
ADD COLUMN pop1982 BIGINT,
ADD COLUMN pop1975 BIGINT,
ADD COLUMN pop1968 BIGINT;"""

query1 = """CREATE OR REPLACE PROCEDURE calcul_pop_dep_reg1()
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Departement d
    SET pop1999 = (SELECT SUM(population) FROM Pop_Dep WHERE num_departement = d.num_dep AND id_stat = 'D99_POP'),
        pop1990 = (SELECT SUM(population) FROM Pop_Dep WHERE num_departement = d.num_dep AND id_stat = 'D90_POP'),
        pop1982 = (SELECT SUM(population) FROM Pop_Dep WHERE num_departement = d.num_dep AND id_stat = 'D82_POP'),
        pop1975 = (SELECT SUM(population) FROM Pop_Dep WHERE num_departement = d.num_dep AND id_stat = 'D75_POP'),
        pop1968 = (SELECT SUM(population) FROM Pop_Dep WHERE num_departement = d.num_dep AND id_stat = 'D68_POP');

    UPDATE Region r
    SET pop1999 = (SELECT SUM(population) FROM Pop_Reg WHERE num_region = r.num_reg AND id_stat = 'D99_POP'),
        pop1990 = (SELECT SUM(population) FROM Pop_Reg WHERE num_region = r.num_reg AND id_stat = 'D90_POP'),
        pop1982 = (SELECT SUM(population) FROM Pop_Reg WHERE num_region = r.num_reg AND id_stat = 'D82_POP'),
        pop1975 = (SELECT SUM(population) FROM Pop_Reg WHERE num_region = r.num_reg AND id_stat = 'D75_POP'),
        pop1968 = (SELECT SUM(population) FROM Pop_Reg WHERE num_region = r.num_reg AND id_stat = 'D68_POP');

END;
$$;"""

query2 = """CREATE OR REPLACE PROCEDURE calcul_pop_dep_reg2()
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Departement d
    SET pop1999 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'D99_POP'),
        pop1990 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'D90_POP'),
        pop1982 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'D82_POP'),
        pop1975 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'D75_POP'),
        pop1968 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'D68_POP');

    UPDATE Region r
    SET pop1999 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'D99_POP'),
        pop1990 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'D90_POP'),
        pop1982 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'D82_POP'),
        pop1975 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'D75_POP'),
        pop1968 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'D68_POP');

END;
$$;"""

query5 = f"""
REVOKE INSERT, UPDATE, DELETE ON Region FROM PUBLIC;
"""
query6 = """
REVOKE INSERT, UPDATE, DELETE ON Departement FROM PUBLIC;
"""

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

### TEST pour vérifier que le trigger se déclanche bien 
query8 = """SELECT num_reg , nom_reg, pop1999 FROM Region where num_reg = '84';"""
cursor.execute(query8)
results_1 = cursor.fetchall()

#Procédure stockée pour calculer la population des départements des 3 nouvelles années 
query11 = """CREATE OR REPLACE PROCEDURE calcul_pop_departements_new_years()
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Departement d
    SET pop2020 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'P20_POP'),
        pop2014 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'P14_POP'),
        pop2009 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'P09_POP');
END;
$$;"""

#Procédure stockée pour calculer la population des régions des 3 nouvelles années 
query12 = """CREATE OR REPLACE PROCEDURE calcul_pop_regions_new_years()
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Region r
    SET pop2020 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'P20_POP'),
        pop2014 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'P14_POP'),
        pop2009 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'P09_POP');
END;
$$;
"""

### procedure pour update les populations reg et dep maintenant qu'il y a toutes les années si il ya des modifications dans Pop_communes 
query13 = """CREATE OR REPLACE PROCEDURE calcul_pop_dep_reg_new_years()
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

#trigger qui déclanche la procédure
query14 = """
CREATE OR REPLACE FUNCTION maj_pop_ny()
RETURNS TRIGGER AS $$
BEGIN
    CALL calcul_pop_dep_reg_new_years();
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_maj_pop_ny
AFTER INSERT OR UPDATE OR DELETE ON Pop_Commune
FOR EACH STATEMENT EXECUTE PROCEDURE maj_pop_ny();
"""

#appel des procedures stockées

#Après ajout des 3 années dans Pop_Commune :
query15 = """CALL calcul_pop_departements_new_years()"""
query16 ="""CALL calcul_pop_regions_new_years()"""
#on peut voir que les données pour les 3 années se sont ajoutés 
query17 = """SELECT * FROM REGION WHERE num_reg = '75' OR num_reg = '84';"""
cursor.execute(query17)
results_4 = cursor.fetchall()

#test modification d'une ligne de Pop_commune
#print('Avant la mise à jour dans Pop_Commune pour l'année 2020 pour la region Auvergne-Rhône-Alpes :')
cursor.execute("""SELECT num_reg , nom_reg, pop2020 FROM Region where num_reg = '84';""")
results_5 = cursor.fetchall()

conn.commit()