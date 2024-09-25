import streamlit as st
import pandas as pd

st.set_page_config(
    layout="centered",
    page_title="Usando SelectBox, MultiSelect, File Uploader e Slider"
)
st.write("<h1><center>Usando SelectBox, MultiSelect, File Uploader e Slider</center><h1>",unsafe_allow_html=True)
st.subheader("Prof. Luciano Borba")

select = st.selectbox("Selecione uma cor:",("Verde", "Preto", "Roxo", "Branco"))
st.write(f"A cor selecionada foi: {select}")

multi = st.multiselect("Selecione as suas marcas de carros preferidas", ("BMW", "Mercedes", "Porsche", "Toyota"))
st.write(f"As marcas selecionadas foram: ")
for m in multi:
    st.write(m)

df = st.file_uploader("Selecione um arquivo Excel:", type="xlsx")
if df:
    data = pd.read_excel(df)
    st.dataframe(data)

image = st.file_uploader('Selecione uma imagem:', type="png")
if image:
    st.image(image)