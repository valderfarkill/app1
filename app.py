import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlsxwriter

st.text("Calcoliamo")
# # ###################################################
#latex
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# # slider
x1 = st.slider('Please inserisci base triangolo', 0, 100, 25)
x2 = st.slider('Please inserisci altezza triangolo', 0, 100, 35)

def area(b:float,h:float):
    a = b*h/2
    return a 

st.write("l'area triangolo è ", area(x1,x2))

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

###### CSS BACKGROUND #######################
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.androidworld.it/wp-content/uploads/2021/03/ROG-Phone-5-Wallpaper-4-YTECHB.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
add_bg_from_url() 


url = "https://soundcloud.com/mc-hammer-official/u-cant-touch-this?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing"
audio_bytes = st.audio(url, format="audio/mp3")

if audio_bytes is not None:
    st.write("Playing audio from URL:", url)


# #####################
### Footer #########
def show_footer():
    st.markdown("***")
    st.markdown(""" **Do you like this example app?** Follow me on
                [Linkedin](https://www.linkedin.com/in/daniele-grotti-38681146/).""")

show_footer()