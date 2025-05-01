# app.py

import streamlit as st
import folium
from streamlit_folium import st_folium
from MapFetcher import RI_MapFetcher

# Initialize
api_key = 'LhMzXgy2kWSqeCJZwc5XYClmjw9vvkIh'
fetcher = RI_MapFetcher(api_key)

st.title("Rhode Island Traffic Map")

# Select town
town = st.text_input("Enter a Rhode Island town name:", "Providence")

# Get town coordinates
try:
    lat, lng = fetcher.get_town_coords(town)
    st.success(f"Showing map for {town} at ({lat}, {lng})")
except Exception as e:
    st.error(f"Error fetching town coordinates: {e}")
    st.stop()

# Create Folium map
m = folium.Map(location=[lat, lng], zoom_start=12)

# Get traffic incidents (use a bounding box covering all RI)
incidents = fetcher.get_traffic_incidents()
for incident in incidents:
    folium.Marker(
        [incident['lat'], incident['lng']],
        popup=incident['shortDesc'],
        icon=folium.Icon(color='red' if incident['severity'] > 2 else 'orange')
    ).add_to(m)

# Display map in Streamlit
st_folium(m, width=700, height=500)
