import streamlit as st
from PIL import Image
casa1=0
casa2=0
#st.title("property-improver")

st.markdown("<h1 style='text-align: center; color: white;'>Mejora tu propiedad con Property Improver </h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>Carga aqui tu imagen</h2>", unsafe_allow_html=True)

col1, col2 = st.columns (2)

with col1:
 st.image('img_1.jpg')
 casa1 = st.button ("Casa 1")

with col2:
 st.image('img_2.jpg')
 casa2 = st.button ("Casa 2")

if 'casa1':
 casa1=1

if 'casa2':
 casa2=1

print('casa1','casa2')
 

#imagefelecha = Image.open('felecha.png')
#st.image(imagefelecha, caption='')

#st.markdown("App mejora de propiedades")
#st.button('Click')

#image = Image.open('img_1.jpg')
#st.image(image, caption='Sunrise by the mountains')

#uploaded_files = st.file_uploader("")
#uploaded_files = st.file_uploader("Elige tus archivos", accept_multiple_files=True)

#selected = st.selectbox("Que carpeta quieres analizar?", options=[1,2,3,4])

#if uploaded_files:
 #   st.markdown("<h6 style='text-align: center; color: white;'>Imagen cargada correctamente</h2>", unsafe_allow_html=True)

#clear = st.button("Eliminar imagenes subidas")

#for uploaded_file in uploaded_files:
  #  st.image(uploaded_file,width=300,caption=uploaded_file.name)

#user_name = st.text_input('Tell me your name')

#if clear:
 #   uploaded_file=0





