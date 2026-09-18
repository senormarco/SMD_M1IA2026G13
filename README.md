# Projet SMD — Analyse, Segmentation et Dashboard Marketing IA

## 1. Présentation du projet

Ce projet propose une chaîne complète d'analyse de données permettant de :

* préparer et explorer les données ;
* réaliser une analyse descriptive ;
* segmenter les clients ;
* appliquer des méthodes de Machine Learning ;
* analyser les performances marketing ;
* analyser les ventes et les produits ;
* produire des visualisations professionnelles ;
* présenter les résultats dans un tableau de bord interactif avec Streamlit.

Le projet est organisé autour de deux éléments principaux :

* `SMD_corrige.ipynb` : notebook contenant les différentes étapes d'analyse et de modélisation ;
* `dashboard.py` : application Streamlit permettant de visualiser les résultats de manière interactive.

---

# 2. Technologies utilisées

Le projet utilise principalement Python et les bibliothèques suivantes :

| Bibliothèque      | Utilisation                                |
| ----------------- | ------------------------------------------ |
| `pandas`          | Manipulation et analyse des données        |
| `numpy`           | Calculs numériques                         |
| `matplotlib`      | Création des graphiques                    |
| `scikit-learn`    | Machine Learning et évaluation des modèles |
| `ydata-profiling` | Génération de rapports exploratoires       |
| `streamlit`       | Création du tableau de bord interactif     |
| `jupyter`         | Exécution du notebook                      |

---

# 3. Structure recommandée du projet

```text
Projet_SMD/
│
├── data/
│   ├── customers_data.csv
│   ├── sales_data_.csv
│   ├── products_data.csv
│   └── marketing_data.csv
│
├── outputs/
│   ├── customers_segmented.csv
│   └── personas.csv
│
├── SMD_notebook.ipynb
├── dashboard.py
├── requirements.txt
└── README.md
```

---

# 4. Description des fichiers

## `SMD_notebook.ipynb`

Le notebook contient les principales étapes d'analyse :

* importation des données ;
* nettoyage et préparation ;
* analyse exploratoire ;
* visualisation ;
* standardisation des variables ;
* segmentation des clients ;
* réduction dimensionnelle avec PCA ;
* classification ;
* régression ;
* évaluation des modèles.

### Algorithmes utilisés

Le projet utilise notamment :

```python
KMeans
AgglomerativeClustering
LogisticRegression
RandomForestClassifier
RandomForestRegressor
```

Des outils de prétraitement et d'évaluation de `scikit-learn` sont également utilisés.

---

## `dashboard.py`

Ce fichier contient le tableau de bord interactif développé avec Streamlit.

Il permet notamment de consulter :

* les indicateurs principaux ;
* la segmentation des clients ;
* les performances des campagnes marketing ;
* les ventes ;
* les catégories de produits ;
* les indicateurs de conversion ;
* le ROI ;
* le CPA ;
* le CTR.

Le tableau de bord comporte trois grandes sections :

1. Segmentation clients
2. Performance campagnes
3. Ventes et produits

---

## `data/`

Le dossier `data` contient les données utilisées par le projet.

### `customers_data.csv`

Contient les informations relatives aux clients.

Exemples de variables utilisées :

* âge ;
* informations client ;
* dépenses ;
* variables nécessaires à la segmentation.

### `sales_data_.csv`

Contient les informations relatives aux ventes.

Le chiffre d'affaires est notamment calculé à partir de :

```text
Revenue = Quantity × Sale_Price
```

### `products_data.csv`

Contient les informations relatives aux produits.

Il est utilisé avec les données de ventes afin d'obtenir une analyse par catégorie de produits.

### `marketing_data.csv`

Contient les informations relatives aux campagnes marketing.

Ces données permettent notamment d'étudier :

* le budget ;
* les conversions ;
* le CTR ;
* le CPA ;
* le ROI ;
* les différents canaux marketing.

---

# 5. Dossier `outputs/`

Le dossier `outputs` contient les résultats produits pendant l'analyse.

### `customers_segmented.csv`

Contient les clients auxquels un cluster a été attribué.

Le cluster permet de regrouper les clients présentant des caractéristiques similaires.

### `personas.csv`

Contient les profils ou personas obtenus à partir de la segmentation.

Ces fichiers sont utilisés par le dashboard lorsqu'ils sont disponibles.

---

# 6. Installation

## Étape 1 — Vérifier Python

Vérifier que Python est installé :

```bash
python --version
```

ou :

```bash
python3 --version
```

Une version récente de Python est recommandée.

---

# 7. Créer un environnement virtuel

Il est recommandé d'utiliser un environnement virtuel afin d'isoler les dépendances du projet.

### Windows

```bash
python -m venv .venv
```

Activation :

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
```

Activation :

```bash
source .venv/bin/activate
```

Lorsque l'environnement est activé, le terminal affiche généralement :

```text
(.venv)
```

---

# 8. Installer les dépendances

Mettre à jour `pip` :

```bash
python -m pip install --upgrade pip
```

Puis installer toutes les bibliothèques du projet :

```bash
pip install -r requirements.txt
```

Le fichier `requirements.txt` contient :

```txt
pandas
numpy
matplotlib
scikit-learn
ydata-profiling
streamlit
jupyter
```

---

# 9. Vérifier l'installation

Pour vérifier les packages installés :

```bash
pip list
```

Pour vérifier individuellement les principales bibliothèques :

```bash
python -c "import pandas; print('pandas OK')"
```

```bash
python -c "import numpy; print('numpy OK')"
```

```bash
python -c "import matplotlib; print('matplotlib OK')"
```

```bash
python -c "import sklearn; print('scikit-learn OK')"
```

```bash
python -c "import streamlit; print('streamlit OK')"
```

```bash
python -c "import ydata_profiling; print('ydata-profiling OK')"
```

---

# 10. Exécuter le notebook

Lancer Jupyter :

```bash
jupyter notebook
```

Une page s'ouvre généralement dans le navigateur.

Ouvrir ensuite :

```text
SMD_corrige.ipynb
```

Puis exécuter les cellules dans l'ordre.

Il est recommandé d'exécuter le notebook depuis la racine du projet afin que les chemins suivants soient correctement reconnus :

```text
data/
outputs/
```

---

# 11. Lancer le tableau de bord

Depuis la racine du projet :

```bash
streamlit run dashboard.py
```

Streamlit affiche normalement une adresse locale dans le terminal.

Le tableau de bord peut ensuite être consulté dans le navigateur.

---

# 12. Ordre recommandé d'utilisation

Pour éviter les problèmes de fichiers manquants, suivre cet ordre :

```text
1. Installer Python
        ↓
2. Créer l'environnement virtuel
        ↓
3. Installer requirements.txt
        ↓
4. Placer les fichiers CSV dans data/
        ↓
5. Exécuter SMD_corrige.ipynb
        ↓
6. Générer les résultats dans outputs/
        ↓
7. Lancer dashboard.py
        ↓
8. Analyser les résultats
```

---

# 13. Indicateurs du dashboard

## Nombre de clients

Nombre total de clients disponibles dans les données.

## Chiffre d'affaires

Le chiffre d'affaires est calculé selon :

```text
Revenue = Quantity × Sale_Price
```

## Budget marketing

Somme des budgets associés aux campagnes marketing.

## ROI

Le ROI est estimé selon la logique utilisée dans le projet :

```text
ROI (%) =
((Conversions × Revenu moyen - Budget) / Budget) × 100
```

Lorsque le budget est nul, le calcul est protégé afin d'éviter une division par zéro.

## CTR

Le CTR correspond au taux de clics.

Il permet d'évaluer l'attractivité d'une campagne auprès des utilisateurs exposés.

## Conversion

Le taux de conversion mesure la proportion d'utilisateurs ayant réalisé l'action attendue après interaction avec la campagne.

## CPA

Le CPA correspond au coût moyen associé à une conversion.

---

# 14. Segmentation des clients

La segmentation permet de regrouper les clients ayant des caractéristiques similaires.

Le projet utilise notamment :

```python
KMeans
```

et :

```python
AgglomerativeClustering
```

Les données peuvent être standardisées avec :

```python
StandardScaler
```

Une réduction dimensionnelle avec :

```python
PCA
```

est également utilisée pour faciliter l'analyse et la visualisation des groupes.

---

# 15. Visualisation de la segmentation

Le dashboard représente notamment les clients sur un graphique utilisant :

```text
Axe X : Age
Axe Y : Total_Spent
```

Chaque groupe est identifié par son numéro de cluster.

La légende permet d'identifier les différents segments.

Les noms des clients peuvent également être affichés sur le graphique afin de faciliter l'interprétation.

---

# 16. Analyse des campagnes marketing

Le dashboard permet de comparer les différents canaux marketing.

Les indicateurs principaux sont :

* ROI ;
* CPA ;
* CTR ;
* taux de conversion ;
* budget ;
* conversions.

Les résultats sont regroupés par canal afin de faciliter la comparaison des performances.

---

# 17. Analyse des ventes

Les ventes sont associées aux informations produits afin d'obtenir une analyse par catégorie.

Le dashboard permet notamment d'identifier :

* les catégories générant le plus de chiffre d'affaires ;
* les performances des produits ;
* les volumes de ventes ;
* les tendances générales des ventes.

---

# 18. Filtres interactifs

Le tableau de bord contient des filtres permettant d'affiner l'analyse.

Selon la section consultée, il est possible de filtrer notamment :

* les clusters clients ;
* les classes ou groupes disponibles ;
* les canaux marketing ;
* les catégories.

Les indicateurs et graphiques sont actualisés en fonction des filtres sélectionnés.

---

# 19. Figures du dashboard

## Figure 1 — Segmentation des clients

Cette figure représente les clients selon leur âge et leurs dépenses totales.

**Axe X :** Age

**Axe Y :** Total_Spent

**Légende :** Cluster client

Objectif : identifier visuellement les groupes de clients ayant des comportements similaires.

---

## Figure 2 — ROI par canal

Cette figure compare le ROI moyen des différents canaux marketing.

**Axe X :** Canal marketing

**Axe Y :** ROI (%)

Objectif : identifier les canaux ayant les meilleures performances financières estimées.

---

## Figure 3 — CPA par canal

Cette figure compare le coût moyen par acquisition selon les canaux.

**Axe X :** Canal marketing

**Axe Y :** CPA

Objectif : identifier les canaux nécessitant le moins de dépenses pour obtenir une conversion.

---

## Figure 4 — CTR et conversion

Cette figure compare :

* le CTR ;
* le taux de conversion.

Objectif : analyser simultanément l'attractivité et l'efficacité des différents canaux.

---

## Figure 5 — Chiffre d'affaires par catégorie

Cette figure présente le chiffre d'affaires généré par les différentes catégories de produits.

**Axe X :** Catégorie

**Axe Y :** Chiffre d'affaires

Objectif : identifier les catégories contribuant le plus aux ventes.

---

# 20. Interprétation des résultats

Le dashboard permet de passer de l'analyse descriptive à une interprétation décisionnelle.

Par exemple :

```text
Segmentation
     ↓
Identification des profils clients
     ↓
Analyse des campagnes
     ↓
Comparaison des canaux
     ↓
Analyse des ventes
     ↓
Identification des catégories performantes
     ↓
Aide à la décision marketing
```

Les résultats doivent cependant être interprétés en tenant compte de la qualité et de la représentativité des données disponibles.

---

# 21. Dépannage

## Erreur : `ModuleNotFoundError`

Exemple :

```text
ModuleNotFoundError: No module named 'pandas'
```

Solution :

```bash
pip install -r requirements.txt
```

Ou installer directement le package manquant :

```bash
pip install pandas
```

---

## Erreur : Streamlit non reconnu

Si la commande :

```bash
streamlit run dashboard.py
```

ne fonctionne pas, utiliser :

```bash
python -m streamlit run dashboard.py
```

---

## Erreur concernant les fichiers CSV

Vérifier que le projet possède bien :

```text
data/
├── customers_data.csv
├── sales_data_.csv
├── products_data.csv
└── marketing_data.csv
```

Les noms des fichiers doivent correspondre exactement aux noms utilisés dans le code.

---

## Erreur concernant `outputs`

Si certains résultats de segmentation ne sont pas disponibles, vérifier la présence de :

```text
outputs/customers_segmented.csv
outputs/personas.csv
```

Ces fichiers peuvent être générés par les étapes précédentes du projet.

---

# 22. Réinstaller complètement les dépendances

En cas de problème avec l'environnement Python :

### Supprimer l'ancien environnement

Windows :

```bash
rmdir /s /q .venv
```

Linux/macOS :

```bash
rm -rf .venv
```

### Recréer l'environnement

Windows :

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS :

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Réinstaller les dépendances

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

# 23. Commandes essentielles — résumé

Pour une installation complète :

```bash
python -m venv .venv
```

Windows :

```bash
.venv\Scripts\activate
```

Linux/macOS :

```bash
source .venv/bin/activate
```

Puis :

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Lancer le notebook :

```bash
jupyter notebook
```

Lancer le dashboard :

```bash
streamlit run dashboard.py
```

Ou :

```bash
python -m streamlit run dashboard.py
```

---

# 24. Bonnes pratiques

Il est recommandé de :

* utiliser un environnement virtuel ;
* conserver toutes les dépendances dans `requirements.txt` ;
* ne pas modifier directement les données originales ;
* conserver les données sources dans `data/` ;
* conserver les résultats produits dans `outputs/` ;
* exécuter le notebook avant le dashboard si les fichiers de sortie doivent être générés ;
* conserver une structure de projet stable ;
* documenter toute modification importante du projet.

---

# 25. Limites

Les indicateurs calculés dépendent directement de la qualité des données disponibles.

En particulier :

* un ROI estimé n'est pas nécessairement un ROI financier réel ;
* la qualité de la segmentation dépend des variables utilisées ;
* les clusters doivent être interprétés à partir de leurs caractéristiques ;
* les résultats statistiques et de Machine Learning doivent être validés avant une prise de décision importante.

---

# 26. Conclusion

Ce projet constitue une chaîne complète d'analyse allant de la préparation des données jusqu'à la visualisation interactive des résultats.

L'utilisation conjointe de :

* Python ;
* Pandas ;
* NumPy ;
* Matplotlib ;
* Scikit-learn ;
* YData Profiling ;
* Streamlit ;

permet de construire une solution d'analyse structurée et interactive.

Le notebook constitue la partie analytique et méthodologique du projet, tandis que `dashboard.py` constitue la partie visualisation et présentation des résultats.

---

# 27. Fichiers principaux

```text
SMD_corrige.ipynb
    → Analyse et Machine Learning

dashboard.py
    → Tableau de bord interactif

requirements.txt
    → Dépendances Python

README.md
    → Documentation du projet

data/
    → Données sources

outputs/
    → Résultats générés
```

---

## Auteur

Projet d'analyse de données, segmentation clients et performance marketing.

Version : 1.0
# Dashboard Marketing IA

## 1. Présentation

Ce projet est un tableau de bord interactif développé avec **Streamlit** pour l'analyse et l'optimisation des performances marketing.

Il permet de centraliser plusieurs dimensions de l'analyse :

* analyse de la clientèle ;
* segmentation des clients ;
* interprétation des segments sous forme de personas ;
* analyse des campagnes marketing ;
* calcul des principaux KPI marketing ;
* analyse des ventes ;
* analyse du revenu par catégorie de produits ;
* aide à la décision marketing.

Le dashboard a été conçu pour fournir une interface simple, interactive et adaptée à l'exploration des données.

---

## 2. Objectifs du projet

L'objectif principal est de transformer des données marketing brutes en informations utiles pour la prise de décision.

Le dashboard permet notamment de répondre aux questions suivantes :

* Combien de clients sont présents dans la base ?
* Quel est le revenu total généré ?
* Quel budget est investi dans les campagnes ?
* Quel canal marketing présente le meilleur ROI ?
* Quel canal possède le CPA le plus faible ?
* Quel est le taux de clic global ?
* Quel est le taux de conversion ?
* Quels sont les différents segments de clients ?
* Quels segments dépensent le plus ?
* Quelles catégories de produits génèrent le plus de revenus ?

---

## 3. Technologies utilisées

Le projet utilise principalement les technologies suivantes :

| Technologie | Utilisation                         |
| ----------- | ----------------------------------- |
| Python      | Langage principal                   |
| Streamlit   | Création du dashboard interactif    |
| Pandas      | Manipulation et analyse des données |
| Matplotlib  | Création des figures statistiques   |
| CSV         | Stockage des données                |

### Installation

Installer les bibliothèques nécessaires avec :

```bash
pip install streamlit pandas matplotlib
```

Ou, si le projet contient un fichier `requirements.txt` :

```bash
pip install -r requirements.txt
```

---

## 4. Structure du projet

La structure attendue est la suivante :

```text
projet/
│
├── dashboard.py
│
├── data/
│   ├── customers_data.csv
│   ├── sales_data_.csv
│   ├── products_data.csv
│   └── marketing_data.csv
│
├── outputs/
│   ├── customers_segmented.csv
│   └── personas.csv
│
└── README.md
```

---

## 5. Rôle des fichiers

### `dashboard.py`

C'est le fichier principal de l'application.

Il contient :

* la configuration de Streamlit ;
* le chargement des données ;
* le calcul des KPI ;
* les filtres interactifs ;
* les tableaux ;
* les graphiques ;
* l'analyse des segments ;
* l'analyse des campagnes ;
* l'analyse des ventes ;
* la synthèse décisionnelle.

Le dashboard est lancé à partir de ce fichier.

---

### `data/customers_data.csv`

Ce fichier contient les informations relatives aux clients.

Il est utilisé notamment pour :

* compter les clients ;
* analyser les caractéristiques des clients ;
* alimenter la segmentation.

---

### `data/sales_data_.csv`

Ce fichier contient les données de ventes.

Il permet notamment de calculer :

```text
Revenue = Quantity × Sale_Price
```

Il est utilisé pour :

* calculer le revenu total ;
* analyser les ventes ;
* analyser les quantités vendues ;
* calculer le revenu moyen utilisé dans l'estimation du ROI.

---

### `data/products_data.csv`

Ce fichier contient les informations relatives aux produits.

Il est associé aux données de ventes grâce au champ :

```text
Product_ID
```

Cette jointure permet notamment d'analyser le revenu par catégorie.

---

### `data/marketing_data.csv`

Ce fichier contient les données relatives aux campagnes marketing.

Il permet de calculer :

* CTR ;
* taux de conversion ;
* CPA ;
* ROI.

---

### `outputs/customers_segmented.csv`

Ce fichier contient les résultats de la segmentation des clients.

Le dashboard utilise notamment la colonne :

```text
Cluster_KMeans
```

pour afficher les différents segments.

---

### `outputs/personas.csv`

Ce fichier contient l'interprétation marketing des différents segments.

Il peut notamment contenir :

```text
Nom_persona
Clients
Description
```

Les personas sont affichés dans la section consacrée à la segmentation.

---

## 6. Lancement du dashboard

### Étape 1 — Ouvrir un terminal

Se placer dans le dossier principal du projet :

```bash
cd chemin/vers/le/projet
```

### Étape 2 — Vérifier Python

```bash
python --version
```

ou :

```bash
python3 --version
```

### Étape 3 — Installer les dépendances

```bash
pip install streamlit pandas matplotlib
```

### Étape 4 — Lancer l'application

```bash
streamlit run dashboard.py
```

Streamlit démarre alors le serveur local.

Le dashboard est généralement accessible à l'adresse :

```text
http://localhost:8501
```

---

# 7. Architecture du dashboard

Le dashboard est organisé en trois grandes sections.

```text
Dashboard Marketing IA
│
├── Vue d'ensemble
│   ├── Clients
│   ├── Revenu total
│   ├── Budget marketing
│   └── ROI moyen
│
├── Segmentation clients
│   ├── Filtre des clusters
│   ├── KPI des segments
│   ├── Tableau des clients
│   ├── Personas
│   ├── Figure de segmentation
│   └── Profil moyen des clusters
│
├── Performance campagnes
│   ├── Filtre des canaux
│   ├── KPI marketing
│   ├── Tableau des campagnes
│   ├── ROI par canal
│   ├── CPA par canal
│   ├── CTR et conversion
│   └── Analyse automatique
│
└── Ventes et produits
    ├── KPI commerciaux
    ├── Tableau des ventes
    ├── Revenu par catégorie
    └── Catégorie la plus performante
```

---

# 8. Indicateurs utilisés

## 8.1 CTR

Le CTR signifie **Click Through Rate**.

Il mesure la proportion d'impressions ayant généré un clic.

```text
CTR = Clicks / Impressions × 100
```

Un CTR élevé indique généralement qu'une campagne génère davantage d'engagement.

---

## 8.2 Taux de conversion

Le taux de conversion mesure la proportion de clics transformés en conversions.

```text
Taux de conversion =
Conversions / Clicks × 100
```

Cet indicateur permet d'évaluer l'efficacité d'une campagne après le clic.

---

## 8.3 CPA

Le CPA signifie **Cost Per Acquisition**.

Il mesure le coût moyen nécessaire pour obtenir une conversion.

```text
CPA = Budget / Conversions
```

Un CPA faible est généralement préférable lorsque la qualité des conversions est comparable.

---

## 8.4 ROI

Le ROI signifie **Return On Investment**.

Dans ce dashboard, le ROI est estimé selon :

```text
ROI =
(Gain - Investissement) / Investissement × 100
```

Le gain estimé est basé sur le nombre de conversions et le revenu moyen des ventes.

La formule utilisée dans le programme est :

```text
ROI =
(Conversions × Revenu moyen - Budget)
/
Budget × 100
```

### Interprétation

|       ROI | Interprétation |
| --------: | -------------- |
| ROI > 0 % | Gain estimé    |
| ROI = 0 % | Équilibre      |
| ROI < 0 % | Perte estimée  |

> Important : le ROI présenté dans ce dashboard est une estimation. Il ne correspond pas nécessairement au ROI financier réel d'une campagne.

---

# 9. Section Segmentation clients

La segmentation permet de regrouper les clients selon leurs caractéristiques similaires.

Le dashboard utilise les résultats produits par la méthode **K-Means**.

Le filtre permet de sélectionner un ou plusieurs clusters.

Pour chaque sélection, le dashboard présente :

* le nombre de clients ;
* la dépense moyenne ;
* le nombre moyen d'achats ;
* le détail des clients ;
* les personas ;
* le profil des clusters.

---

## 9.1 Figure de segmentation

La figure représente les clients dans un espace à deux dimensions :

```text
Axe X → Âge du client

Axe Y → Dépenses totales (€)

Légende → Cluster K-Means
```

### Figure 1 — Segmentation des clients selon l'âge et les dépenses

**Légende :**

Chaque point représente un client. L'axe horizontal indique l'âge du client et l'axe vertical représente ses dépenses totales. La légende identifie le cluster auquel appartient chaque client selon la segmentation K-Means.

Cette représentation permet d'observer visuellement les groupes de clients présentant des comportements similaires.

---

# 10. Section Performance des campagnes

Cette section permet de comparer les campagnes marketing selon plusieurs indicateurs.

Les principaux indicateurs sont :

* nombre de campagnes ;
* budget ;
* conversions ;
* ROI ;
* CTR ;
* taux de conversion ;
* CPA.

Un filtre permet de sélectionner les canaux marketing à analyser.

---

## 10.1 ROI par canal

### Figure 2 — ROI moyen par canal marketing

La figure compare le ROI moyen estimé des différents canaux.

Une valeur élevée indique une rentabilité estimée plus importante selon la méthode de calcul utilisée.

---

## 10.2 CPA par canal

### Figure 3 — CPA moyen par canal marketing

La figure présente le coût moyen nécessaire pour obtenir une conversion pour chaque canal.

Une valeur plus faible indique un coût d'acquisition plus faible, toutes choses égales par ailleurs.

---

## 10.3 Engagement et conversion

### Figure 4 — Engagement et conversion par canal

Cette figure compare :

* le CTR ;
* le taux de conversion.

Les deux indicateurs doivent être étudiés conjointement.

Un canal peut avoir un CTR élevé mais un taux de conversion relativement faible.

---

# 11. Section Ventes et produits

Cette section permet d'étudier les performances commerciales.

Les indicateurs présentés sont notamment :

* nombre de ventes ;
* revenu total ;
* quantité vendue.

Les données de ventes sont associées aux données produits grâce au champ :

```text
Product_ID
```

---

## 11.1 Revenu par catégorie

### Figure 5 — Revenu total par catégorie de produit

Cette figure représente le revenu généré par chaque catégorie.

Les catégories sont classées selon leur contribution au revenu total.

Elle permet d'identifier rapidement les catégories les plus performantes.

---

# 12. Interactivité

Le dashboard permet à l'utilisateur d'interagir avec les données.

Les principaux filtres sont :

### Segmentation

```text
Filtrer les clusters
```

L'utilisateur peut sélectionner un ou plusieurs clusters.

### Marketing

```text
Filtrer par canal
```

L'utilisateur peut sélectionner un ou plusieurs canaux marketing.

Les KPI et les tableaux sont automatiquement recalculés en fonction des filtres sélectionnés.

---

# 13. Analyse automatique

Le dashboard identifie automatiquement :

* le canal présentant le meilleur ROI moyen ;
* le canal présentant le CPA moyen le plus faible ;
* la catégorie de produits générant le plus de revenu.

Ces informations facilitent l'interprétation des résultats.

---

# 14. Flux général des données

Le fonctionnement général peut être résumé comme suit :

```text
                    DONNÉES BRUTES
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
     Clients           Ventes          Marketing
        │                │                │
        │                ▼                ▼
        │          Calcul Revenue     Calcul KPI
        │                                │
        ▼                                ▼
   Segmentation                    Performance
        │                           campagnes
        ▼                                │
    Clusters                             │
        │                                │
        ▼                                │
    Personas                             │
        │                                │
        └───────────────┬────────────────┘
                        │
                        ▼
              DASHBOARD INTERACTIF
                        │
                        ▼
                AIDE À LA DÉCISION
```

---

# 15. Résultats attendus

Après lancement du dashboard, l'utilisateur doit pouvoir :

1. consulter les principaux KPI ;
2. filtrer les segments clients ;
3. examiner le profil des clients ;
4. visualiser la segmentation ;
5. consulter les personas ;
6. comparer les canaux marketing ;
7. identifier le meilleur ROI ;
8. identifier le CPA le plus faible ;
9. analyser le CTR et le taux de conversion ;
10. analyser les ventes ;
11. identifier les catégories les plus rentables.

---

# 16. Vérification en cas d'erreur

Si Streamlit affiche :

```text
Impossible de charger les fichiers de données.
```

Vérifier que les fichiers suivants existent :

```text
data/customers_data.csv
data/sales_data_.csv
data/products_data.csv
data/marketing_data.csv
```

Si la segmentation n'apparaît pas, vérifier :

```text
outputs/customers_segmented.csv
```

Si les personas n'apparaissent pas, vérifier :

```text
outputs/personas.csv
```

---

# 17. Organisation recommandée

Pour maintenir le projet propre, il est recommandé de séparer :

```text
data/
```

pour les données brutes,

```text
outputs/
```

pour les résultats produits par les différents modules,

```text
dashboard.py
```

pour l'application interactive.

Cette organisation permet de distinguer clairement les données d'entrée, les résultats intermédiaires et l'interface de visualisation.

---

# 18. Bonnes pratiques

Avant de lancer le dashboard :

* vérifier les noms des fichiers CSV ;
* vérifier les colonnes utilisées par le programme ;
* vérifier que les valeurs numériques sont correctement formatées ;
* vérifier l'absence de divisions par zéro ;
* vérifier que les fichiers de segmentation ont été générés ;
* vérifier que les données sont suffisamment complètes.

Pour une présentation académique, il est également recommandé d'accompagner chaque figure d'un titre, d'axes clairement nommés et d'une légende expliquant ce que représente la visualisation.

---

# 19. Limites

Les résultats du dashboard doivent être interprétés avec prudence.

En particulier :

* le ROI est une estimation ;
* la segmentation dépend des variables utilisées pour K-Means ;
* un cluster ne constitue pas nécessairement un profil marketing définitif ;
* un CTR élevé ne garantit pas une conversion élevée ;
* un CPA faible ne signifie pas nécessairement que la campagne est la plus rentable ;
* les résultats dépendent de la qualité des données utilisées.

Les indicateurs doivent donc être interprétés conjointement plutôt qu'isolément.

---

# 20. Conclusion

Le Dashboard Marketing IA constitue une interface d'analyse permettant de passer des données brutes à une lecture synthétique des performances marketing.

Il combine trois dimensions principales :

```text
Segmentation clients
        +
Performance marketing
        +
Analyse commerciale
        =
Aide à la décision
```

L'objectif final est d'utiliser les données pour mieux comprendre les clients, évaluer les campagnes marketing, identifier les produits performants et orienter les décisions d'optimisation.

---

## Auteur

**Projet : Dashboard Marketing IA**

**Technologies :** Python, Streamlit, Pandas, Matplotlib

**Module :** Module 8 — Dashboard Marketing interactif


