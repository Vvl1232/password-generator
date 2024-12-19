import random as rd
import streamlit as st

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '+','<', '>', '?', '/']

st.title("🔒 Password Generator 🔒")

password_letters = st.number_input("🔡 Enter the number of letters you want in your password:", min_value=2, max_value=12)
password_numbers = st.number_input("🔢 Enter the number of numbers you want in your password:", min_value=1, max_value=4)
password_symbols = st.number_input("🔣 Enter the number of symbols you want in your password:", min_value=1, max_value=2)

password = ""

for i in range(password_letters):
    password += rd.choice(letters)
for i in range(password_numbers):
    password += rd.choice(numbers)
for i in range(password_symbols):
    password += rd.choice(symbols)

# Shuffle the password to ensure randomness
password = ''.join(rd.sample(password, len(password)))

st.warning(f"Total length of password: {password_letters + password_numbers + password_symbols}")

if st.button("Generate"):
    st.info(f"🔑 Generated Password: **{password}**")
