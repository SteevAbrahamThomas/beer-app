import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Streamlit app UI
st.title("🍺 Alcohol Consumption Predictor")
st.image("https://images.unsplash.com/photo-1516455590571-18256e5bb9ff", use_container_width=True)
st.write("Welcome! Enter the servings of beer, spirits, and wine to predict the **total litres of pure alcohol** consumed.")

# User inputs
beer = st.number_input("Beer Servings (per person per year)", min_value=0, max_value=500, value=50)
spirit = st.number_input("Spirit Servings (per person per year)", min_value=0, max_value=500, value=50)
wine = st.number_input("Wine Servings (per person per year)", min_value=0, max_value=500, value=20)

# Predict button
if st.button("Predict Total Alcohol Consumption"):
    input_data = pd.DataFrame([[beer, spirit, wine]], columns=["beer_servings", "spirit_servings", "wine_servings"])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Total Litres of Pure Alcohol: **{prediction:.2f} L**")


