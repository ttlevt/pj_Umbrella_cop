import pandas as pd
import numpy as np

column_name = ['date', 'hr', 'mm', 'percent', 'cloudy']
df = pd.read_csv('./project_data/train/suwon_ttl.csv', encoding='utf8')
df.columns = column_name
#컬럼명 재설정 및 fillna 코드로 결측치 처리 ( 강수시간, 강수량만 습도와 전운량은 not null상태임)
df.fillna(0, inplace=True)

# print(df)

output_file = r'./project_data/train/suwon_ttl.csv'
df.to_csv(output_file, index=False)