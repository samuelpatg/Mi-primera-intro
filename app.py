import streamlit as st
from PIL import Image

st.title("Vapoi?")
image = Image.open('vapoi.jpg')
st.image(image, caption='Vapoi')


texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El etxto escrito es', texto)

st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1: 
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuarios")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('Correcto')

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Que modalidad es la principalen tu interfaz", ('visual','auditiva', 'tactil'))
  if modo == "visual":
    st.write('la vista es fundamental para tu interfaz')
  if modo == "auditiva":
        st.write('la audicion es fundamental para tu interfaz')
 if modo == "tactil":
        st.write('El tacto es fundamental para tu interfaz')
