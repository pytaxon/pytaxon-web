import streamlit as st

st.title('Pytaxon')
st.header('v0.1.1')
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown('Windows:')
    st.markdown('[Pytaxon-Win.rar](https://drive.google.com/file/d/1eTyPHLXGj11VH8MC0MMY8L8UH3aOcT16/view?usp=drive_link)')
    st.markdown('[Pytaxon-Win.zip](https://drive.google.com/file/d/1iBMTVAKbo_06jj6vAG30D01a-HThPzgc/view?usp=drive_link)')

with col2:
    st.markdown('Linux:')
    st.markdown('[Pytaxon-Lin.rar](https://drive.google.com/file/d/1U1CxFBCMslfHMCgo52uZPVlwAShceqjh/view?usp=drive_link)')
    st.markdown('[Pytaxon-Lin.zip](https://drive.google.com/file/d/1m-Jh1CIADKo0OAKUkFiMzj3cehlyShz5/view?usp=drive_link)')
