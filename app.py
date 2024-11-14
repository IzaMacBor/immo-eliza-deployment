import streamlit as st
import pandas as pd
from joblib import load
import json
import os

# Load the trained model
#model_path = os.path.join("random_forest_model.joblib")


# Load mean and std for reversing standardization
with open("price_stats.json", "r") as f:
    stats = json.load(f)

price_mean = stats["price_mean"]
price_std = stats["price_std"]

# Define property options
property_options = {
   "Apartment": {"display": "Apartment", "encoded": 1},
   "House": {"display": "House", "encoded": 0}
}

region_options = {
   "Flanders": {"display": "Flanders", "encoded": 0},
   "Wallonia": {"display": "Wallonia", "encoded": 1},
   "Brussels-Capital": {"display": "Brussels-Capital", "encoded": 2}
}

province_options = {
   "Antwerp": {"display": "Antwerp", "encoded": 0},
   "Brussels": {"display": "Brussels", "encoded": 1},
   "East Flanders": {"display": "East Flanders", "encoded": 2},
   "Flemish Brabant": {"display": "Flemish Brabant", "encoded": 3},
   "Hainaut": {"display": "Hainaut", "encoded": 4},
   "Liège": {"display": "Liège", "encoded": 5},
   "Limburg": {"display": "Limburg", "encoded": 6},
   "Luxembourg": {"display": "Luxembourg", "encoded": 7},
   "Namur": {"display": "Namur", "encoded": 8},
   "Walloon Brabant": {"display": "Walloon Brabant", "encoded": 9},
   "West Flanders": {"display": "West Flanders", "encoded": 10}
}

state_options = {
   "As new": {"display": "As new", "encoded": 0},
   "Just renovated": {"display": "Just renovated", "encoded": 0},
   "Good": {"display": "Good", "encoded": 1},
   "To renovate": {"display": "To renovate", "encoded": 2},
   "To restore": {"display": "To restore", "encoded": 4},
   "To be done up": {"display": "To be done up", "encoded": 5}
}

epc_options = {
   "A++": {"display": "A++", "encoded": 0},
   "A+": {"display": "A+", "encoded": 1},
   "A": {"display": "A", "encoded": 2},
   "B": {"display": "B", "encoded": 3},
   "C": {"display": "C", "encoded": 4},
   "D": {"display": "D", "encoded": 5},
   "E": {"display": "E", "encoded": 6},
   "F": {"display": "F", "encoded": 7},
   "G": {"display": "G", "encoded": 8}
}

# Collect user input
type = st.selectbox(
   "Type of Property", 
   options=list(property_options.keys()),
   format_func=lambda x: property_options[x]["display"]
)

region = st.selectbox(
   "Region", 
   options=list(region_options.keys()),
   format_func=lambda x: region_options[x]["display"]
)

province = st.selectbox(
   "Province", 
   options=list(province_options.keys()),
   format_func=lambda x: province_options[x]["display"]
)

postal_code = st.number_input("Postal Code", min_value=1000, max_value=9999, value=1000)

state = st.selectbox(
   "State of Building", 
   options=list(state_options.keys()),
   format_func=lambda x: state_options[x]["display"]
)

construction_year = st.number_input("Construction year", min_value=1000, max_value=9999, value=1985)
area = st.number_input("Area (m²)", min_value=10, max_value=1000, value=100)
land_sqm = st.number_input("Surface land (m²)", min_value=0, value=0)
nr_of_bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=2)

epc = st.selectbox(
   "Energy Class", 
   options=list(epc_options.keys()),
   format_func=lambda x: epc_options[x]["display"]
)

has_fireplace = st.checkbox("Does the property have a fireplace?")
has_terrace = st.checkbox("Does the property have a terrace?")
has_garden = st.checkbox("Does the property have a garden?")
garden_sqm = st.number_input("Surface garden (m²)", min_value=0, value=0)
has_pool = st.checkbox("Does the property have a swimming pool?")

# Prepare encoded input data
input_data = {
   "subproperty_type_encoded": property_options[type]["encoded"],
   "region_encoded": region_options[region]["encoded"],
   "province_encoded": province_options[province]["encoded"],
   "zip_code": postal_code,
   "state_encoded": state_options[state]["encoded"],
   "construction_year": construction_year,
   "total_area_sqm": area,
   "surface_land_sqm": land_sqm,
   "nbr_bedrooms": nr_of_bedrooms,
   "epc_encoded": epc_options[epc]["encoded"],
   "fl_open_fire": int(has_fireplace),
   "fl_terrace": int(has_terrace),
   "fl_garden": int(has_garden),
   "garden_sqm": garden_sqm,
   "fl_swimming_pool": int(has_pool)
}

# Prediction function using Random Forest model and reversing standardization
def predict_price(input_data, model):
    # Convert input_data into a format suitable for the model (e.g., a list or DataFrame)
    input_features = [
        input_data["subproperty_type_encoded"],
        input_data["region_encoded"],
        input_data["province_encoded"],
        input_data["zip_code"],
        input_data["state_encoded"],
        input_data["construction_year"],
        input_data["total_area_sqm"],
        input_data["surface_land_sqm"],
        input_data["nbr_bedrooms"],
        input_data["epc_encoded"],
        input_data["fl_open_fire"],
        input_data["fl_terrace"],
        input_data["fl_garden"],
        input_data["garden_sqm"],
        input_data["fl_swimming_pool"]
    ]
    
    # Make prediction
    prediction = random_forest_model.predict([input_features])
    
    # Reverse standardization: (predicted_value * price_std) + price_mean
    prediction_original = (prediction[0] * price_std) + price_mean
    return prediction_original

if st.button("Predict"):
    try:
        # Display the input data
        st.write("Input data:", input_data)
        random_forest_model = load('random_forest_model.joblib')
        st.write(random_forest_model)
        # Make the prediction using the model
        prediction = predict_price(input_data,random_forest_model)
        st.success(f"Predicted Property Price: €{prediction:,.2f}")
    except Exception as e:
        st.error(f"Error: {str(e)}")
