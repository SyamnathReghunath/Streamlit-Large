import streamlit as st

st.write("""
# Largest Number Prediction App
This app predicts the largest among the 3 given numbers(value greater than the other two).
""")
#Get Input

st.header('User Input Parameters')

cnt_children = st.number_input("CNT_CHILDREN",min_value=0,max_value=20,step=1)
cnt_fam_members = st.number_input("CNT_FAM_MEMBERS",min_value=0,max_value=20,step=1)
cnt_new_members = st.number_input("CNT_NEW_MEMBERS",min_value=0,max_value=20,step=1)

st.subheader('Largest Number')
st.write(cnt_children)
    
