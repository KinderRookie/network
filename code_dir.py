

import pandas as pd
import numpy as np

# 데이터 준비
assem1 = pd.read_csv('./asone.csv', encoding='cp949').fillna("")
mem = pd.read_csv('./meber_data.csv', encoding='cp949').fillna("")


total = []

# 공동발의자와 대표발의자를 합치는 단계
for i in range(0, len(assem1)):
    lists = assem1.loc[i, '공동발의자'].split(',')
    lists.append(assem1.loc[i, '대표발의자'])
    total.append(lists) # total에는 리스트를 넣어준다. 


# 즉, total은 리스트(발의안을 낸 국회의원들)의 리스트이다.


print('\n')

# 이제 total에 있는 이름 리스트를 다루기 편하게 id로 치환하자. 
for i in range(0, len(total)):
    temp = total[i]
    for j in range(0, len(temp)):
        temp[j] = (mem['이름']==temp[j]).idxmax()
    total[i] = temp

print(total)


# 공동발의로 참여한 횟수만큼 누적함.
# edge_pre.csv에는 관계와 0으로 초기화된 Weight 데이터가 존재한다.
## 시간이 6분 이상 걸린다...
edges = pd.read_csv('edge_pre.csv')
for temp in total:
    for i in range(0, len(temp)-1):
        # +1 씩 누적한다.
        edges.loc[(edges['Source']==temp[i]) & (edges['Target']==temp[-1]), 'Weight'] += 1


# 누적한 edges 파일을 import
edges.to_csv('./edges_di.csv', index=False)


# 이후 Weight == 0 인 행은 Excel을 통해 제거한다.

