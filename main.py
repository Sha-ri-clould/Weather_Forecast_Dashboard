import streamlit as st

st.title("Weather Forecast Dashboard🌦️")
st.subheader("Explore the world's weather, one city at a time")
st.write("A full-globe weather visualizer that lets you pick any country or city and view real-time temperature, Displays current weather conditions, 5-day forecast.")

city = st.text_input("Enter your city name")
days = st.slider("Select Forecast days",min_value=1,max_value=5,help="Pick Number of days")
view = st.selectbox("Select data to view", options=["Temperature","Sky"])

if days == 1:
    day = "day"
else:
    day = "days"

st.subheader(f"{view} for next {days} {day} in {city}")

st.write("Developed by \n"
"[Sha-ri-cloud]")
