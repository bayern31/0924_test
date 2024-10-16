# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd

# 캐시메모리는 대용량 데이터는 불러오면 안됨
# 현업 : SQL 데이터 가공을 일부 진행
# 쉽게 말하면 Raw 데이터는 끌고 오면 안됨
@st.cache_data
def load_data():
    train = pd.read_csv('./data/train.csv')
    return train

def main():
    st.title("여기서부터 시작")

    train = load_data()
    print(train.head())
    st.data_editor(train)
    # st.table(train) 가급적 쓰지 말자

if __name__== "__main__":
    main()