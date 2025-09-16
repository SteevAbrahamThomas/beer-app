import streamlit as st
import pickle

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# App title
st.title("🍺 Alcohol Consumption Predictor")

# Center and resize welcome image
col1, col2, col3 = st.columns([1, 2, 1])  # middle column is wider
with col2:
    st.image("https://images.unsplash.com/photo-1516455590571-18256e5bb9ff", width=450)

st.write(
    "Welcome! This app predicts the **total litres of pure alcohol consumed per person per year** "
    "based on beer, spirit, and wine servings."
)

# User inputs
beer = st.number_input("Beer Servings 🍺", min_value=0, max_value=500, value=50)
spirit = st.number_input("Spirit Servings 🥃", min_value=0, max_value=500, value=30)
wine = st.number_input("Wine Servings 🍷", min_value=0, max_value=500, value=20)

# Predict button
if st.button("Predict"):
    prediction = model.predict([[beer, spirit, wine]])[0]
    st.success(f"Predicted Total Litres of Pure Alcohol: **{prediction:.2f} litres**")

