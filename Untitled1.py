#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
dfc = pd.ExcelFile("Bibus")
dfc.sheet_names


# In[3]:


trajets = pd.read_excel("Bibus", header=2)
trajets.head(15)


# In[4]:


import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))
trajets["Retard_Minutes"].hist(bins=20)
plt.title("Distribution des retards")
plt.xlabel("Retard (minuite)")
plt.ylabel("Nombre de trajets")
plt.show()
# le bins = 20 nous dit de découpé les données en 20 intervalles ou classe 
# les retard sont concentrer au tours d'une valeur


# In[5]:


# Distribution du nombre de passegers
plt.figure(figsize=(8,5))
trajets["Nb_Passagers"].hist(bins=20)
plt.title("Distributions du nombre de passagers")
plt.xlabel("Nombre de passegers")
plt.ylabel("Nombre de trajets")
plt.show()


# In[6]:


# Détections des valeurs extremes
#Des retards anormalement élevés
plt.figure(figsize = (8,5))
plt.boxplot(trajets["Retard_Minutes"])
plt.title("Boxplot des retards")
plt.show()


# In[7]:


# Nombre de passagers
plt.figure(figsize=(8,5))
plt.boxplot(trajets["Nb_Passagers"])
plt.title("Boxplot du nombre de passagers")
plt.show()


# In[8]:


# Répartition de la météo
trajets["Meteo"].value_counts().plot(kind="bar")
plt.title(" conditions Meteo")
plt.xlabel("Meteo")
plt.ylabel("Nb de Trajets")
plt.show()


# In[9]:


# répartitions des tranches horraire
trajets["Tranche_Horaire"].value_counts().plot(kind="bar")
plt.title("Répartition des tranches horaires")
plt.xlabel("Tranche Ho")
plt.ylabel("Nombre de trajets")
plt.show()


# In[10]:


trajets["Est_Weekend"].value_counts().plot(kind="bar")
plt.title("Trajets semaine vs week-end")
plt.show()


# In[11]:


# retard selon la meteo
trajets.groupby("Meteo")["Retard_Minutes"].mean().plot(kind="bar")
plt.title("Retard moyen selon la meteo")
plt.ylabel("Retard moyens (minutes)")
plt.show()


# In[12]:


# confort selon le statut de ponctualité
trajets.groupby("Statut_Ponctualite")["Note_Confort"].mean().plot(kind="bar")
plt.title("Confort moyen sl ponctualité")
plt.show()


# In[ ]:




