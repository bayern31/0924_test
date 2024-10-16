import pandas as pd
import streamlit as st

def load_data():
    train = pd.read_csv('./data/train.csv')
    return train

def main():
    st.title("Stacked Bar Plot loan_intent vs loan_status")
    
    # 데이터 로드
    df = load_data()

    # Streamlit 위젯을 사용해 feature와 target 선택
    features = df.columns.tolist()
    feature = st.selectbox("Select the feature:", features)
    target = st.selectbox("Select the target:", features)

    # 이후 분석 로직 계속...

if __name__ == "__main__":
    main()
