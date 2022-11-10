import pandas as pd
import requests

# On crée une fonction qui va appeler l'api.
def recovery_url(categorie:str):
    https = "https://swapi.dev/api/"
    url = https + categorie
    if requests.get(url):
        reponse = requests.get(url)
        print("===> la requête s’est déroulée correctement")
    else:
        print("ERREUR : la requête s’est pas déroulée correctement")
    return reponse
