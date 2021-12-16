import pandas as pd
import numpy as np
import gc

# Dictionnaire des colonnes a caster en string
dtype_dico = {"No disposition" : str,
              "No voie" : str,
              "Code voie" : str,
              "Code postal" : str, 
              "Nombre pieces principales" : str,
              }

# Liste des noms de fichiers texte splites.
listetxt = ['2019_1','2019_2','2019_3','2019_4','2019_5','2019_6','2019_7','2019_8']
file_name = '{}.txt'
df_list = []

# Import des fichiers eclates des valeurs foncieres de 2017 #
    # low_memory = False pour depasser la limite d'usage memoire
    # encoding = 'ISO-8859-1'
dvf_2019 = pd.concat([pd.read_csv(file_name.format(i), sep = "|", dtype = dtype_dico, low_memory = False, encoding = "ISO-8859-1") for i in listetxt])

# Nettoyage de la memoire
gc.collect()

# Supression des colonnes inutiles
dvf_2019 = dvf_2019.drop(columns=['Code service CH', 'Reference document', '1 Articles CGI', '2 Articles CGI',
                                  '3 Articles CGI', '4 Articles CGI', '5 Articles CGI', '1er lot', 
                                  'Surface Carrez du 1er lot', '2eme lot', 'Surface Carrez du 2eme lot',
                                  '3eme lot', 'Surface Carrez du 3eme lot', '4eme lot', 'Surface Carrez du 4eme lot', 
                                  '5eme lot', 'Surface Carrez du 5eme lot', 'Nombre de lots', 'Identifiant local',
                                  'B/T/Q', "Nature culture speciale", "Code type local", "No plan", "No Volume"
                                  ])

# Ajout d'un 0 en debut de code postal / code departement pour les cas concernes
    # Code postal avec moins de 5 chiffres (4 chiffres ou il manque le 0 de debut)
dvf_2019["Code postal"] = dvf_2019["Code postal"].apply(lambda x: '0' + str(x) if len(str(x)) < 5 else str(x))
    # Code departemental avec moins de 2 chiffres (1 chiffre ou il manque le 0 de debut)
dvf_2019["Code departement"] = dvf_2019["Code departement"].apply(lambda x: '0' + str(x) if len(str(x)) < 2 else str(x))
gc.collect()

# Definition d'une fonction servant a remplacer la "," en "."
def replacee(s):
    i=str(s).find(',')
    if(i>0):
        return s[:i] + '.' + s[i+1:]
    else :
        return s 

# Application de la fonction "replacee" pour obtenir une valeur fonciere de la forme : 999.00
dvf_2019['Valeur fonciere'] = dvf_2019['Valeur fonciere'].apply(replacee)

# Chargement dans un .csv
dvf_2019.to_csv("dvf_2019.csv")