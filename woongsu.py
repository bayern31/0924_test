import pandas as pd

df1 = pd.read_excel("C:/0924_test/1004_test/ss_ex_1.xlsx", parse_dates=['일자'], index_col=0)
df1.info()
print(df1)

df1 = df.reset_index()
#print(df.head(1))
#print(df.info())
#print(df['일자'.dt.quarter])
print(df1['일자'].dt.year)
print(df1['일자'].dt.month)
print(df1['일자'].dt.day)

# column 추가
