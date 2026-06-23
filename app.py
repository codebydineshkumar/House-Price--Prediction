import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("house_price_model.pkl", "rb"))

st.title("House Price Prediction")

under_construction = st.selectbox("Under Construction", [0, 1])
rera = st.selectbox("RERA Approved", [0, 1])
bhk = st.number_input("BHK", min_value=1)
square_ft = st.number_input("Square Feet", min_value=100)
ready_to_move = st.selectbox("Ready To Move", [0, 1])
resale = st.selectbox("Resale", [0, 1])
longitude = st.number_input("Longitude", value=77.0)
latitude = st.number_input("Latitude", value=28.0)
posted_by_dealer = st.selectbox("Posted By Dealer", [0, 1])
posted_by_owner = st.selectbox("Posted By Owner", [0, 1])
bhk_or_rk_rk = st.selectbox("RK", [0, 1])

if st.button("Predict Price"):
    data = pd.DataFrame([[under_construction,
                          rera,
                          bhk,
                          square_ft,
                          ready_to_move,
                          resale,
                          longitude,
                          latitude,
                          posted_by_dealer,
                          posted_by_owner,
                          bhk_or_rk_rk]],
                        columns=['UNDER_CONSTRUCTION',
                                 'RERA',
                                 'BHK_NO.',
                                 'SQUARE_FT',
                                 'READY_TO_MOVE',
                                 'RESALE',
                                 'LONGITUDE',
                                 'LATITUDE',
                                 'POSTED_BY_Dealer',
                                 'POSTED_BY_Owner',
                                 'BHK_OR_RK_RK'])

    prediction = model.predict(data)
    st.success(f"Predicted Price: ₹ {prediction[0]:.2f} Lakhs")