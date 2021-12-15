# Valeurs foncieres en France (2017-2020)

# Table of Contents
1. [Sources de données](#sources)
2. [Nettoyage de données](#nettoyage)
3. [Stockage sous SQL Server](#SQL_Server)
    1.  [Docker](#Docker)
    2.  [SQL Server Management Studio](#SSMS)
4. [Analysis](#Analysis)
5. [Visualisation](#Visualisation)

# Sources de données <a name="sources"></a>

Les données ont été récupérées sur le site data-gouv.fr : https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/.

Ces données comprennent 4 fichiers texte pour les années 2017, 2018, 2019 et 2020.

# Nettoyage de données <a name="nettoyage"></a>

Les fichiers texte de chaque année contenant plus de 3 millions de lignes, il a été nécessaire de spliter ceux-ci pour permettre de ne pas avoir d'erreur  de type *"out of memory"* durant l'exécution des traitements de cleaning.

Les scripts Python ont servi à effectuer un reformatage des données et à obtenir en sortie des .csv (un pour chaque année). 

Ces scripts sont disponibles dans */scripts/python/*.

# Stockage sous SQL Server <a name="SQL_Server"></a>

## Docker <a name="Docker"></a>

Docker a été utilisé pour monter une image SQL Server. Il a suffit d'ouvrir PowerShell et d'exécuter les deux commandes suivantes : 
- ```docker pull mcr.microsoft.com/mssql/server:2019-CU14-ubuntu-20.04```
- ```docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=<my_password>" -e "MSSQL_PID=Express" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-CU14-ubuntu-20.04```

Documentation : https://hub.docker.com/_/microsoft-mssql-server.

## SQL Server Management Studio <a name="SSMS"></a>

Une fois l'image de SQL Server en place, j'ai du téléchargé un logiciel pour pouvoir le gérer : Microsoft SQL Server Management Studio 18 - https://docs.microsoft.com/fr-fr/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15.

J'ai crée une nouvelle database : *DVF*. Puis insérer chacun de mes flat files (.csv) dans une table correspondante (ex : *dvf_2017*).

# Analysis

# Visualization 

