import streamlit as st
from PIL import Image

st.title("property-improver")
# markdown("App mejora de propiedades")
st.button('Click')
image = Image.open('img_1.jpg')

st.image(image, caption='Sunrise by the mountains')

datos = file_uploader("Carga aqui la fotografia")
