import streamlit as st
from PIL import Image

#st.title("property-improver")

st.markdown("<h1 style='text-align: center; color: white;'>Mejora tu propiedad con Property Improver </h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>Carga aqui tu imagen</h2>", unsafe_allow_html=True)

#imagefelecha = Image.open('felecha.png')
#st.image(imagefelecha, caption='')

#st.markdown("App mejora de propiedades")
#st.button('Click')

#image = Image.open('img_1.jpg')
#st.image(image, caption='Sunrise by the mountains')

datos = st.file_uploader("")

#user_name = st.text_input('Tell me your name')



if datos:
    st.markdown("<h6 style='text-align: center; color: white;'>Imagen cargada correctamente</h2>", unsafe_allow_html=True)

