import streamlit as st

st.title("Saksdetaljer")


st.title("Larvikforsvinningen")
with open("/Users/bendikberg-jensen/Documents/Skole/øvinger/SelmaSpill/LarvikSak.txt") as larvikfil:
    larvik_sak_tekst = larvikfil.read()

st.write(larvik_sak_tekst)


st.title("Kunstforsvinningen")

with open("/Users/bendikberg-jensen/Documents/Skole/øvinger/SelmaSpill/Kunstforsvinning.txt") as kunsttekst:
    kunst = kunsttekst.read()

st.write(kunst)

