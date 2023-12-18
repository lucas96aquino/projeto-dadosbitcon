#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Importar as libs

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly.graph_objects as Dash

# Lib para ignorar avisos
import warnings

# Desabilitando avisos
warnings.filterwarnings('ignore')


# In[2]:


path = r"C:\Users\Lucas Aquino\Downloads\Dados_Bitcoin.xlsx"

Base_Dados = pd.read_excel(path)


# In[3]:


Base_Dados.head()


# In[4]:


Base_Dados.dtypes


# In[7]:


# Setar o index

Base_Dados.set_index('Date', inplace=True)

# Gráfico de Linhas

fig = px.line(Base_Dados, y='Close')

#Plotar

fig.show()


# In[8]:


# Gerar médias moveis

Media_Movel = Base_Dados['Close'].rolling(5).mean()
Media_Tendencia = Base_Dados['Close'].rolling(30).mean()


# In[9]:


Media_Movel


# In[34]:


# Criar Dashboard

# Criando uma Figura
Figura = Dash.Figure()

# Adicionando o primeiro eixo
Figura.add_trace(
    Dash.Scatter(
        x = Base_Dados.index,
        y = Base_Dados.Close,
        mode = 'lines',
        name = 'Fechamento',
        marker_color = '#ff7f0e',
        opacity = 0.5
    )
)

# Adicionando a Media
Figura.add_trace(
    Dash.Scatter(
        x = Base_Dados.index,
        y = Media_Movel,
        mode = 'lines',
        name = 'Média Móvel',
        marker_color = '#d62728',
        opacity = 0.5
    )
)

# Adicionando a Tendência
Figura.add_trace(
    Dash.Scatter(
        x = Base_Dados.index,
        y = Media_Tendencia,
        mode = 'lines',
        name = 'Tendencia',
        marker_color = '#2ca02c'
    )
)

# Ajustes no Layout

Figura.update_layout(
    
    # Titulo
    title='Análise do Fechamento de Bitcoins',
    # Tamanho do Título
    titlefont_size=20,
    
    # Ajustando o eixo X
    xaxis = dict(
        title='Período Histórico',
        titlefont_size=14,
        tickfont_size=10
    ),
    
    # Ajustando o eixo Y
    yaxis = dict(
        title='Valor em Dólar ($)',
        titlefont_size=14,
        tickfont_size=10
    ),
    
    # Parâmetros para Legenda
    legend = dict(
        y=1,
        x=1
    )
    
)


# In[ ]:




