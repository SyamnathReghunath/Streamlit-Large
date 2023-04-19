import streamlit as st

st.write("""
# Largest Number Prediction App
This app predicts the largest among the 3 given numbers(value greater than the other two).
""")
#Get Input

st.header('User Input Parameters')

num1 = st.number_input("FIRST_NUMBER")
num2 = st.number_input("SECOND_NUMBER")
num3 = st.number_input("THIRD_NUMBER")

if st.button ('Find Largest'):
    
    if num1 >= num2 and num1 >= num3 :
        large = num1
    elif num2 >= num1 and num2 >= num3 :
        large = num2
    else :
        large = num3

st.subheader('Largest Number')
st.write(large)
    
