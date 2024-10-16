# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd

def cal_sales_revenue(price, total_sales):
    return price * total_sales

def cal_cost_of_goods_sold(unit_cost, total_sales):
    return unit_cost * total_sales

def cal_gross_profit(revenue, cogs):
    return revenue - cogs

def cal_operating_profit(gross_profit, operating_expenses):
    return gross_profit - operating_expenses

def cal_net_profit(operating_profit, other_expenses):
    return operating_profit - other_expenses

def main():
    st.title("손익계산서 생성기")
    input_method = st.radio("판매단가와 판매갯수 입력 방법 선택:", ("슬라이더", "직접 입력"))
    
    if input_method == "슬라이더":
        price = st.slider("판매단가", 1000, 10000, value=5000)
        total_sales = st.slider("판매갯수:", 1, 1000, value=500)
        wheat_price = st.slider("밀 가격 (USD)", 100, 500, value=300)
        palm_oil_price = st.slider("팜유 가격 (USD)", 50, 300, value=200)
        exchange_rate = st.slider("달러/원 환율", 1000, 1500, value=1300)
        operating_expenses = st.slider("운영비용", 10000, 500000, value=100000)
        other_expenses = st.slider("기타 비용", 1000, 100000, value=5000)
        depreciation = st.slider("감가상각비", 1000, 100000, value=10000)
        amortization = st.slider("무형자산상각비", 1000, 100000, value=5000)
        interest_income = st.slider("이자 수익", 0, 50000, value=10000)
        interest_expense = st.slider("이자 비용", 0, 50000, value=5000)
    else:
        price = st.number_input("판매단가 입력:", min_value=1000, max_value=10000, value=5000, step=100)
        total_sales = st.number_input("판매갯수 입력:", min_value=1, max_value=1000, value=500, step=1)
        wheat_price = st.number_input("밀 가격 입력 (USD):", min_value=100, max_value=500, value=300, step=10)
        palm_oil_price = st.number_input("팜유 가격 입력 (USD):", min_value=50, max_value=300, value=200, step=10)
        exchange_rate = st.number_input("달러/원 환율 입력:", min_value=1000, max_value=1500, value=1300, step=10)
        operating_expenses = st.number_input("운영비용 입력:", min_value=10000, max_value=500000, value=100000, step=1000)
        other_expenses = st.number_input("기타 비용 입력:", min_value=1000, max_value=100000, value=5000, step=500)
        depreciation = st.number_input("감가상각비 입력:", min_value=1000, max_value=100000, value=10000, step=1000)
        amortization = st.number_input("무형자산상각비 입력:", min_value=1000, max_value=100000, value=5000, step=1000)
        interest_income = st.number_input("이자 수익 입력:", min_value=0, max_value=50000, value=10000, step=1000)
        interest_expense = st.number_input("이자 비용 입력:", min_value=0, max_value=50000, value=5000, step=1000)
    
    # Calculate unit cost based on raw materials (wheat and palm oil)
    wheat_cost = wheat_price * 0.7 * exchange_rate
    palm_oil_cost = palm_oil_price * 0.3 * exchange_rate
    unit_cost = wheat_cost + palm_oil_cost
    
    st.write("판매단가: {:,}원, 판매갯수: {:,}개, 단위당 원가: {:,}원".format(price, total_sales, int(unit_cost)))

    if st.button("손익계산서 생성"):
        revenue = cal_sales_revenue(price, total_sales)
        cogs = cal_cost_of_goods_sold(unit_cost, total_sales)
        gross_profit = cal_gross_profit(revenue, cogs)
        operating_profit = cal_operating_profit(gross_profit, operating_expenses)
        ebitda = operating_profit + depreciation + amortization
        net_interest = interest_income - interest_expense
        net_profit = cal_net_profit(operating_profit, other_expenses) + net_interest - depreciation - amortization
        
        # Financial Ratios
        gross_margin = (gross_profit / revenue) * 100 if revenue != 0 else 0
        operating_margin = (operating_profit / revenue) * 100 if revenue != 0 else 0
        ebitda_margin = (ebitda / revenue) * 100 if revenue != 0 else 0
        net_profit_margin = (net_profit / revenue) * 100 if revenue != 0 else 0
        interest_coverage_ratio = (operating_profit / interest_expense) if interest_expense != 0 else float('inf')
        
        st.write("매출액: {:,}원".format(revenue))
        st.write("매출원가: {:,}원".format(cogs))
        st.write("매출총이익: {:,}원".format(gross_profit))
        st.write("영업이익: {:,}원".format(operating_profit))
        st.write("EBITDA: {:,}원".format(ebitda))
        st.write("감가상각비: {:,}원".format(depreciation))
        st.write("무형자산상각비: {:,}원".format(amortization))
        st.write("이자 수익: {:,}원".format(interest_income))
        st.write("이자 비용: {:,}원".format(interest_expense))
        st.write("순이자 수익/비용: {:,}원".format(net_interest))
        st.write("순이익: {:,}원".format(net_profit))
        
        # Display Financial Ratios
        st.write("\n**재무 지수**")
        st.write("매출총이익률: {:.2f}%".format(gross_margin))
        st.write("영업이익률: {:.2f}%".format(operating_margin))
        st.write("EBITDA 마진: {:.2f}%".format(ebitda_margin))
        st.write("순이익률: {:.2f}%".format(net_profit_margin))
        st.write("이자보상배율: {:.2f}".format(interest_coverage_ratio))

if __name__ == "__main__":
    main()