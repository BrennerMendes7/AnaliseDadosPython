# pip install pandas, numpy, openpyxl, plotly
import pandas as pd
import plotly.express as px # biblioteca de gráficos

# Passo 1: Importar a base de dados
tabela = pd.read_csv("telecom_users.csv") # ler arquivo csv

# Passo 2: Visualizar a base de dados
print(tabela)

# Passo 3: Tratamento de dados (corrigir os problemas da base de dados)
# axis = eixo
# axis = 0 -> linha
# axis = 1 -> coluna
tabela = tabela.drop("Unnamed: 0", axis=1) # deletar coluna inútil
print(tabela)

# valores reconhecidos de forma errada
# object -> texto
# int -> números inteiros
# float -> números com casa decimal
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce") # transformar coluna em númerico, coerce = tratamento de erro para botar valor vazio
print(tabela.info()) # mostrar informações da tabela

# tratar valores vazios
# how="all" -> deletar linha ou coluna que está totalmente vazia
# how="any" -> deletar linha ou coluna inteira que possui pelo menos um valor vazio
tabela = tabela.dropna(how="all", axis=1) # dropna = deletar valores vazios, excluir colunas vazias
tabela = tabela.dropna(how="any", axis=0) # excluir as linhas que tem algum valor vazio
print(tabela.info()) # mostrar informações da tabela

# Passo 4: Análise Inicial
print(tabela["Churn"].value_counts()) # contar valores da coluna Churn
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format)) # contar valores da coluna Churn e colocar em percentual

# Passo 5: Análise detalhada dos clientes
for coluna in tabela.columns: # repetir o processo com todas as colunas da tabela
    grafico = px.histogram(tabela, x=coluna, color="Churn") # criar gráfico histogram, x = informações do eixo x do gráfico, color = separação de cor do gráfico
    grafico.show() # mostrar o gráfico