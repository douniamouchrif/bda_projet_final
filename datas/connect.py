import psycopg2

# Connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="bddd",
    user="postgres",
    password="souabk"
)

# Création de la BDD
conn.autocommit = True
cursor = conn.cursor()
cursor.execute("CREATE DATABASE testtt;")
