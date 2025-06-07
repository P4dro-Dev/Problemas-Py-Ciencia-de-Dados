import numpy as np # Para cálculos numéricos, como a média
import pandas as pd # Para manipular dados em DataFrames e salvar em CSV

# Objetivo: Processar uma lista de números, calcular a média,
# identificar os maiores que a média e salvar em um CSV.

# 1. Usar a lista de números fornecida.
numeros = [12, 45, 67, 23, 89, 34, 22, 90, 56, 78]
print(f"Lista original: {numeros}")

# 2. Calcular a média dos números usando numpy.
media = np.mean(numeros)
print(f"Média: {media:.2f}")

# 3. Identificar os números que são maiores que a média.
numeros_maiores_que_media = [num for num in numeros if num > media]
print(f"Maiores que a média: {numeros_maiores_que_media}")

# 4. Armazenar os números maiores que a média em um DataFrame do pandas.
df_maiores_que_media = pd.DataFrame(numeros_maiores_que_media, columns=['Numeros Maiores que a Media'])
print("\nDataFrame com os resultados:")
print(df_maiores_que_media)

# 5. Salvar o DataFrame em um arquivo CSV.
nome_arquivo = "numeros_maiores_que_media.csv"
df_maiores_que_media.to_csv(nome_arquivo, index=False) # 'index=False' evita salvar a coluna de índice
print(f"\nResultados salvos em '{nome_arquivo}'!")