import streamlit as st
import pandas as pd
from PIL import Image
import uuid
import os



st.set_page_config(
    page_title = ' SkyWatchHub',
    page_icon = '✈️',
    layout = 'wide'
)


if 'drum_timing' not in st.session_state:
    st.session_state['drum_timing'] = 1 #or whatever default


if 'challenging_level' not in st.session_state:
    st.session_state['challenging_level'] = "Non-Game Mode"

if 'fun_fact' not in st.session_state:
    st.session_state['fun_fact'] = "Go back home page and press the button properly"

if 'fuel_level' not in st.session_state:
    st.session_state['fuel_level'] = [0,100]
plane_data = pd.read_csv("plane_data.csv")
plane_data_departure = pd.read_csv("plane_data_departure.csv")

plane_data["arrival_scheduled"] = pd.to_datetime(plane_data["arrival_scheduled"])
plane_data_departure["departure_estimated"] = pd.to_datetime(plane_data_departure["departure_estimated"])
plane_data["timeline"] = plane_data["arrival_scheduled"].dt.time
plane_data_departure['timeline'] = plane_data_departure["departure_estimated"].dt.time
plane_data["direction"] = "Arriving at Changi"
plane_data_departure["direction"] = "Departing from Changi"
data1 = plane_data[["airline_name","timeline","direction"]]
data2 = plane_data_departure[["airline_name","timeline","direction"]]
df = pd.concat([data1,data2])
df = df.sort_values(by=['timeline'])


colnew1,dudcol,colnew2 = st.columns([7.75,1,1.25])
with colnew1:
    st.title("🛬 Welcome to SkyWatchHub")
    st.title("Click below for more information of common planes that pass by this area")

with colnew2:
    st.subheader("Follow us on Instagram!!!")
    st.image("insta.jpg", use_column_width = "auto", width= 0.1)

placeholder = st.empty()
placeholder2 = st.empty()

# col1,col2,col3, col4 = st.columns(4)
col1,col2mehmeh, col2, col1mehmehmeh,col4 = st.columns([2.5,0.5,2.5,0.5,2.5])

with col1:
    st.image("Boeing-737-Max-9-Alaska.jpg", use_column_width ="auto")
    with st.expander("Boeing 737 MAX"):
        st.write("""The Boeing 737 MAX experienced two tragic crashes, Lion Air Flight 610 in late 2018 and 
                 Ethiopian Airlines Flight 302 in early 2019, resulting in the loss of 346 lives.  
                 This was due to issues with its Maneuvering Characteristics Augmentation System (MCAS) system and pilot training. 
                 It was grounded globally from March 2019 to November 2020, resulting in significant financial losses for Boeing. 
                 Despite controversies, the FAA cleared the 737 MAX for return to service in November 2020, after mandated changes.""")
        st.write("Used by: Singapore Airlines")
        if st.button('🎮 Play Skywatchhub Drum - Easy Level 🎮'):
            st.session_state['drum_timing'] = 30
            st.session_state['challenging_level'] = "Easy Level"
            st.session_state["fun_fact"] = " Did you know, Boeing 737 MAX has a 241-278 km/h takeoff speed, which is the 1st for speed out of the 3 planes. It consume approximately 100-200 liters of fuel"
            st.session_state['fuel_level'] = [75,25]
            st.switch_page("pages/drum.py")


# with col2:
#     st.image("A320neo.jpg", use_column_width ="auto")
#     with st.expander("Airbus A320neo"):
#         st.write("""Did you know, The neo in A320neo stands for new engine option. It features new, more fuel-efficient engines,
#                  which results in lower emissions of greenhouse gases and pollutants. """)
#         st.write("""The A320neo had a 60% market share against the competing Boeing 737 MAX.[4] As of February 2024, 
#                  a total of 10,354 A320neo family aircraft had been ordered by more than 130 customers, 
#                  of which 3,228 aircraft had been delivered. The global A320neo fleet had completed more than 
#                  5.51 million flights over 11 million block hours with one hull loss being an airport-safety related accident.""")
#         st.write("With its improved fuel efficiency and range capabilities, the A320neo has enabled airlines to open new routes and operate longer flights more economically.")
#         st.write("Used by: AirAsia, Scoot")
#         if st.button('Drum Game: Mid Level'):
            # st.session_state['drum_timing'] = 10
            # st.session_state['challenging_level'] = "Medium Level"
#             st.session_state["fun_fact"] = "Did you know, Airbus A320neo has a 241-278 km/h takeoff speed, which is the 2nd fastest plane out of the 3 planes."
#             st.switch_page("pages/drum.py")



with col4:
    st.image("Boeing_787_Dreamliner.jpg", use_column_width ="auto")
    with st.expander("Boeing 787 Dreamliner"):
        st.write("""The Boeing 787 Dreamliner is the first commercial airliner to utilize a significant amount of composite materials 
                 in its construction. Approximately 50% of the primary structure, including the fuselage and wings, 
                 is made of composite materials such as carbon fiber-reinforced polymer. 
                 This results in a lighter, stronger, and more fuel-efficient aircraft.""")
        st.write("The Boeing 787 Dreamliner can fly non-stop for distances ranging from 13,500 to 17,600 km")
        st.write("Used by: Scoot, Jetstar, Singapore Airlines(SIA), All Nippon Airways (ANA),Japan Airlines (JAL), Qatar Airways, Etihad Airways, British Airways, United Airlines")
        if st.button('🎮 Play Skywatchhub Drum - Hard Level 🎮'):
            st.session_state['drum_timing'] = 10
            st.session_state['challenging_level'] = "Hard Level"
            st.session_state["fun_fact"] = " Did you know, Boeing 787 Dreamliner has a 278-315 km/h takeoff speed, which is the 3rd fastest plane out of the 3 planes. It consume approximately 200-300 liters of fuel to take off"
            st.session_state['fuel_level'] = [25,75]
            st.switch_page("pages/drum.py")
with col2:
    st.image("Airbus_A350.jpg", use_column_width ="auto")
    with st.expander("Airbus A350"):        
        st.write("""The Airbus A350 is constructed using advanced composite materials, including carbon-fiber reinforced polymer (CFRP), 
                 making it one of the most modern and lightweight commercial aircraft in its class. """)
        st.write("""The A350 features a quiet cabin environment, 
        with reduced noise levels both inside the aircraft and in surrounding communities during takeoff and landing. 
        Advanced soundproofing materials and engineering techniques contribute to a more comfortable and peaceful passenger experience.""")
        st.write("Used by: Singapore Airlines (SIA), Cathay Pacific Airways, Qatar Airways, Finnair, Thai Airways International, Vietnam Airlines, China Airlines")
        if st.button('🎮 Play Skywatchhub Drum - Medium Level 🎮'):
            st.session_state['drum_timing'] = 20
            st.session_state['challenging_level'] = "Medium Level"
            st.session_state["fun_fact"] = " Did you know, Airbus A350 has a 259-296 km/h takeoff speed, which is the 2nd fastest plane out of the 3 planes. It consume approximately 200-300 liters of fuel"
            st.session_state['fuel_level'] = [50,50]
            st.switch_page("pages/drum.py")