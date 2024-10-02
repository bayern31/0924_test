from pandas import DataFrame

#data = [
#   ["036360", "3SOFT", 1790],
#    ["005670", "ACTS", 1185]
#]

#columns = ["종목코드", "종목명", "현재가"]
#df = DataFrame(data=data, columns=columns)
#df.set_index("종목코드", inplace=True)

# ascending=False : 내림차순
# ascending=True (기본값) : 오름차순
#print(df.sort_values(by="종목명", ascending=False)) 
#print(df.sort_values(by="종목명", ascending=True))

#print(df.sort_index()) # 기본값
#print(df.sort_index(ascending=False)) # 역순

# 인덱스 연산
# 합집합, 교집합, 차집합의 원리를 이용해서, 데이터 병합을 할 때 사용
#import pandas as pd
#idx1 = pd.Index([1, 2, 3])
#idx2 = pd.Index([2, 3, 4])

#print(idx1.union(idx2))
#print(idx1.intersection(idx2))
#print(idx1.difference(idx2))

from pandas import DataFrame

data = [
    ["2차전지(생산)", "SK이노베이션", 10.19, 1.29],
    ["해운", "팬오션", 21.23, 0.95],
    ["시스템반도체", "티엘아이", 35.97, 1.12],
    ["해운", "HMM", 21.52, 3.20],
    ["시스템반도체", "아이에이", 37.32, 3.55],
    ["2차전지(생산)", "LG화학", 83.06, 3.75]
]

columns = ["테마", "종목명", "PER", "PBR"]
df = DataFrame(data=data, columns=columns)
#print(df)

result = df.groupby("테마")[["PER", "PBR"]].mean()
#print(result, type(result))

print(df.groupby("테마").get_group("2차전지(생산)"))
print(df.groupby("테마").get_group("해운"))
print(df.groupby("테마").get_group("시스템반도체"))