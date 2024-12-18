import streamlit as st


st.image("/Users/bendikberg-jensen/Documents/Skole/øvinger/SelmaSpill/images-2.png", width = 300)


if st.button("Den mystiske forsvinningen i Larvik"):
    st.switch_page("views/dokumenter.py")

st.image("/Users/bendikberg-jensen/Documents/Skole/øvinger/SelmaSpill/mannibutikk.jpg", width = 500)
st.write("")

st.title(" ")
if st.button("Det forsvunnede maleri"):
    st.switch_page("views/dokumenter.py")

st.image("/Users/bendikberg-jensen/Documents/Skole/øvinger/SelmaSpill/Kunstbilde.jpg", width = 500)

