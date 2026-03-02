import pandas as pd

df = pd.read_csv('fipe_2022.csv',
                 usecols=['year_model', 'avg_price_brl', 'age_years'],
                 sep=',',
                 encoding='utf-8')

df = df.dropna()

media_ano = df['year_model'].mean()
mediana_idade = df['age_years'].median()
moda_preco = df['avg_price_brl'].mode()[0]

max_ano = df['year_model'].max()
min_ano = df['year_model'].min()
amplitude_ano = max_ano - min_ano

desvio_preco = df['avg_price_brl'].std()
variancia_idade = df['age_years'].var()

print("="*60)
print("       TRABALHO DE ESTATÍSTICA - TABELA FIPE 2022")
print("="*60)

print(f"MÉDIA (Ano do Modelo):        {media_ano:.0f}")
print(f"MEDIANA (Idade dos Carros):   {mediana_idade:.1f} anos")
print(f"MODA (Preço Médio):           R$ {moda_preco:,.2f}")

print("-" * 60)
print(f"AMPLITUDE (Ano):              {amplitude_ano} anos (De {min_ano} a {max_ano})")
print(f"DESVIO PADRÃO (Preço):        R$ {desvio_preco:,.2f}")
print(f"VARIANTE/VARIÂNCIA (Idade):    {variancia_idade:.2f}")

print("-" * 60)
print(f"Total de registros analisados: {len(df)} linhas.")
print("="*60)