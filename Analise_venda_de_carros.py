import pandas as pd 
import matplotlib.pyplot as plt

# importar o arquivo
tabela_vendas = pd.read_csv("venda de carros.csv")

# visualizar o arquivo
print(tabela_vendas)
print("*"*50)
print()
print()
# criando listas separadas para datas e quantidades
datas = [
    '31/01/2017', '28/02/2017', '31/03/2017', '30/04/2017', '31/05/2017', '30/06/2017',
    '31/07/2017', '31/08/2017', '30/09/2017', '31/10/2017', '30/11/2017', '31/12/2017',
    '31/01/2018', '28/02/2018', '31/03/2018', '30/04/2018', '31/05/2018', '30/06/2018',
    '31/07/2018', '31/08/2018', '30/09/2018', '31/10/2018', '30/11/2018', '31/12/2018'
]

quantidades = [
    10, 30, 31, 47, 63, 81, 101, 124, 148, 174, 201, 230,
    261, 303, 326, 362, 400, 448, 483, 527, 573, 621, 670, 721
]

# criando o DataFrame
df = pd.DataFrame({
    'Data':datas,
    'Quantidade':quantidades
})

# Convertendo a coluna 'Data' para o tipo datetime
# Isso é importante para podermos extrair o ano depois
df['Data'] = pd.to_datetime(df['Data'], dayfirst = True)
# Conversão de datas: Converti a coluna 'Data' para o tipo datetime, que permite trabalhar com funções de data.
#  O parâmetro dayfirst=True indica que o dia vem primeiro no formato (dd/mm/aaaa).


#extraindo o ano de cada adta e crianfo uma nova coluna 'ano'
df['Ano'] = df['Data'].dt.year

# agora agrupar por ano e somar as quantidades
vendas_por_ano = df.groupby('Ano')['Quantidade'].sum().reset_index()

# renomeando a coluna para ficar masi claro 
vendas_por_ano.columns = ['Ano','Total de Vendas']

# Mostrando o resultado
print(vendas_por_ano)




vendas_por_ano.plot(kind='bar', x='Ano', y='Total de Vendas')
plt.title('Vendas de Carros por Ano')
plt.ylabel('Total de Vendas')
plt.show()