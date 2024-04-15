import streamlit as st
import time
import json
import requests
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title = ' SkyWatchHub Drum',
    page_icon = '✈️',
    layout = 'wide'
)
drum_timing = st.session_state['drum_timing']
difficulty_level = st.session_state['challenging_level']
fun_fact = st.session_state['fun_fact']
st.subheader(f"Level of difficulty: {difficulty_level}")
st.subheader(f"Hit the drums within {drum_timing} seconds and try to light up all the lights surrounding you")
st.subheader(f"Fun Fact:{fun_fact}")
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://lottie.host/f93b2116-89fb-4221-8e40-8b024aa5c32c/qKM9FIJwnO.json")
placeholder = st.empty()
# placeholder2 = st.columns([0.5,1, 0.5])
placeholder2 = st.columns(3)
Sensor1 = placeholder2[0].empty()
Sensor2 = placeholder2[1]
Sensor3 = placeholder2[2].empty()
with Sensor2.container():
    st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
 # canvas
    height=None,
    width=None,
    key=None,
)

mehmeh = "💡"
for secondsx in range(drum_timing): 
    with placeholder.container():
        st.header(f"Countdown Timer: {secondsx+1}")

    with Sensor1.container():
        
        st.header(mehmeh)         
    with Sensor3.container():
        st.header(mehmeh) 

    mehmeh += "💡"
    time.sleep(1)

with Sensor1.container():
    st.title("Moving back Info Page")
time.sleep(2)
st.switch_page("frontend_taikodrum3.py")

   

# for x in range(19):
#     st.title(x+1)


# st_lottie(
#     lottie_hello,
#     speed=1,
#     reverse=False,
#     loop=True,
#     quality="low", # medium ; high
#  # canvas
#     height=None,
#     width=None,
#     key=None,
# )