import pandas as pdi

df = pdi.read_csv('fipe_2022.csv',
                  usecols=['year_model' ,'avg_price_brl', 'age_years'],
                  sep=',',
                  encoding='utf-8')

array_yer_model = (df['year_model'].copy())
array_avg_price_brl = (df['avg_price_brl'].copy())
array_yer_model = (df['age_years'].copy())
print(df.head())

