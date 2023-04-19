import streamlit as st

st.write("""
# Largest Number Prediction App
This app predicts the largest among the 3 given numbers(value greater than the other two).
""")
#Get Input

st.header('User Input Parameters')
col1, col2, col3 = st.columns([1,1,1,])

num1 = col1.number_input("FIRST_NUMBER")
num2 = col2.number_input("SECOND_NUMBER")
num3 = col3.number_input("THIRD_NUMBER")

if st.button ('Predict Largest'):
    
    if num1 >= num2 and num1 >= num3 :
        large = num1
    elif num2 >= num1 and num2 >= num3 :
        large = num2
    else :
        large = num3

    st.subheader('Largest Number')
    st.write(large)
    
