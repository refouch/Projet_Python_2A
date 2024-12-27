# Quels déterminants de la consommation cannabis en Europe et quelq liens avec sa légalisation ?
*Victor le Lay, Rémi Fouchérand, Quentin Mallegol*

## Présentation du sujet
Dans ce projet, nous avons pour but de décrire l'état de la consommation de cannabis dans les différents pays européens, en étudiant les liens qu'il pourrait y avoir avec la législation dans un pays donné. Nous avions un premier objectif en tête: essayer de prédire la législation sur le cannabis dans un pays donné à partir des différentes caractéristiques du pays en matière de consommation de drogue. 
Une analyse approfondie de notre jeu de données nous a conduit à réorienter ensuite notre analyse vers des objectifs plus larges.

## Données utilisées
- Open Data de [l'EUDA](https://www.euda.europa.eu/index_en) (European Union Drugs Agency) sur la Prévalence de la consommation de drogue en Europe, le nombre d'infractions liées aux drogues ou encore le nombre d'admission aux urgences liées aux drogues
- Open Data [d'Eurostat](https://ec.europa.eu/eurostat/fr/) sur des données macroéconomiques et socio-économiques pour chaque pays.
  
- Scraping de données disponibles en accès libre sur [Wikipedia](https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal), et en particulier l'état de la législation sur le cannabis dans chaque pays

## Modèles mis en œuvre
- Mise en place d'un **Classifieur** afin de tenter de prédire l'état de la législation dans chaque pays à partir des données de consommation de drogue.
- Mise en place d'une **Régréssion linéaire** afin de prédire la prévalence dans chaque pays à partir des données socio-économiques

# Dans quel ordre lire le projet ?

Le projet a été divisé en deux parties:

1. Une phase de récupération, de nettoyage et de mise en forme des données décrites dans un premier Notebook (`Tidy.ipynb`). Nous vous conseillons de parcourir d'abord en surface ce notebook plutôt lourd, mais dans lequel nous avons détaillé les décisions méthodologiques prises quant à la restriction et à la mise en forme des données utilisées

2. Une phase d'utilisation des données à des fins descriptives comme de modélisation, décrite dans un second Notebook (`Notebook_Final.ipynb`). Nous vous conseillons de le lire dans un second temps et plus attentivement que le premier, car c'est ce dernier qui contient toutes les expérimentations avec les données, et présente les résultats de notre analyse et les conclusions que nous en avons tiré.

Bonne lecture ! 
