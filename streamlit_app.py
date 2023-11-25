#import streamlit as st
#from PIL import Image

#st.title("property-improver")

#st.markdown("<h1 style='text-align: center; color: white;'>Mejora tu propiedad con Property Improver </h1>", unsafe_allow_html=True)
#st.markdown("<h2 style='text-align: center; color: white;'>Carga aqui tu imagen</h2>", unsafe_allow_html=True)

#imagefelecha = Image.open('felecha.png')
#st.image(imagefelecha, caption='')

#st.markdown("App mejora de propiedades")
#st.button('Click')

#image = Image.open('img_1.jpg')
#st.image(image, caption='Sunrise by the mountains')

#datos = st.file_uploader("")

#user_name = st.text_input('Tell me your name')


import streamlit as st
from random import choice

st.title("Magic 8 Ball")

user_name = st.text_input('Tell me your name...')
button_press = st.button("Try your luck")

phrases = ["As I see it, yes.",
           "Ask again later.",
           "Better not tell you now.",
           "Cannot predict now.",
           "Concentrate and ask again.",
           "Don’t count on it.",
           "It is certain.",
           "It is decidedly so.",
           "Most likely.",
           "My reply is no.",
           "My sources say no.",
           "Outlook not so good.",
           "Outlook good.",
           "Reply hazy, try again.",
           "Signs point to yes.",
           "Very doubtful.",
           "Without a doubt.",
           "Yes.",
           "Yes – definitely.",
           "You may rely on it"]

if button_press:
    st.header(f"Let's see, {user_name}...")
    st.title(choice(phrases))
