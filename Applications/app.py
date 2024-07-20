import streamlit as st
import pandas as pd
import numpy as np
import pickle

pipe = pickle.load(open('modelXGB.pkl', 'rb'))

teams = [
    'India',
    'England',
    'New Zealand',
    'Australia',
    'Pakistan',
    'South Africa',
    'West Indies',
    'Sri Lanka',
    'Bangladesh',
    'Afghanistan'
    ]

cities = ['Colombo',
 'Mirpur',
 'Johannesburg',
 'Dubai',
 'Auckland',
 'Cape Town',
 'London',
 'Pallekele',
 'Barbados',
 'Sydney',
 'Melbourne',
 'Durban',
 'St Lucia',
 'Wellington',
 'Lauderhill',
 'Hamilton',
 'Centurion',
 'Manchester',
 'Abu Dhabi',
 'Mumbai',
 'Nottingham',
 'Southampton',
 'Mount Maunganui',
 'Chittagong',
 'Kolkata',
 'Lahore',
 'Delhi',
 'Nagpur',
 'Chandigarh',
 'Adelaide',
 'Bangalore',
 'St Kitts',
 'Cardiff',
 'Christchurch',
 'Trinidad',
 'Brisbane',
 'Birmingham',
 'Hambantota',
 'Dhaka',
 'Lucknow']

st.title('Cricket Score Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))
    
city = st.selectbox('Select City', sorted(cities))

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs Done(Applicable If Overs>5)')
with col5:
    wickets = st.number_input('Wickets Gone')
    
last_five = st.number_input('Runs Socred in last 5 Overs')

if st.button('Predict Score'):
    balls_left = 120 - (overs*6)
    wicket_left = 10 - wickets
    crr = current_score/overs
    
    input_df = pd.DataFrame(
        {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [city], 'current_score': [current_score], 'balls_left': [balls_left], 'wicket_left': [wicket_left], 'crr': [crr], 'last_five': [last_five]}
        
    )
    
    result = pipe.predict(input_df)
    
    st.header("Predicted Score: "  + str(int(result[0])))