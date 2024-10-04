# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly
import yfinance as yf
import plotly.graph_objects as go

# 서술형 문제 1
"""
Git hub에서 Repository 이름을 'aopaco'로 만들고, readmefile을 만드는데 체크를 합니다.
Repo가 만들어지면 주소를 복사해서, 만들고자 하는 폴더로 이동해서, git bash를 실행합니다.
git clone (주소)와cd (폴더명)에 접속하고, code .을 입력해. Visual Studio Code를 실행합니다.
가상의 파일 'main.py'를 만들어서 코드를 작성합니다.
가상환경을 만들기 위해, pip install virtualenv와virtualenv venv를 실행해 가상환경을 만듭니다.
이후, source venv/Scripts/activate 를 실행해 가상환경에 접속합니다.
requirements.txt. 파일을 만들어 사용하고자 하는 라이브러리 리스트를 입력하고, 가상환경에 pip install -r requirements.txt를 입력해 라이브러리들을 설치해줍니다.
이후, git hub에 업데이트 하기 위해, git add . 와 git commit -m “updated” 와git push를 실행해 업데이트 합니다.
이를 편리하게 하기 위해 deploy.sh파일을 만들어 해당 내용들을 입력하고 ./deploy.sh를 실행해 업데이트 할 수도 있습니다.
"""

# 코드 문제 1
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i * 2)
print(result)

# 답지
code_result1 = [i * 2 for i in range(10) if i % 2 == 0]
print(code_result1)

# 코드 문제 2
my_dict = {'apple': 3, 'banana': 5, 'orange': 2}

# 답지
for key, value in my_dict.items():
    print(f"{key}: {value}")

# 코드 문제 3
series = pd.Series([25, 35, 45, 60, 75])

# 답지
# np.where를 사용하여 조건 적용
code_result3 = pd.Series(np.where((series > 30) & (series < 60), series + 10, series))
print(code_result3)

# 코드 문제 4
iris = sns.load_dataset("iris")

# 답지
iris.to_csv('output/code4_woongsu.csv', index=True)

# excel 파일로 저장
iris.to_excel('output/code4_woongsu.xlsx', index=True)

# 코드 문제 5
data = [
    ["1,000", "1,100", '1,510'],
    ["1,410", "1,420", '1,790'],
    ["850", "900", '1,185'],
]
columns = ["03/02", "03/03", "03/04"]
df = pd.DataFrame(data=data, columns=columns)

# 답지
def rm_comma(x):
    return int(x.replace(",", ""))

df["03/02"] = df["03/02"].apply(rm_comma)
df["03/03"] = df["03/03"].apply(rm_comma)

df.info()

# 코드 문제 6
apple = yf.download("AAPL", start="2020-01-01", end = "2024-09-30")
fig, ax = plt.subplots()
ax.plot(apple['Open'], label = "Apple")
ax.legend()

# 답지
ax.legend(loc='best')
plt.savefig('output/code6_woongsu.png')
plt.show()

# 코드 문제 7
tips = sns.load_dataset("tips")

# 답지
g = sns.PairGrid(tips, diag_sharey=False)
g.map_offdiag(lambda *args, **kwargs: None)
g.map_diag(lambda *args, **kwargs: plt.hist([], color="white"))
g.axes[1, 1].scatter(tips["total_bill"], tips["tip"])
g.axes[1, 1].set_title('Scatter Plot of Total Bill vs Tip')

plt.savefig('output/code7_woongsu.png')
plt.show()

# 코드 문제 8
apple = yf.download("AAPL", start="2024-05-01", end="2024-09-30")

# 답지
fig = go.Figure(data=[
    go.Candlestick(
        x=apple.index,
        open=apple['Open'],
        high=apple['High'],
        low=apple['Low'],
        close=apple['Close'],
        name='AAPL'
    )
])
fig.update_traces(increasing_line_color='green', decreasing_line_color='red')

fig.update_layout(
    title='AAPL Candlestick Chart (2020-2024)',
    xaxis_title='Date',
    yaxis_title='Price (USD)',
    xaxis_rangeslider_visible=False,
    template='plotly_white'
)

fig.show()