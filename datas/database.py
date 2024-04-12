from connect import conn

# Création de la BDD
conn.autocommit = True
cursor = conn.cursor()

# Création des tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Region (
    num_reg INTEGER PRIMARY KEY,
    nom_reg TEXT NOT NULL,
    chef_lieu TEXT
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Departement (
    num_dep TEXT PRIMARY KEY,
    nom_dep TEXT NOT NULL,
    chef_lieu TEXT,
    num_reg INTEGER REFERENCES Region(num_reg)
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Commune (
    num_com TEXT PRIMARY KEY,
    nom_com TEXT NOT NULL,
    num_dep TEXT REFERENCES Departement(num_dep)
    );
""")

conn.commit()
cursor.close()
conn.close()
