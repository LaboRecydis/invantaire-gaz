import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
#import matplotlib
#import matplotlib.pyplot as plt
#matplotlib.use('Agg')
import json
#import plotly.express as px
import altair as alt





if __name__=="__main__":
    st.set_page_config(
        page_title="Streamlit basics app",
        layout="centered"
    )

    st.title("Analyses pour déterminer la fillière de traitement adéquate")

    st.write("Auteur : Brahim AIT OUALI  - Technicien chimiste")
    st.write("GRV de résines AKZO non pompables")
    st.write("Pâteux visqueux non pompable")
   
    # Display the LOGO
    img1 = Image.open("IMG_PAPREC.jpg")
    img2 = Image.open("IMG_RECYDIS.jfif") 
    
  
    st.sidebar.image(img1, width=250)
    st.sidebar.image(img2, width=250)


    
#     st.write("Photos du déchet")
#     st.image(img4, width=250)
#     st.image(img3, width=250)
    
    st.write("Vidéos : butane - propane")
    st.write("* Partie 1)
    video_file = open('prop-1_zmdztHeY.mp4', 'rb')
    video_bytes = video_file.read()

#     st.video(video_bytes)
    
#     st.write("Point éclair = 115,0 °C")
#     st.image(img5)
#     st.write("Pas de chlore (test de flamme négatif au chlore)")
  


  
    



