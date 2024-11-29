import numpy as np
import pandas as pd
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the pre-trained model
model = pickle.load(open('water.pkl', 'rb'))

# Title of the app
st.title("Water Quality Prediction")

# Create columns for input
col1, col2 = st.columns(2)

with col1:
    ph = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.01)
    hardness = st.number_input("Hardness", min_value=0.0)
    solids = st.number_input("Solids", min_value=0.0)
    chloramines = st.number_input("Chloramines", min_value=0.0)
    sulfate = st.number_input("Sulfate", min_value=0.0)

with col2:
    conductivity = st.number_input("Conductivity", min_value=0.0)
    organic_carbon = st.number_input("Organic Carbon", min_value=0.0)
    trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0)
    turbidity = st.number_input("Turbidity", min_value=0.0)

# Predict button
if st.button("Predict Water Quality"):
    # Create input array for prediction
    input_data = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity,
                            organic_carbon, trihalomethanes, turbidity]])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display prediction
    if prediction == 1:
        st.success("The probability is stating that the water is clean for drinking.")

    else:
        st.error("The probability is stating that the  water is NOT clean for drinking.")
        
        
        st.write("ph must be in 6.5 to 8.5..")
        st.write("hardness must be in 0 to 200..")
        st.write("solids must be in 20000 to 100000..")
        st.write("Chloramines must be in 0 to 4..")
        st.write("Sulfate must be in 0 to 250..")
        st.write("Conductivity must be in 0 to 1500..")
        st.write("Organic_carbon must be in 0 to 2..")
        st.write("Trihalomethanes must be in 0 to 80..")
        st.write("Turbidity must be in 0 to 1")

