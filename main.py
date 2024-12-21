import streamlit as st

hjem_page = st.Page(
    page = "views/hjem.py",
    title = "Hjem",
    default = True,
)

tipsportal = st.Page(
    page ="views/kodeknekker.py",
    title="Tips"
)
#dokumenter = st.Page(
#    page = "views/dokumenter.py",
#    title = "Dokumenter"

#)

#navigasjon

pg = st.navigation(pages=[hjem_page, tipsportal])

#run navi

pg.run()
