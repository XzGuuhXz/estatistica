import pandas as pdi

df = pdi.read_csv('fipe_2022.csv',
                  usecols=['year_model' ,'avg_price_brl', 'age_years'],
                  sep=',',
                  encoding='utf-8')

print(df.head())

