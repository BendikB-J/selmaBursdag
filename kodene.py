import streamlit as st

def koder(user_input):
    if user_input == "hem":  
        st.write("Riktig, link vises i navigeringsmenyen")
        page = st.sidebar.radio("Gratulere, du kan nå navigere til:", ("https://www.google.com/webhp?hl=no&sa=X&ved=0ahUKEwin-I3q2quJAxX7JhAIHRSfFssQPAgJ"))
    if user_input == "3":
        st.write("Riktig, link vises i navigeringsmenyen")
        page = st.sidebar.radio("Gratulere, du kan nå navigere til:", ("https://www.google.com/webhp?hl=no&sa=X&ved=0ahUKEwin-I3q2quJAxX7JhAIHRSfFssQPAgJ"))

    else:
        st.sidebar.write("Skriv inn riktig kode for å låse opp flere sider.")

