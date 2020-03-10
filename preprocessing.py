import pandas as pd
import numpy as np

column_name = ['date', 'hr', 'mm', 'percent', 'cloudy']
df = pd.read_csv('./project_data/train/suwon_ttl.csv', encoding='utf8')
df.columns = column_name

df.fillna(0, inplace=True)

print(df)

output_file = r'./project_data/train/suwon_ttl.csv'
df.to_csv(output_file, index=False)