#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Analyse et optimisation du réseau de transport Bibus

#Le transport urbain joue un rôle essentiel dans la mobilité quotidienne des citoyens. La qualité d’un réseau de transport dépend de plusieurs facteurs, notamment la ponctualité des véhicules, la fréquentation des lignes et la satisfaction des voyageurs.

#L’objectif de cette étude est d’exploiter les données opérationnelles du réseau Bibus afin d’identifier les principaux facteurs à l’origine des retards, d’analyser les variations de fréquentation du réseau et d’évaluer l’impact de ces éléments sur la satisfaction des usagers.

#À travers une démarche complète de Data Analytics, ce projet mobilise des techniques de préparation des données, d’analyse exploratoire, de visualisation et d’interprétation des résultats afin de transformer les données en informations utiles à la prise de décision.

#Les conclusions de cette étude permettront de mettre en évidence des pistes d’amélioration concrètes visant à renforcer la performance opérationnelle du réseau et à améliorer l’expérience des voyageurs.


# In[ ]:


# chargement et exploration de mes données
import pandas as pd
dfc = pd.ExcelFile("Bibus")
dfc.sheet_names


# In[ ]:


trajets = pd.read_excel("Bibus", header=2)
trajets.head(15)


# In[ ]:


trajets.columns
# ce qui montre que j'ai plus de 25 variables que je vais analyser 


# In[ ]:


# Je verifie la qualité des données
trajets.shape


# In[ ]:


trajets.info()


# In[ ]:


trajets.isna().sum()


# In[ ]:


trajets.duplicated().sum()


# In[ ]:


# Mon etude est vraiment centré sur trois variable clées qui explique et optimise le reseau bibus a Brest
trajets["Retard_Minutes"].describe()
# on vois ici que en moyenne, les bus présentent un retard de 2,5 minuites 
# pour la médiane c'est la moitier des trajets présentent un retard inferieur ou egale a 1,5
# std les retards présentent une variabilité importante autour de la moyenne, ce qui suggere une ponctualité irrégulière selon les trajets


# In[ ]:


trajets["Nb_Passagers"].describe()


# In[ ]:


trajets.columns.tolist()


# In[ ]:


trajets["Note_Confort"].describe()


# In[ ]:


trajets["Meteo"].value_counts()
# ca montre combien de jours de pluie
# combien de jours de beau temps
# quelle catégorie est la plus frequente


# In[ ]:


trajets["Tranche_Horaire"].value_counts()
# ca montre la tranche horaire la plus représenté et la moins representée


# In[ ]:


trajets["Est_Weekend"].value_counts()
# ca montre la proportion du trajet lieu en semaine et la proportion en weekend


# In[ ]:


# Je passe a la visualisation pour mieux comprendre les données car le cerveau comprend mieux les representation que les textes
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))
trajets["Retard_Minutes"].hist(bins=20)
plt.title("Distribution des retards")
plt.xlabel("Retard (minuite)")
plt.ylabel("Nombre de trajets")
plt.show()
# le bins = 20 nous dit de découpé les données en 20 intervalles ou classe 
# les retard sont concentrer au tours d'une valeur


# In[ ]:


# Distribution du nombre de passegers
plt.figure(figsize=(8,5))
trajets["Nb_Passagers"].hist(bins=20)
plt.title("Distributions du nombre de passagers")
plt.xlabel("Nombre de passegers")
plt.ylabel("Nombre de trajets")
plt.show()


# In[ ]:


# Détections des valeurs extremes
#Des retards anormalement élevés
plt.figure(figsize = (8,5))
plt.boxplot(trajets["Retard_Minutes"])
plt.title("Boxplot des retards")
plt.show()


# In[ ]:


# Nombre de passagers
plt.figure(figsize=(8,5))
plt.boxplot(trajets["Nb_Passagers"])
plt.title("Boxplot du nombre de passagers")
plt.show()


# 

# In[ ]:


# Répartition de la météo
trajets["Meteo"].value_counts().plot(kind="bar")
plt.title(" conditions Meteo")
plt.xlabel("Meteo")
plt.ylabel("Nb de Trajets")
plt.show()


# In[ ]:


# répartitions des tranches horraire
trajets["Tranche_Horaire"].value_counts().plot(kind="bar")
plt.title("Répartition des tranches horaires")
plt.xlabel("Tranche Ho")
plt.ylabel("Nombre de trajets")
plt.show()


# In[ ]:


trajets["Est_Weekend"].value_counts().plot(kind="bar")
plt.title("Trajets semaine vs week-end")
plt.show()


# In[ ]:


# retard selon la meteo
trajets.groupby("Meteo")["Retard_Minutes"].mean().plot(kind="bar")
plt.title("Retard moyen selon la meteo")
plt.ylabel("Retard moyens (minutes)")
plt.show()


# In[ ]:


# freaquentation selon les tranches horaire
trajets.groupby("Tranche_Horaire")["Nb_Passagers"].mean().plot(kind="bar")
plt.title("Nombre pass tranche")
plt.show()


# In[ ]:


# confort selon le statut de ponctualité
trajets.groupby("Statut_Ponctualite")["Note_Confort"].mean().plot(kind="bar")
plt.title("Confort moyen sl ponctualité")
plt.show()


# In[ ]:


#import seaborn as sns
#colonnes = [ " Retard_Minutes", "Nb_Passagers", "Taux_Remplissage_Pct", "Note_Confort" ]
#sns.heatmap(
    #trajets[colonnes].corr(),
    #annot=True
#plt.title("Matrice des corrélations")
#plt.show()


# In[ ]:


trajets.groupby("Meteo")["Retard_Minutes"].agg(
    ["count", "mean", "median", "max"]
).sort_values(by="mean", ascending=False)


# In[ ]:


# on constate que Les retards moyens sont plus élevés en cas de pluie et de brouillard. Les conditions météorologiques semblent donc avoir un impact sur la ponctualité du réseau.
# le retard moyen varie de 2,04 minute ( Nuageux) a 4,05 minutes (Vent fort)
# Les conditions météorologiques difficiles sont associées à des retards plus élevés que les conditions normales.


# In[ ]:


trajets.groupby("Incident")["Retard_Minutes"].agg(
    ["count", "mean", "median", "max"]
).sort_values(by="mean", ascending=False)


# 

# In[ ]:


# ici on constate que Les incidents voyageurs génèrent le retard moyen le plus élevé : 3,24 minutes.
#Les trajets touchés par des incidents voyageurs semblent plus perturbés que les autres catégories


# In[ ]:


trajets.groupby("Tranche_Horaire")["Retard_Minutes"].agg(
    ["count", "mean", "median"]
).sort_values(by="mean", ascending=False)


# In[ ]:


# Le retard moyen atteint 4,05 minutes en heure de pointe contre seulement 1,09 minute en heure creuse.
# Les heures de pointe constituent le principal facteur de retard du réseau.


# In[ ]:


trajets.groupby("Ligne")["Retard_Minutes"].agg(
    ["count", "mean", "median"]
).sort_values(by="mean", ascending=False)


# In[ ]:


# La ligne 10 présente le retard moyen le plus élevé (3,05 minutes), tandis que les lignes de tramway T1 et T2 sont les plus ponctuelles.
# Les performances varient selon les lignes, ce qui suggère des contraintes opérationnelles différentes


# In[ ]:


trajets.groupby("Tranche_Horaire")["Nb_Passagers"].agg(
    ["count", "mean", "median", "max"]
).sort_values(by="mean", ascending=False)


# In[ ]:


# La fréquentation moyenne passe de 16 voyageurs en heure creuse à près de 42 voyageurs en heure de pointe.
# La demande est fortement concentrée durant les heures de pointe.


# In[ ]:


trajets[["Retard_Minutes", "Note_Confort"]].corr()
# les retards influencent il le confort?


# In[ ]:


# Une forte relation négative est observée entre les retards et le confort perçu.
# Plus les retards augmentent, plus la note de confort diminue.


# In[ ]:


# A base de toutes ses analyses  on arrive a la conclusion suivante:

# L’analyse des données du réseau Bibus met en évidence plusieurs facteurs influençant la qualité du service. Les retards sont principalement observés durant les heures de pointe, lorsque la fréquentation du réseau atteint son niveau maximal. Les conditions météorologiques défavorables et certains types d’incidents, notamment les incidents voyageurs, contribuent également à la dégradation de la ponctualité.

# L’étude montre également que les performances varient selon les lignes, certaines lignes de bus présentant des retards moyens plus importants que les lignes de tramway. Enfin, une forte relation négative a été observée entre les retards et le confort perçu par les voyageurs, indiquant que la ponctualité constitue un élément essentiel de la qualité de service.

# Ces résultats suggèrent que les actions d’amélioration devraient prioritairement cibler la gestion des heures de pointe, la prévention des incidents et l’optimisation des lignes les plus exposées aux retards afin d’améliorer l’expérience globale des usagers.

