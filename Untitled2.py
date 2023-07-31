#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

#Adquirindo a Tabela de filmes e limpandos os dados zerados

url = "https://pt.wikipedia.org/wiki/Lista_de_filmes_de_maior_bilheteria"
data = pd.read_html(url)
data = data[0]  # Índice 0 representa o primeiro DataFrame na lista
data
data.rename(columns={'Bilheteria (US$)': 'Bilheteria'}, inplace=True)
bilheteria = data['Bilheteria'].str.replace(' ', '')
bilheteria


# In[ ]:




