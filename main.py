import streamlit as st
import plotly.express as px
from backend import get_data

# ADD TITLE, SUBHEADER, INPUT_TEXT, SLIDER AND SELECTBOX

st.set_page_config(page_title="Weather Forecast Dashboard",page_icon="🌦️",layout="wide",
                   menu_items={"About":"This is a Weather Forecast Dahboard helps in displaying temperature and sky conditions upto 5 days!"})
st.title("Welcome to Weather Forecast Dashboard🌦️")
st.subheader("Explore the world's weather, one city at a time")
st.write("A full-globe weather visualizer that lets you pick any country or city and view real-time temperature, Displays current weather conditions, 5-day forecast.")

city = st.text_input("Enter your city name")
days = st.slider("Select Forecast days",min_value=1,max_value=5,help="Pick Number of days")
view = st.selectbox("Select data to view", options=["Temperature","Sky"])
submit = st.button("Submit")

# AFTER USER INPUT
if submit:
    if city:
        try:
            if days == 1:
                day = "day"
            else:
                day = "days"
            st.subheader(f"{view} for next {days} {day} in {city}")

            # GET TEMPERATURE/SKY DATA
            filtered_data= get_data(city, days)

            # OUTPUT FOR TEMPERATURE
            if view == "Temperature":
                temperature = [data["main"]["temp"]/10 for data in filtered_data]
                dates = [data["dt_txt"] for data in filtered_data]
                figure = px.line(x=dates, y=temperature,labels={"x":"Date","y":"Temperature(C)"},line_shape="linear")
                st.plotly_chart(figure)

            # OUTPUT FOR SKY CONDITION
            if view == "Sky":
                description = [data["weather"][0]["description"].title() for data in filtered_data]
                dates = [data["dt_txt"] for data in filtered_data]
                captions = [f"{dest}\n\n{date}" for dest,date in zip(description, dates)]
                filtered_data = [data["weather"][0]["main"] for data in filtered_data]
                image = {"Clear": "images/clear.png",
                         "Clouds": "images/cloud.png",
                         "Rain": "images/rain.png",
                         "Snow":"images/snow.png"}
                image_path = [image[filter_data] for filter_data in filtered_data]
                st.image(image=image_path, caption=captions, width=125,)

        except KeyError:
            st.error("Enter a valid city name")


    else:
        st.error("Please enter a city name")


st.write(f"Developed by \n"
f"[Sha-ri-cloud]")
