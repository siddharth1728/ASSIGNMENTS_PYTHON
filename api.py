import streamlit as st 

import streamlit as st
import requests


st.title("Rhyming Words Finder")

word = st.text_input("Enter a word", placeholder="Eg. Donkey ")
is_clicked = st.button("Generate", type='primary')

if is_clicked:
    response = requests.get(f"https://dummy-backend-batch-2.vercel.app/?word={word}")
   
    if response.status_code == 200:
        data = response.json()
        for item in data:
            st.write(item.get('word'))
    else:
        st.toast("Soemthing went wrong")
