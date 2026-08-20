import streamlit as st
from PIL import Image

st.title("Vapoi?")
image = Image.open('vapoi.jpg')
st.image(image, caption='Vapoi')


texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El etxto escrito es', texto)
