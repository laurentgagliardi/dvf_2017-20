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

# Import des fichiers eclates des valeurs foncieres de 2017 #
    # low_memory = False pour depasser la limite d'usage memoire
    # encoding = 'ISO-8859-1'
dvf_2017_1 = pd.read_csv("2017_1.txt", sep = "|", dtype = dtype_dico, low_memory = False, encoding = "ISO-8859-1")
dvf_2017_2 = pd.read_csv("2017_2.txt", sep = "|", dtype = dtype_dico, low_memory = False, encoding = "ISO-8859-1")
dvf_2017_3 = pd.read_csv("2017_3.txt", sep = "|", dtype = dtype_dico, low_memory = False, encoding = "ISO-8859-1")
dvf_2017_4 = pd.read_csv("2017_4.txt", sep = "|", dtype = dtype_dico, low_memory = False, encoding = "ISO-8859-1")
dvf_2017_5 = pd.read_csv("2017_5.txt", sep = "|", dtype = dtype_dico, low_memory = False, encoding = "ISO-8859-1")
dvf_2017_6 = pd.read_csv("2017_6.txt", sep = "|", dtype = dtype_dico, low_memory = False, encoding = "ISO-8859-1")
dvf_2017_7 = pd.read_csv("2017_7.txt", sep = "|", dtype = dtype_dico, low_memory = False, encoding = "ISO-8859-1")

# Dictionnaire des df pour concatenation
frames = [dvf_2017_1,dvf_2017_2,dvf_2017_3,dvf_2017_4,dvf_2017_5,dvf_2017_6,dvf_2017_7]
dvf_2017 = pd.concat(frames)
# Nettoyage de la memoire
gc.collect()

# Definition d'une fonction servant a remplacer la "," en "."
def replacee(s):
    i=str(s).find(',')
    if(i>0):
        return s[:i] + '.' + s[i+1:]
    else :
        return s 

# Supression des colonnes inutiles
dvf_2017 = dvf_2017.drop(columns=['Code service CH', 'Reference document', '1 Articles CGI', '2 Articles CGI',
                                  '3 Articles CGI', '4 Articles CGI', '5 Articles CGI', '1er lot', 
                                  'Surface Carrez du 1er lot', '2eme lot', 'Surface Carrez du 2eme lot',
                                  '3eme lot', 'Surface Carrez du 3eme lot', '4eme lot', 'Surface Carrez du 4eme lot', 
                                  '5eme lot', 'Surface Carrez du 5eme lot', 'Nombre de lots', 'Identifiant local',
                                  'B/T/Q', "Nature culture speciale", "Code type local", "No plan", "No Volume"
                                  ])

# Ajout d'un 0 en début de code postal / code departement pour les cas concernes
    # Code postal avec moins de 5 chiffres (4 chiffres ou il manque le 0 de debut)
dvf_2017["Code postal"] = dvf_2017["Code postal"].apply(lambda x: '0' + str(x) if len(str(x)) < 5 else str(x))
    # Code departemental avec moins de 2 chiffres (1 chiffre ou il manque le 0 de debut)
dvf_2017["Code departement"] = dvf_2017["Code departement"].apply(lambda x: '0' + str(x) if len(str(x)) < 2 else str(x))

# Application de la fonction "replacee" pour obtenir une valeur fonciere de la forme : 999.00
dvf_2017['Valeur fonciere'] = dvf_2017['Valeur fonciere'].apply(replacee)
gc.collect()

# Chargement dans un .csv
dvf_2017.to_csv("dvf_2017.csv")