# 관계망과 가중치=0으로 초기화 하는 코드

import pandas as pd
num = 0
data = pd.read_csv('edge_temp.csv')
for i in range(0, 292):
    for j in range(0, 292):
        if i==j:
            pass
        else:
            data.loc[num]=[i, j, 'Directed', 0]

        num += 1

print(data.head())


data.to_csv('./edge_pre.csv', index=False)