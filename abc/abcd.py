from pandas import DataFrame

data = {
    "종목명": ["3R", "3SOFT", "ACTS"],
    "현재가": [1510, 1790, 1185],
    "등락률": [7.36, 1.65, 1.28],
}

df = DataFrame(data, index=["037730", "036360", "005760"])
# print(df)

import seaborn as sns
import pandas as pd

# CSV 파일로 저장
df.to_csv("today_stock.csv", index=True)

# excel 파일로 저장
df.to_excel("today_stock.xlsx", index=True)