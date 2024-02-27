# Importação das Bibliotecas que serão utilizadas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

# Definindo o caminho do arquivo para facilitar manipulações futuras
path_to_file = r'C:\Workspace\CURSO ADA TECH\MODULO II - tecnicas de programação\projeto_ccvil\data_cno\cno.parquet'

# Carregando os dados em um DataFrame
df_cno = pd.read_parquet(path_to_file)

# Removendo duplicatas para garantir a unicidade dos registros
df_cno = df_cno.drop_duplicates()

# Filtrando os dados para manter apenas registros do Brasil
exclude_values = ['A DESIGNAR', 'ARGENTINA', 'AUSTRIA']
df_cno = df_cno[~df_cno['Nome do pais'].isin(exclude_values)]

# Removendo registros atrelados a estados não relevantes para a análise
df_cno = df_cno[~df_cno['Estado'].isin(['EX'])]

# Mapeando códigos numéricos para situações legíveis
situation_mapping = {
    1: 'NULA',
    2: 'ATIVA',
    3: 'SUSPENSA',
    14: 'PARALISADA',
    15: 'ENCERRADA',    
}
df_cno['Situação'] = df_cno['Situação'].replace(situation_mapping)

# Preenchendo dados numéricos nulos com 0 para colunas específicas
numeric_columns_with_nulls = ['CNO vinculado', 'NI do responsável', 'Caixa Postal']
df_cno.loc[df_cno[numeric_columns_with_nulls].isna().any(axis=1), numeric_columns_with_nulls] = 0

# Preenchendo dados do tipo objeto nulos com espaço vazio para colunas específicas
object_columns_with_nulls = ['Nome', 'Número do logradouro', 'Logradouro', 'Bairro', 'Complemento', 'Nome empresarial', 'Código de localização']
df_cno.loc[df_cno[object_columns_with_nulls].isna().any(axis=1), object_columns_with_nulls] = ' '

# Convertendo colunas com datas para o formato datetime
date_columns = ["Data de início", "Data de inicio da responsabilidade", "Data de registro", "Data da situação"]
for column in date_columns:
    df_cno[column] = pd.to_datetime(df_cno[column])

# Análise de obras ativas por estado
masc = df_cno['Situação'] == 'ATIVA'
obras_estado = df_cno.loc[masc, ['Estado']].value_counts().reset_index()
obras_estado.columns = ['Estado', 'Quantidade de Obras']

# Visualização gráfica do número de obras ativas por estado
plt.figure(figsize=(12,8))
sns.barplot(x='Quantidade de Obras', y='Estado', hue='Estado', data=obras_estado, palette='rocket')
plt.title('Quantidade de Obras ativas por Estado brasileiro')
plt.xscale('log')
plt.show()

# Análise de obras ativas por município (top 25 cidades)
obras_municipio = df_cno.loc[masc, ['Nome do município', 'Estado']].value_counts().reset_index()
obras_municipio.columns = ['Nome do município', 'Estado', 'Quantidade de Obras']
obras_municipio = obras_municipio.head(25)

# Visualização gráfica do número de obras ativas por município
plt.figure(figsize=(12,8))
sns.barplot(x='Quantidade de Obras', y='Nome do município', hue='Estado', data=obras_municipio, palette='rocket')
plt.title('Quantidade de Obras ativas por município, por Estado brasileiro')
plt.xscale('log')
plt.show()

# Adicionando coluna com o ano da situação
df_cno['Ano da Situação'] = df_cno['Data da situação'].dt.year

# Filtro de obras ativas por ano, considerando apenas o intervalo de 2016 a 2023
filtro_ativas_ano = df_cno[(df_cno['Situação'] == 'ATIVA') & (df_cno['Ano da Situação'] >= 2016) & (df_cno['Ano da Situação'] <= 2023)]
obras_ativas_ano = filtro_ativas_ano.groupby(['Estado', 'Ano da Situação']).size().reset_index(name='Quantidade de Obras')

# Visualização de obras ativas por ano em cada estado
g = sns.FacetGrid(obras_ativas_ano, col="Estado", col_wrap=5, height=3)
g.map(sns.lineplot, "Ano da Situação", "Quantidade de Obras")
g.add_legend()
plt.show()
