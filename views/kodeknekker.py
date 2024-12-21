import streamlit as st
import time

# Initialiser session state
if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False
if 'input_locked' not in st.session_state:
    st.session_state.input_locked = False

def countdown_timer():
    st.session_state.timer_running = True
    total_seconds = 5 * 60
    
    timer_placeholder = st.empty()
    
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer_placeholder.header(f'{mins:02d}:{secs:02d}')
        time.sleep(1)
        total_seconds -= 1
    
    timer_placeholder.header("Tiden er ute!")
    st.session_state.timer_running = False
    st.session_state.input_locked = False
    st.rerun()



# Last inn bilde
try:
    st.image("images/images-2.png")
except:
    st.error("Kunne ikke laste inn bildet. Sjekk at filstien er korrekt.")


kodeliste = [
    "MOTHERLODE",
    "IDDQD",
    "SELMA",
    "BONUS",
    "IMACHEAT",
    "REDPILL",
    "BONUSPOENG",
    "HOROSKOP",
    "CHEZBURGER",
    "HELIUM",
    "KONTORARBEID",
    "MILKSHAKE",
    "MAJONES",
    "JUKS",
    "GOD JUL",
    "30",
    "FREDERIK",
    "KOKETOPP",
    "PLATETOPP",
    "BENDIK",
    "ERNA SOLBERG",
    "MARIUS BORG"
]

riktig_svar = [ 
    "RØD", 
    "PR52122", 
    "LARVIKSTASJON"
]
# Håndter input basert på timer og låsestatus
if st.session_state.input_locked:
    st.text_input("Her kan du sende inn observasjoner og tips til politiet:", 
                 value="Låst - vent til timeren er ferdig", 
                 disabled=True)
    countdown_timer()
else:
    user_input = st.text_input("Skriv inn riktig kode for å låse opp flere sider:", type = "default").upper().replace(" ", "")

    if user_input:
        if user_input == "6570406,194967":
            st.success("Klikk på lenken under for å gå videre:")
            st.markdown('<a href="https://www.google.com/maps/place/Rødborge+10,+3711+Skien/@59.1628044,9.6620454,3a,75y,336.68h,72.18t/data=!3m7!1e1!3m5!1sqpfVUYs62pEV99zC7NaHkw!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D17.816497170145084%26panoid%3DqpfVUYs62pEV99zC7NaHkw%26yaw%3D336.68460825835535!7i16384!8i8192!4m15!1m8!3m7!1s0x464720865a5ea89d:0xef0812ac99525e89!2sRødborge+10,+3711+Skien!3b1!8m2!3d59.1629065!4d9.6617568!16s%2Fg%2F11c10zkt_1!3m5!1s0x464720865a5ea89d:0xef0812ac99525e89!8m2!3d59.1629065!4d9.6617568!16s%2Fg%2F11c10zkt_1?entry=ttu&g_ep=EgoyMDI0MTIxMS4wIKXMDSoASAFQAw%3D%3D" target="_blank">Klikk her for å gå videre</a>', unsafe_allow_html=True)
       
        elif user_input in riktig_svar:
            st.success("Takk for tipset, vi kommer tilbake til deg når vi vet noe mer!")
            
        elif user_input == "START":
            st.success("Riktig! Klikk på lenken under for å gå videre:")
            st.markdown('<a href="https://drive.google.com/drive/folders/1zkd_3BxmZdQ7mzTjBF8DBKKslufvuC3H" target="_blank">Klikk her for å gå videre</a>', unsafe_allow_html=True)
            
        elif user_input == "UTPÅTUR,ALDRISUR":
            st.success("Klikk på lenken under for å gå videre:")
            st.markdown('<a href="https://drive.google.com/file/d/1h46W62ljwCe24pmieNg9jL0GMTrVaFn1/view?usp=sharing" target="_blank">Klikk her for å gå videre</a>', unsafe_allow_html=True)

        elif user_input == "CHESBURGER":
            st.success("Klikk på lenken under for å gå videre:")
            st.markdown('<a href="https://drive.google.com/file/d/1BVTQ7Ys6pPkfPP1t069En75AxCyiRxEx/view?usp=sharing" target="_blank">Klikk her for å gå videre</a>', unsafe_allow_html=True)
        
        elif user_input == "OSEBRO,OVERVURDERT?":
            st.success("Klikk på lenken under for å gå videre:")
            st.markdown('<a href="https://drive.google.com/file/d/1CUsYBq_6SZRnOjP-JJnLLnRspJnH4UM8/view?usp=sharing" target="_blank">Klikk her for å gå videre</a>', unsafe_allow_html=True)
          
        elif user_input in kodeliste:
            st.success("Riktig kode, gå til gamemaster og oppgi hvilken kode du har skrevet inn")
            

        #elif user_input == "RØD":
         #   st.success("Riktig! Klikk på lenken under for å gå videre:")
          #  st.markdown('<a href="https://docs.google.com/document/d/1sOMwI4pvwil9bOALEIi3MwnjwXx4pwZ6rNz7r84eYYE/edit?usp=sharing" target="_blank">Klikk her for å gå videre</a>', unsafe_allow_html=True)



        else:
            st.error("Feil kode!")
            st.session_state.input_locked = True
            st.rerun()

if not st.session_state.timer_running:
    st.sidebar.info("Her kan du sende inn observasjoner og tips til politiet:")
