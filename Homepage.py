import streamlit as st

st.title('Pytaxon')

with open('files/pytaxon_gui.rar', 'rb') as arq:
    st.download_button('Baixar Pytaxon-GUI.rar', data=arq, file_name='pytaxon_gui.rar')

with open('files/pytaxon_gui.zip', 'rb') as arq:
    st.download_button('Baixar Pytaxon-GUI.zip', data=arq, file_name='pytaxon_gui.zip')
