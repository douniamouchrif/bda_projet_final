import psycopg2

# Connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    #port="5433",
    port="5432",
    database="bda1",
    user="postgres",
    password="dounia123"
    # password="mtissandier"
    #password="souabk"
)

"""# Création de la BDD
conn.autocommit = True
cursor = conn.cursor()
cursor.execute("CREATE DATABASE bda1;")"""
