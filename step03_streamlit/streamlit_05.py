# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def cal_sales_revenue(price, total_sales):
    revenue = price * total_sales
    return revenue

def main():
    st.title("여기에서부터 시작")
    input_method = st.radio("단가와 판매갯수 입력 방법 선택:", ("슬라이더", "직접 입력"))
    
    if input_method == "슬라이더":
        price = st.slider("단가", 1000, 10000, value=5000)
        total_sales = st.slider("판매갯수:", 1, 1000, value=500)
    else:
        price = st.number_input("단가 입력:", min_value=1000, max_value=10000, value=5000, step=100)
        total_sales = st.number_input("판매갯수 입력:", min_value=1, max_value=1000, value=500, step=1)
    
    st.write("단가: {:,}원, 판매갯수: {:,}개".format(price, total_sales))

    # 시각화 선택
    st.write("## 시각화 옵션")
    show_price_hist = st.checkbox("단가 히스토그램")
    show_sales_hist = st.checkbox("판매갯수 히스토그램")
    show_revenue_line = st.checkbox("매출액 라인 그래프")

    # 시각화
    if show_price_hist:
        fig, ax = plt.subplots()
        prices = np.random.normal(price, 500, 100)  # 단가의 예시 데이터를 생성
        ax.hist(prices, bins=20, color='skyblue', edgecolor='black')
        ax.set_title('단가 히스토그램')
        ax.set_xlabel('단가 (원)')
        ax.set_ylabel('빈도')
        st.pyplot(fig)

    if show_sales_hist:
        fig, ax = plt.subplots()
        sales = np.random.normal(total_sales, 50, 100)  # 판매갯수의 예시 데이터를 생성
        ax.hist(sales, bins=20, color='lightgreen', edgecolor='black')
        ax.set_title('판매갯수 히스토그램')
        ax.set_xlabel('판매갯수 (개)')
        ax.set_ylabel('빈도')
        st.pyplot(fig)

    if show_revenue_line:
        fig, ax = plt.subplots()
        sales_range = np.linspace(1, total_sales, 100)
        revenues = cal_sales_revenue(price, sales_range)
        ax.plot(sales_range, revenues, color='coral')
        ax.set_title('매출액 라인 그래프')
        ax.set_xlabel('판매갯수 (개)')
        ax.set_ylabel('매출액 (원)')
        st.pyplot(fig)

if __name__ == "__main__":
    main()