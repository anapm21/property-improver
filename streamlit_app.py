import streamlit as st
from PIL import Image

st.title("property-improver")
st.button('Click')
image = Image.open('img_1.jpg')

st.image(image, caption='Sunrise by the mountains')
