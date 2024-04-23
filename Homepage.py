import streamlit as st

with open('files/title.txt', 'r', encoding='utf-8') as file:
    title = file.read()
st.markdown(f'<h1 style="text-align: center;">{title}</h1>', unsafe_allow_html=True)

with open('files/resumen.txt', 'r', encoding='utf-8') as file:
    resumen = file.read()
st.header('Resumo da Pesquisa:')
st.markdown(f'<p style="text-align: justify">{resumen}</p>', unsafe_allow_html=True)

with open('files/references.txt', 'r', encoding='utf-8') as file:
    references = file.read()
st.header('Referências')
st.markdown(references, unsafe_allow_html=True)
