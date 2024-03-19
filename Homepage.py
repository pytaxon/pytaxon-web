import streamlit as st

st.title('Pytaxon')

with open('files/pytaxon_gui.rar', 'rb') as arq:
    st.download_button('Baixar Pytaxon GUI', data=arq, file_name='pytaxon_gui.rar')
