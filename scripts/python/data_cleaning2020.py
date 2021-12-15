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

# Import des fichiers eclates des valeurs foncieres de 2020 #
    # low_memory = False pour depasser la limite d'usage memoire
    # encoding = 'ISO-8859-1'
dvf_2020_1 = pd.read_csv("2020_1.txt", sep = "|", dtype = dtype_dico, low_memory = False, encoding = "ISO-8859-1")
dvf_2020_2 = pd.read_csv("2020_2.txt", sep = "|", dtype = dtype_dico, low_memory = False, encoding = "ISO-8859-1")
dvf_2020_3 = pd.read_csv("2020_3.txt", sep = "|", dtype = dtype_dico, low_memory = False, encoding = "ISO-8859-1")
dvf_2020_4 = pd.read_csv("2020_4.txt", sep = "|", dtype = dtype_dico, low_memory = False, encoding = "ISO-8859-1")
dvf_2020_5 = pd.read_csv("2020_5.txt", sep = "|", dtype = dtype_dico, low_memory = False, encoding = "ISO-8859-1")
dvf_2020_6 = pd.read_csv("2020_6.txt", sep = "|", dtype = dtype_dico, low_memory = False, encoding = "ISO-8859-1")
dvf_2020_7 = pd.read_csv("2020_7.txt", sep = "|", dtype = dtype_dico, low_memory = False, encoding = "ISO-8859-1")

# Dictionnaire des df pour concatenation
frames = [dvf_2020_1,dvf_2020_2,dvf_2020_3,dvf_2020_4,dvf_2020_5,dvf_2020_6,dvf_2020_7]
dvf_2020 = pd.concat(frames)
# Nettoyage de la memoire
gc.collect()

# Supression des colonnes inutiles
dvf_2020 = dvf_2020.drop(columns=['Code service CH', 'Reference document', '1 Articles CGI', '2 Articles CGI',
                                  '3 Articles CGI', '4 Articles CGI', '5 Articles CGI', '1er lot', 
                                  'Surface Carrez du 1er lot', '2eme lot', 'Surface Carrez du 2eme lot',
                                  '3eme lot', 'Surface Carrez du 3eme lot', '4eme lot', 'Surface Carrez du 4eme lot', 
                                  '5eme lot', 'Surface Carrez du 5eme lot', 'Nombre de lots', 'Identifiant local',
                                  'B/T/Q', "Nature culture speciale", "Code type local", "No plan", "No Volume"
                                  ])
                                  
# Ajout d'un 0 en debut de code postal / code departement pour les cas concernes
    # Code postal avec moins de 5 chiffres (4 chiffres ou il manque le 0 de debut)
dvf_2020["Code postal"] = dvf_2020["Code postal"].apply(lambda x: '0' + str(x) if len(str(x)) < 5 else str(x))
    # Code departemental avec moins de 2 chiffres (1 chiffre ou il manque le 0 de debut)
dvf_2020["Code departement"] = dvf_2020["Code departement"].apply(lambda x: '0' + str(x) if len(str(x)) < 2 else str(x))
gc.collect()

# Definition d'une fonction servant a remplacer la "," en "."
def replacee(s):
    i=str(s).find(',')
    if(i>0):
        return s[:i] + '.' + s[i+1:]
    else :
        return s 

# Application de la fonction "replacee" pour obtenir une valeur fonciere de la forme : 999.00
dvf_2020['Valeur fonciere'] = dvf_2020['Valeur fonciere'].apply(replacee)

# Chargement dans un .csv
dvf_2020.to_csv("dvf_2020.csv")