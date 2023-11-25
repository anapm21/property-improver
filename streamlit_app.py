import streamlit as st
from PIL import Image

#st.title("property-improver")

st.markdown("<h1 style='text-align: center; color: white;'>Mejora tu propiedad con </h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>Carga aqui tu imagen</h2>", unsafe_allow_html=True)

imagefelecha = Image.open('felecha.png')
st.image(imagefelecha, caption='',aling: center)

#st.markdown("App mejora de propiedades")
#st.button('Click')

#image = Image.open('img_1.jpg')
#st.image(image, caption='Sunrise by the mountains')

datos = st.file_uploader("")

st.text_input('Tell me your name')
