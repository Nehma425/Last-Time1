import streamlit as st
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
from datetime import datetime as dt
from numerize.numerize import numerize
from PIL import Image


# Set page configuration
st.set_page_config(page_title='CitiBikes Strategy Dashboard', layout='wide')

# Center-align the title using HTML
st.markdown("""
    <h1 style='text-align: center;'>CitiBikes Strategy Dashboard</h1>
""", unsafe_allow_html=True)

# Add additional markdown content
st.markdown("The dashboard will help with the expansion problems Citibike currently faces.")
st.markdown("Currently, CitiBike faces a challenge wherein customers frequently encounter unavailability of bikes at specific times. This analysis seeks to investigate the underlying causes contributing to this issue and propose potential solutions.")

# Define page selector
page = st.sidebar.selectbox("Aspect Selector", ["Intro page", "Most popular stations", "Bike Trips and Temperature", "Aggregated Bike Trips", "Recommendations"])

# Load data

df3 = pd.read_csv('top20.csv', index_col=0)
df = pd.read_csv('dual_chart.csv', index_col=0)


# Intro page
if page == "Intro page":
    st.markdown("#### This dashboard aims at providing helpful insights on the expansion problems CitiBikes currently faces.")
    st.markdown("Right now, Citibikes runs into a situation where customers complain about bikes not being available at certain times. This analysis will look at the potential reasons behind this. The dashboard is separated into 4 sections:")
    st.markdown("- Most popular stations")
    st.markdown("- Bike Trips and Temperature")
    st.markdown("- Aggregated Bike Trips")
    st.markdown("- Recommendations")
    st.markdown("The dropdown menu on the left 'Aspect Selector' will take you to the different aspects of the analysis our team looked at.")

    myImage = Image.open("CitiBike.png")  # Source: https://images.ctfassets.net/p6ae3zqfb1e3/647OU4Rla0GlF2rGwtaBWC/aea6f7c8f543ab2e1ec8608af2a61db9/Citi_Bike_ExploreNYC_Hero_3x.jpg?w=2500&q=60&fm=webp
    st.image(myImage)
  ### Create the dual axis line chart page ###
    
elif page == 'Bike Trips and Temperature':

    fig_2 = make_subplots(specs = [[{"secondary_y": True}]])

    fig_2.add_trace(
    go.Scatter(x = df['date'], y = df['trip_count'], name = 'Bike Trips', marker={'color': df['trip_count'],'color': 'blue'}),
    secondary_y = False
    )

    fig_2.add_trace(
    go.Scatter(x=df['date'], y = df['avgTemp'], name = 'Daily temperature', marker={'color': df['avgTemp'],'color': 'red'}),
    secondary_y=True
    )

    fig_2.update_layout(
    title = 'Bike Trips and Temperatures in 2022',
    height = 400
    )

    st.plotly_chart(fig_2, use_container_width=True)
    st.markdown("The connection between temperature fluctuations and daily bike trip frequency is evident. As temperatures decrease, bike usage also declines. This observation suggests that the scarcity issue may primarily occur during warmer months, roughly from May to October.")


# Most popular stations chart
elif page == 'Most popular stations':
    fig = go.Figure(go.Bar(x=df3['start_station_name'], y=df3['trip_count'], marker={'color': df3['trip_count'], 'colorscale': 'Blues'}))
    fig.update_layout(
        title='Top 20 Most Popular Bike Stations in New York',
        xaxis_title='Start stations',
        yaxis_title='Sum of trips',
        width=900, height=600
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("The bar chart clearly shows that some start stations are way more popular than others. W21 St &6 Ave,West St & Chambers St, Broadway & W 58 St are the top three. There's a big difference between the highest and lowest bars, indicating strong preferences for these leading stations.")
    
elif page == 'Aggregated Bike Trips': 

    ### Display the KeplerGl map ###

    st.write("Interactive map showing aggregated Citibike trips over New York City")

    # Load and display the KeplerGl map HTML file
    st.components.v1.html(open('keplergl_map.html', 'r').read(), height=700)

   

 #Recommendations   

elif page == 'Recommendations':
    # Display the image
    myImage = Image.open("newplot.png")  
    st.image(myImage)

    # Markdown text explaining the image
    st.markdown("""
    The chart indicates a significant increase in bike usage during the summer season, with over 14 million rides recorded. 
    Conversely, the spring season shows relatively lower bike rental counts compared to other seasons. 
    Additionally, the data suggests that bike usage during fall and winter is more comparable, with both seasons having approximately 8-5 million rides. 
    The average temperature throughout the year seems moderate, contributing to consistent bike usage across different seasons.
    """)
    st.markdown("""
    **Seasonal Inventory Management**: Adjust the number of bikes available at rental stations based on seasonal demand patterns. Allocate more bikes to stations in high-demand seasons like summer and fall, and reduce inventory during lower-demand seasons like winter.

    **Weather-Based Marketing**: Utilize weather forecasts to tailor marketing campaigns and promotions. For example, offer discounts or incentives on days with favorable weather conditions to encourage more people to rent bikes.

    **Station Optimization**: Analyze the distribution of bike rental stations and consider adding or relocating stations in areas with high demand or under-served areas. This can help improve accessibility and convenience for users, especially during peak seasons.

    **Maintenance Planning**: Plan bike maintenance schedules based on seasonal usage patterns. Increase maintenance activities during high-demand seasons to ensure bikes are in optimal condition and reduce downtime due to repairs.

    **Customer Engagement**: Engage with customers through surveys or feedback mechanisms to understand their preferences and improve the overall biking experience. Gather insights on factors like preferred riding routes, station accessibility, and bike availability.

    **Partnerships and Events**: Collaborate with local businesses, event organizers, or tourism agencies to promote bike rentals as a sustainable and convenient transportation option. Sponsor community events or organize biking tours to attract more users and raise awareness about bike rental services.

    **Technology Integration**: Implement advanced analytics and predictive modeling techniques to forecast future demand and optimize inventory levels in real-time. Use mobile apps or online platforms to provide users with real-time information on bike availability, station locations, and rental options.

    These recommendations aim to enhance the overall bike rental experience, attract more users, and maximize the utilization of bike rental services throughout the year.
    """)



    


