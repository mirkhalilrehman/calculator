import streamlit as st

st.title("SIMPLE CALCULATOR")
a=st.number_input("Enter First No")
b=st.number_input("Enter 2nd No")
c=hobby = st.selectbox("Operation: ",
                     ['Addition', 'Multiplication', 'Division','Subtraction'])
if c=='Addition':
    r=a+b
elif c=='Subtraction':
    r=a-b
elif c=='Multiplication':
    r=a*b
elif c=='Division':
    if b!=0:
        r=a//b
    else:
        r='Error! cant divide by 0'

st.write(r)