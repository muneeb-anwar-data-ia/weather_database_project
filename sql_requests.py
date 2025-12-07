URL_API = "https://goweather.xyz/weather/Liege" #Lien URL de l'API météo de Liège
DB_name = "liege_weather.sqlite" #nom de la base de donnée


#Creation de la table (3 colonnes: id, date_heure, meteo)
SQL_CREATION_TABLE = """
    CREATE TABLE IF NOT EXISTS Liege_weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_heure TEXT, meteo TEXT
    )"""

#Insertion des données
SQL_AJOUTER_PRIX = "INSERT INTO Liege_weather (date_heure, meteo) VALUES (?, ?)"

#Lecture des données
SQL_LECTURE = "SELECT * FROM Liege_weather ORDER BY id DESC"