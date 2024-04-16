import streamlit as st
import time
import json
import requests
from streamlit_lottie import st_lottie
import matplotlib.pyplot as plt

st.set_page_config(
    page_title = ' SkyWatchHub Drum',
    page_icon = '✈️',
    layout = 'wide'
)
drum_timing = st.session_state['drum_timing']
difficulty_level = st.session_state['challenging_level']
fun_fact = st.session_state['fun_fact']
fuel_level = st.session_state['fuel_level']
mehmeh = st.columns([9.1,0.9])
with mehmeh[0]:
    st.subheader(f"Level of difficulty: {difficulty_level}")
    st.subheader(f"Currently the plane fuel gauge is 0%, hit the drums within {drum_timing} seconds and to power up the engine to spin the turbine and light up the lights surrounding you")
    st.subheader(f"Fun Fact:{fun_fact}")
with mehmeh[1]:
        categories = ['Energy Saved']
        values1 = [0]
        values2 = [100]

        fig, ax = plt.subplots(figsize=(1, 5))
        ax.bar(categories, values1, label='Group 1', color ="Green")
        ax.bar(categories, values2, bottom=values1, label='Group 2', color ="#D3D3D3")

        # Customizing
        ax.set_title('Fuel Energy Bar')
        # ax.set_xlabel('Fuel Energy Bar')
        ax.set_ylabel('Percentage %')
        # ax.title('Vertical Stack Graph')
        # plt.legend()

        # Displaying the graph



        st.pyplot(fig, use_container_width  = True)
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://lottie.host/f93b2116-89fb-4221-8e40-8b024aa5c32c/qKM9FIJwnO.json")
placeholder = st.empty()
# placeholder2 = st.columns([0.5,1, 0.5])
placeholder2 = st.columns([3,3,0.9,2.1])
Sensor1 = placeholder2[0].empty()
Sensor2 = placeholder2[1]
Sensor3 = placeholder2[2].empty()
Sensor4 = placeholder2[3]
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
        st.header(f"Countdown Timer: {secondsx+1} / {drum_timing}")

    with Sensor1.container():
        
        st.header(mehmeh)         
    # with Sensor3.container():
    #     st.header(mehmeh) 

    mehmeh += "💡"
    time.sleep(1)

with Sensor1.container():
    st.title("Moving back Info Page")

with Sensor3.container():
    categories = ['Energy Saved']
    values1 = [fuel_level[0]]
    values2 = [fuel_level[1]]
    fig, ax = plt.subplots(figsize=(1, 5))
    ax.bar(categories, values1, label='Group 1', color ="Green")
    ax.bar(categories, values2, bottom=values1, label='Group 2', color ="#D3D3D3")

    # Customizing
    ax.set_title('Fuel Energy Bar')
    # ax.set_xlabel('Fuel Energy Bar')
    ax.set_ylabel('Percentage %')
    # ax.title('Vertical Stack Graph')
    # plt.legend()

    # Displaying the graph



    st.pyplot(fig, use_container_width  = True)

with Sensor4.container():
    st.title(f"You manage to charge up {fuel_level[0]}% of energy")
time.sleep(10)
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