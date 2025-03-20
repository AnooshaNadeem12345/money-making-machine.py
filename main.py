import streamlit as st
import time
import requests
import random

st.title("Money Making Machine")

def generate_money():
    return random.randint(1,1000)

st.subheader("Instant Cash Generator")    
if st.button("Generate Money"):
    st.write("Counting your Money....")
    time.sleep(1)
    amount = generate_money()
st.success(f"Your made ${amount}")   

def fetch_side_hustle():
    try:
        response = requests.get("https://127.0.1:8000/side-hustle")
        if response.status_code == 200:
            hustles =response.json()
            return hustles
        else:
            return("No side hustles found")
    except:
        return("Something went wrong..😟")
    
st.subheader("Side Hustle Ideas")    
if st.button("Generate Hustle"):
     idea=fetch_side_hustle()
     st.success(idea)
