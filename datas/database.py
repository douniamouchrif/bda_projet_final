from connect import conn

# Création de la BDD
conn.autocommit = True
cursor = conn.cursor()

# Création des tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Specialite (
    id_s SERIAL PRIMARY KEY,
    nom TEXT NOT NULL,
    sysAnatomique TEXT NOT NULL
    );
""")

conn.commit()
cursor.close()
conn.close()
