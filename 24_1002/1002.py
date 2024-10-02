from pandas import DataFrame

data = [
    ["037730", "3R", 1510],
    ["036360", "3SOFT", 1790],
    ["005670", "ACTS", 1185]
]

columns = ["종목코드", "종목명", "현재가"]
df = DataFrame(data=data, columns=columns)
df.set_index("종목코드", inplace=True)

# ascending=False : 내림차순
# ascending=True (기본값) : 오름차순
#print(df.sort_values(by="종목명", ascending=False)) 
#print(df.sort_values(by="종목명", ascending=True))

#print(df.sort_index()) # 기본값
#print(df.sort_index(ascending=False)) # 역순

# 인덱스 연산
# 합집합, 교집합, 차집합의 원리를 이용해서, 데이터 병합을 할 때 사용
import pandas as pd
idx1 = pd.Index([1, 2, 3])
idx2 = pd.Index([2, 3, 4])

print(idx1.union(idx2))
print(idx1.intersection(idx2))
print(idx1.difference(idx2))