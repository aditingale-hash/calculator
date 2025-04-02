import streamlit as st
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import calculator


st.title("🧮 Simple Calculator")

a = st.number_input("Enter first number", value=0)
b = st.number_input("Enter second number", value=0)

operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    try:
        if operation == "Add":
            result = calculator.add(a, b)
        elif operation == "Subtract":
            result = calculator.subtract(a, b)
        elif operation == "Multiply":
            result = calculator.multiply(a, b)
        elif operation == "Divide":
            result = calculator.divide(a, b)
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(str(e))
