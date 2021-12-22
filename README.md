# Valeurs foncieres en France (2017-2020)

<img src="/img/global/global_fil_rouge.png" width="800" height="750">

# Table of Contents
1. [Sources de données](#sources)
2. [Nettoyage de données](#nettoyage)
3. [Stockage sous SQL Server](#SQL_Server)
    1.  [Docker](#Docker)
    2.  [SQL Server Management Studio](#SSMS)
4. [Visualisation avec Power BI](#Visualisation)
    1.  [Connexion SQL Server](#Power_BI_SQL_Server)
    2.  [Preparation des données](#Data_preparation)
    3.  [Création du dashboard](#Dashboard_creation)
6. [Analyse de données](#Analysis)

# Sources de données <a name="sources"></a>

Les données ont été récupérées sur le site data-gouv.fr : [dvf](https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/).

La base de données DVF recense les mutations à titre onéreux (vente, vente en l'état futur d'achèvement, vente terrain à bâtir, échange, adjudication, expropriation) advenues sur les années de 2017 à 2020. Les données obtenues étaient constituées de 4 fichiers texte (un pour chaque année).

# Nettoyage de données <a name="nettoyage"></a>

Les fichiers texte de chaque année contenant plus de 3 millions de lignes, il a été nécessaire de spliter ceux-ci avec *Notepad++* pour permettre de ne pas avoir d'erreur  de type *"out of memory"* durant l'exécution des traitements de cleaning. Les scripts Python ont servi à effectuer un reformatage des données et à obtenir en sortie des .csv (un pour chaque année). Ces scripts sont disponibles dans */scripts/python/*.

# Stockage sous SQL Server <a name="SQL_Server"></a>

## Docker <a name="Docker"></a>

Docker a été utilisé pour monter une image SQL Server. Il a suffit d'ouvrir PowerShell et d'exécuter les deux commandes suivantes : 
- ```docker pull mcr.microsoft.com/mssql/server:2019-CU14-ubuntu-20.04```
- ```docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=<my_password>" -e "MSSQL_PID=Express" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-CU14-ubuntu-20.04```

Documentation : [MySQL Server via Docker](https://hub.docker.com/_/microsoft-mssql-server).

## SQL Server Management Studio <a name="SSMS"></a>

Le logiciel a SQL Server Management Studio a été utilisé pour pouvoir manager le stockage des mes données. Disponible ici : [SQL Server Management Studio](https://docs.microsoft.com/fr-fr/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15).

Pour se connecter : 

<img src="/img/SQL_Server/connexion.png" width="600" height="400">

Il suffit ensuite de créer une base *DVF*, d'importer les .csv dans des tables correspondantes *dvf_2017*.

# Visualisation avec Power BI <a name="Visualisation"></a>

## Connexion SQL Server <a name="Power_BI_SQL_Server"></a>

Pour se connecter :

<img src="/img/Power_BI/obtenir_data_SQL_Server.png" width="600" height="500">

## Préparation des données <a name="Data_preparation"></a>

1) Transformation des données "Valeur fonciere", "Surface batie" et " Surface terrain" en float.
    -  Changement des "." en "," et changement du type de données : devise pour la valeur foncière et décimal pour les surfaces.
2) Définition des données géographiques (hiérarchie Géo) : 
    - Pays : ajout d'une colonne "Pays" contenant la valeur "France".
    - Département : code département.
    - Code postal : code postal.
    - Localité : commune.
3) Gestion des données vides pour les types de locaux : remplacement des "*null*" par "Autres".

## Création du dashboard  <a name="Dashboard_creation"></a>

Le .pbix sera constitué de 4 dashboard - un pour chaque année - construit selon le même schéma détaille ci-après : 
- Titre : Valeur foncière de l'année 20XX.
- Nature de la mutation : filtre sur le type de mutation.
- Valeur foncière (médiane) par département : 3DMa.
- Valeur foncière (médiane) par type de local : pie chart sur le pourcentage de valeur foncière associée à chaque type de local. 
- Valeur foncière (médiane) et nombre de ventes par mois : histogramme des valeurs foncières par mois groupé à une courbe du nombre de ventes par mois au cours de l'année 20XX.

L'aspect est le suivant : 

<img src="/img/Power_BI/dashboard_2017.png" width="900" height="550">

Les aperçus des autres dashboards (2018 à 2020) sont également disponibles dans */img/Power_BI/*.

Le .pbix dépassant les 100Mb, il n'a pas pu être déposé ici. Celui-ci est en revanche disponible suivant ce lien : [dashboard_annuel](https://app.powerbi.com/links/2K-8GldX8w?ctid=373016f8-79a9-4eed-80d2-100ce948d960&pbi_source=linkShare&bookmarkGuid=1222e86f-1cca-4dc2-afab-7e082bb8ccd0).

# Analyse de données <a name="Analysis"></a>

Jupyter notebook a été utilisé pour l'analyse; celui-ci est consultable dans */scripts/jupyter_notebook/*.
L'analyse est constitué de 3 grands axes : 
1) Analyse générale sur les valeurs foncières en France.
2) Focus sur la métropole lyonnaise.
3) Analyse temporelle (non terminée).
4) Machine Learning (non traité - faute de temps).
