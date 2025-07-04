import requests
import streamlit as st
 
print("***RHYMING WORD GENERATOR*****")
choice = input('Enter a word:')
endpoint = f"https://api.dhttps://api.datamuse.com/words?ml=i%20am%20studentatamuse.com/words?sp={choice}"
 
response = requests.get(endpoint)
 
data = response.json()
 
if response.status_code == 200:
    for item in data:
        print(item.get('tag'[0]))