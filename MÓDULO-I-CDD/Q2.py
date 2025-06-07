import pandas as pd
import numpy as np

# Dados de entrada fornecidos
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo'],
    'Idade': [28, 34, 29, None, 42],
    'Cidade': ['São Paulo', 'Rio de Janeiro', None, 'Curitiba', 'Belo Horizonte'],
    'Vendas': [150, 200, 300, 400, None]
}

print("--- Dados Originais ---")
print(dados)

# 1. Crie um DataFrame com base nos dados fornecidos
df_clientes = pd.DataFrame(dados)
print("\n--- DataFrame Criado ---")
print(df_clientes)

# 2. Filtre os clientes que têm mais de 30 anos
# Atenção: A coluna 'Idade' pode ter valores nulos (None/NaN),
# então vamos primeiro garantir que só filtramos números para evitar erros.
# Usamos .dropna() na coluna 'Idade' para esta filtragem específica,
# ou podemos usar uma condição que ignore NaN automaticamente.
# Vamos usar df_clientes['Idade'] > 30, o Pandas trata NaN como False para comparações.
clientes_mais_de_30 = df_clientes[df_clientes['Idade'] > 30]
print("\n--- Clientes com mais de 30 anos ---")
print(clientes_mais_de_30)

# 3. Calcule a média de idade dos clientes
# numpy.mean() ou pandas.DataFrame.mean() ignoram valores NaN por padrão.
media_idade = df_clientes['Idade'].mean()
print(f"\n--- Média de Idade dos Clientes: {media_idade:.2f} anos ---")

# 4. Substitua valores faltantes na coluna 'Cidade' por 'Desconhecido'
df_clientes['Cidade'].fillna('Desconhecido', inplace=True)
print("\n--- DataFrame com valores faltantes na 'Cidade' preenchidos ---")
print(df_clientes)

# 5. Calcule a soma total das vendas
# numpy.sum() ou pandas.DataFrame.sum() também ignoram valores NaN por padrão.
soma_vendas = df_clientes['Vendas'].sum()
print(f"\n--- Soma Total das Vendas: R$ {soma_vendas:.2f} ---")

print("\nAnálise concluída!")
print("O DataFrame final, após as operações de limpeza e filtragem, é:")
print(df_clientes)