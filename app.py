import streamlit as st
st.title("Power calculator")
st.write("Enter a number to calculatee its square,cube and fifth power.")

n=st.number_input("enter the number",value=1,step=1)
square=n**2
cube=n**3
fifth_power=n**5

st.write(f"The square of {n} is {square}")
st.write(f"The cube of {n} is {square}")
st.write(f"The square of {n} is {square}")