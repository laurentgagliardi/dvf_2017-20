# Valeurs foncieres en France (2017-2020)

# Table of Contents
1. [Sources de données](#sources)
2. [Nettoyage de données](#nettoyage)
3. [Stockage sous SQL Server](#SQL_Server)
    1.  [Docker](#Docker)
    2.  [SQL Server Management Studio](#SSMS)
4. [Visualisation avec Power BI](#Visualisation)
    1.  [Connexion SQL Server](#Power_BI_SQL_Server)
6. [Analysis](#Analysis)


# Sources de données <a name="sources"></a>

Les données ont été récupérées sur le site data-gouv.fr : https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/.

La base de données DVF recense les mutations à titre onéreux (vente, vente en l'état futur d'achèvement, vente terrain à bâtir, échange, adjudication, expropriation) advenues sur les années de 2017 à 2020.

Les données obtenues sont constituées de 4 fichiers texte (un pour chaque année).

<img src="/img/Source_files/file_text.png" width="800" height="500">

# Nettoyage de données <a name="nettoyage"></a>

Les fichiers texte de chaque année contenant plus de 3 millions de lignes, il a été nécessaire de spliter ceux-ci avec *Notepad++* pour permettre de ne pas avoir d'erreur  de type *"out of memory"* durant l'exécution des traitements de cleaning.

Les scripts Python ont servi à effectuer un reformatage des données et à obtenir en sortie des .csv (un pour chaque année). Ces scripts sont disponibles dans */scripts/python/*.

# Stockage sous SQL Server <a name="SQL_Server"></a>

## Docker <a name="Docker"></a>

Docker a été utilisé pour monter une image SQL Server. Il a suffit d'ouvrir PowerShell et d'exécuter les deux commandes suivantes : 
- ```docker pull mcr.microsoft.com/mssql/server:2019-CU14-ubuntu-20.04```
- ```docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=<my_password>" -e "MSSQL_PID=Express" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-CU14-ubuntu-20.04```

Documentation : https://hub.docker.com/_/microsoft-mssql-server.

## SQL Server Management Studio <a name="SSMS"></a>

Une fois l'image de SQL Server en place, j'ai du télécharger un logiciel pour pouvoir manager le stockage des mes données : Microsoft SQL Server Management Studio 18.

Disponible ici : https://docs.microsoft.com/fr-fr/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15.

Pour me connecter, j'ai utilisé les informations fournies lors de la création via Docker (voir ci-dessous).

<img src="/img/SQL_Server/connexion.png" width="600" height="400">

J'ai ensuite crée une nouvelle database : *DVF*. 

<img src="/img/SQL_Server/new_database.png" width="600" height="600">

Et importé chacun de mes flat files (.csv) dans une table correspondante (ex : *dvf_2017*).

<img src="/img/SQL_Server/csv_to_table.png" width="800" height="500">

# Visualisation avec Power BI <a name="Visualisation"></a>

Pour visualiser mes données, j'ai opté pour le tout Microsoft, avec Power BI.

## Connexion SQL Server <a name="Power_BI_SQL_Server"></a>

J'ai donc connecté Power Bi à SQL Server pour obtenir les données stockées dans mes tables.

<img src="/img/Power_BI/obtenir_data_SQL_Server.png" width="600" height="500">

Il m'a encore une fois suffit de renseigner les informations utilisées lors de la création via Docker. J'ai même pu préciser directement la BDD *DVF*. 

<img src="/img/Power_BI/power_bi_BDD.png" width="500" height="250">

Et j'ai donc rapidement obtenu mes tables dans Power BI (relativement aux tailles de mes tables SQL - plus de 3M d'enregistrements chacune).

<img src="/img/Power_BI/table_power_bi.png" width="750" height="500">

# Analysis


