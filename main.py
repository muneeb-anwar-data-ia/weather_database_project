import requests #Librarie de connexion APIs
import sqlite3 #Librairie de connexion base de donnée SQLite
import datetime #Librairie 'date et heure du jour'

from sql_requests import * #importation de mes variables et requetes SQL

def main():
    #Connexion à la base de donnée
    print(f"\nConnecting to {DB_name}")
    conn = sqlite3.connect(DB_name)
    cursor = conn.cursor()

    #Creation de la table
    cursor.execute(SQL_CREATION_TABLE) #Execute ce qu'il y'a dans cette variable
    conn.commit() #sauvegarde

    #Appel API
    print(f"\nRécupération de la météo...")
    response = requests.get(URL_API) #On place dans la variable ce que l'API nous renvoie

    if response.status_code == 200: #Si l'appel API a bien fonctionné
        data = response.json()  #On traduis la réponse et on la place dans data
        meteo = data['temperature'] #Je récupère ce qu'il y'a dans la clé température de la réponse data
        print(f"Météo actuelle : {meteo}")

    else:
        print('Problème API')
        meteo = "Erreur API"

    date_now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M") #On récupère la date et l'heure actuelle sous ce format
    cursor.execute(SQL_AJOUTER_PRIX, (date_now, meteo)) #On execute la requete SQL en remplaclant (?, ?) par ceci
    conn.commit() #sauvegarde

    if meteo != "Erreur API":
        print(f'Météo sauvegardée dans {DB_name} !')

    historique = input("\nVoulez vous consulter l'historique actuel [Y] ? ")

    if historique.lower() == 'y':
        print("\n ---HISTORIQUE---")
        cursor.execute(SQL_LECTURE) #Execute la requete SQL qui affiche chaque ligne de la base de donnée

        for ligne in cursor.fetchall(): #Pour chaque ligne cela va afficher de la manière suivante
            print(f"Date: {ligne[1]} | Weather: {ligne[2]}") # [1] correspond à la date et [2] à la meteo ([0] correspond à id)
        conn.close()

    print("\nFin de l'éxécution")


#Cette condition permet de lancer le script proprement
if __name__ == "__main__":
    main()