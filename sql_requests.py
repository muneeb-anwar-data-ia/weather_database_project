URL_API = "https://goweather.xyz/weather/" #Début de l'url de l'API
DB_name = "european_weather.sqlite" #nom de la base de donnée

#Liste différentes villes européennes
cities_list = ["Paris", "Zurich", "Luxembourg", "London", "Istanbul", "Berlin", "Rome", "Bruxelles", "Amsterdam"]

#Creation de la table (3 colonnes: id, date_heure, meteo)
SQL_CREATION_TABLE = """
    CREATE TABLE IF NOT EXISTS european_weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_heure TEXT, city TEXT, meteo TEXT
    )"""

#Insertion des données
SQL_AJOUTER_PRIX = "INSERT INTO european_weather (date_heure, city, meteo) VALUES (?, ?, ?)"

#Lecture des données
SQL_LECTURE = "SELECT * FROM european_weather ORDER BY city, id ASC"