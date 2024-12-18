import streamlit as st

hjem_page = st.Page(
    page = "views/hjem.py",
    title = "Hjem",
    default = True,
)

kodeknekker = st.Page(
    page ="views/kodeknekker.py",
    title="Kodeknekker"
)
dokumenter = st.Page(
    page = "views/dokumenter.py",
    title = "Dokumenter"

)

#navigasjon

pg = st.navigation(pages=[hjem_page, dokumenter, kodeknekker])

#run navi

pg.run()