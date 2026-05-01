#streamlit run filename.py
import streamlit as st

st.title("Simple Calculator")
# st.subheader("Enter two numbers and select an operation")
st.markdown("Enter two numbers and select an operation")

c1,c2 = st.columns(2)
fnum = c1.number_input("Enter first number", value=0)
snum = c2.number_input("Enter second number", value=0)

options = ["Addition", "Subtraction", "Multiplication", "Division"]
choice = st.radio("Select an operation", options)

button = st.button("Calculate")

result = 0
if button:
    if choice == "Addition":
        result = fnum + snum
    if choice == "Subtraction":
        result = fnum - snum
    if choice == "Multiplication":
        result = fnum * snum
    if choice == "Division":
        result = fnum / snum
st.success(f"Result: {result}")
# st.snow()
# st.balloons()