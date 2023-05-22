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

    st.title("Inventaire gaz")

    st.write("Auteur : Brahim AIT OUALI  - Technicien chimiste")
  
   
    # Display the LOGO
    img1 = Image.open("IMG_PAPREC.jpg")
    img2 = Image.open("IMG_RECYDIS.jfif") 
    
  
    st.sidebar.image(img1, width=250)
    st.sidebar.image(img2, width=250)

    
    st.write(" * ## Butane / Propane")
    
    st.write("* Première partie : visualisez la vidéo s'il vous plaît")
    video_file = open('prop-1_zmdZtHeY.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    st.write("* Deuxième partie : visualisez la vidéo s'il vous plaît")
    video_file = open('PROP_2.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    st.write("* Troisième partie : visualisez la vidéo s'il vous plaît")
    video_file = open('PROP_3.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    st.write("* Quatième partie")
    img_PROP_4 = Image.open("PROP_4.jpg")
    st.image(img_PROP_4, width=700)
    
    st.write("* Cinquième partie ")
    img_PROP_5 = Image.open("PROP_5.jpg")
    st.image(img_PROP_5, width=700)
    
    st.write("* Sixième partie : visualisez la vidéo s'il vous plaît")
    video_file = open('PROP_6.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    
    st.write("* Septième partie :")
    img_PROP_4 = Image.open("PROP_4.jpg")
    st.image(img_PROP_4, width=700)
    
    st.write("* Huitième partie :")  
    img_PROP_5 = Image.open("PROP_5.jpg")
    st.image(img_PROP_5, width=700)

    st.write(" * ## Helium")
    img_He_1 = Image.open("He_1.jpg")
    st.image(img_He_1, width=700)
    
    video_file = open('He_2.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    st.write("------------------------------------------------ ")
  
    st.write(" * ## CO2")
    img_CO2 = Image.open("CO2.jpg")
    st.image(img_CO2, width=700)
    
    st.write("------------------------------------------------ ")
        
    st.write(" * ## N2")
    img_N2 = Image.open("N2.jpg")
    st.image(img_N2, width=700)
    
    st.write("------------------------------------------------ ")
       
    st.write(" * ## O2")
    img_O2_1 = Image.open("O2_1.jpg")
    st.image(img_O2_1, width=700)
       
    img_O2_3 = Image.open("O2_3.jpg")
    st.image(img_O2_3, width=700)
    
    st.write("------------------------------------------------ ")
        
    st.write(" * ## CCl2F2")
    img_CCL2F2 = Image.open("CCL2F2.jpg")
    st.image(img_CCL2F2, width=700)
    
    st.write("------------------------------------------------ ")
        
    st.write(" * ## UN3501")
    img_CCL2F2 = Image.open("UN3501_2.jpg")
    st.image(img_CCL2F2, width=700)
    
    video_file = open('UN3501.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
            
    st.write(" * ## CCl2F2")
    img_CCL2F2 = Image.open("CCL2F2.jpg")
    st.image(img_CCL2F2, width=700)




  
    



