import streamlit as st
from PIL import Image

#st.title("property-improver")

st.markdown("<h1 style='text-align: center; color: white;'>Mejora tu propiedad con Property Improve</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: white;'>Carga tu imagen</h2>", unsafe_allow_html=True)

#st.markdown("App mejora de propiedades")
#st.button('Click')
image = Image.open('img_1.jpg')

st.image(image, caption='Sunrise by the mountains')

datos = st.file_uploader("Carga aqui la fotografia")
