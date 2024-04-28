import streamlit as st
import pandas as pd
col1,col2,col3 = st.columns([1,2,1])

st.title("Welcom to yash website!")
st.header("This website is create for student help for semester exam !")

uploaded_Photo = col1.file_uploader("Upload a Photo")
camera_photo = col1.camera_input("Take a photo")

with st.expander("Click to read more"):
    st.write("Hello ,here are more details on this topic that you are intrested in.")

    if uploaded_Photo is None:
        st.image(camera_photo)
    else:
        st.image(uploaded_Photo) 
        
       

        