import streamlit as st
import base64
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")


st.title("📝 Resume")

st.write("[Click here!](https://drive.google.com/file/d/14Nv3thLxYOmHb4VbqkyOmhH4xPosD0zV/view?usp=drive_link)")


  
