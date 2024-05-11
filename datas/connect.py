import psycopg2

# Connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="bda1",
    user="postgres",
    password="enter_votre_mot_de_passe"
)

"""# Création de la BDD
conn.autocommit = True
cursor = conn.cursor()
cursor.execute("CREATE DATABASE bda1;")"""
