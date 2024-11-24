import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# pd.set_option('display.width',None)
# pd.set_option('display.max_colwidth',None)

# Ler o arquivo no dataframe df
df = pd.read_csv('ecommerce_preparados.csv')

print(df.info())

# Print do início e fim do arquivo para avaliar os dados
# print(df.head().to_string())
# print(df.tail().to_string())

df.drop(['Desconto','Review1','Review2','Review3'],axis=1,inplace=True)
print('Dataframe depois do drop:\n',df.info())

# Verificação do % de dados nulos
print('% de dados nulos:\n',df.isnull().mean()*100)             # Nenhum valor nulo: Título, Marca, Temporada, Qtd_Vendidos, Marca_Cod, Material_Cod, Temporada_Cod, Marca_Freq

x = df['Gênero'].value_counts().index
y = df['Gênero'].value_counts().values

# Fazendo um gráfico de Pizza de Gênero
plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
plt.pie(y,autopct='%.1f%%',startangle=0)
plt.title('Representatividade de Gênero')
plt.legend(x,title='Gênero:',loc='lower center',bbox_to_anchor=(0.5, -0.05),ncol=3,fontsize='x-small')
plt.axis('equal')


# Fazendo um gráfico de Barras de Gênero
plt.subplot(1,2,2)
plt.bar(x,y)
plt.title('Gênero e quantidade')
plt.xlabel('Gênero')
plt.ylabel('Quantidade')
plt.xticks(rotation=90)


df_corr = df[['Nota_MinMax','N_Avaliações_MinMax','Preço_MinMax','Qtd_Vendidos_Cod']].corr()

# Heatmap de correlação entre variáveis normalizadas (Nota, Número de Avaliações, Preço e Qtd. Vendidos)
plt.figure(figsize=(10,6))
sns.heatmap(df_corr,annot=True)
plt.title('Mapa de Correlação entre Nota, Nº de Avaliações, Preço e Quantidade de vendas')

# Fazendo um gráfico de Densidade 
plt.figure(figsize=(10,6))
sns.kdeplot(x='Nota',data=df,fill=False)
plt.title('Densidade Nota')
plt.xlabel('Nota')
plt.ylabel('Quantidade')

# Fazendo um gráfico de Dispersão para analisar Preço e Quantidade de vendas
plt.figure(figsize=(10,6))
sns.jointplot(x='Preço',y='Qtd_Vendidos_Cod',data=df,kind='scatter')
plt.title('Preço x Quantidade de vendas')
plt.xlabel('Preço')
plt.ylabel('Quantidade de Vendas')

plt.tight_layout()
plt.show()

