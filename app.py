import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load models and columns used for training
with open('model_regression.pkl', 'rb') as f:
    reg_model = pickle.load(f)

with open('model_classifer.pkl', 'rb') as f:
    clf_model = pickle.load(f)

st.title('Industry Copper Price Prediction')

# Task selection
task = st.selectbox('Select Task', ['Regression', 'Classification'])

# Input fields
if task == 'Regression':
    col1,col2,col3=st.columns(3)
    with col1:
        i_day = st.selectbox('Select item day', options=list(range(1, 32)), index=0)
        i_month = st.selectbox('Select item month', options=list(range(1, 13)), index=0)
        i_year = st.number_input('Enter item year', min_value=2020)
        customer = st.number_input('enter customer number',min_value=12458,max_value=30408185)
        countries = [28., 32., 38., 78., 27., 30., 25., 77., 79., 39., 40., 26., 84., 80., 113., 107., 89.]
        country = st.selectbox('Select Country', options=countries)
        item=[4., 3., 1., 2., 5., 0.]
        st.write("'W'=5., 'WI'=6., 'S'=3., 'Others'=1., 'PL'=2., 'IPL'=0., 'SLAWR'=4.")
        item_type = st.selectbox('Select item type', options=item)
        application = st.number_input('enter  application number',min_value=2,max_value=99)
    with col2:
        pass
    with col3:
        reference=[1670798778,     611993, 1668701376,  164141591,     628377,
        1671863738,     640665, 1332077137, 1668701718,     640405,
        1693867550, 1665572374, 1282007633, 1668701698,     628117,
        1690738206,  164337175, 1668701725, 1665572032, 1721130331,
        1693867563,     611733, 1690738219,  929423819]
        product_ref = st.selectbox('Select product reference', options=reference)
        quantity_tons = st.number_input('enter quantity',min_value=-18,max_value=151)
        thickness = st.number_input('enter thickness',min_value=1.0,max_value=6.4)
        width = st.number_input('enter width',min_value=735,max_value=1880)
        d_day = st.selectbox('Select delivery day', options=list(range(1, 32)), index=0)
        d_month = st.selectbox('Select delivery month', options=list(range(1, 13)), index=0)
        d_year = st.number_input('Enter delivery year', min_value=2020)
        status=st.number_input('Enter status 0 for win  or 1 for loss',min_value=0,max_value=1)
 

    # Prepare input data

    input_data = pd.DataFrame({'quantity tons': [quantity_tons],'customer': [customer],'country': [country],'status':[status],'item type': [item_type],
                    'application': [application],'thickness': [thickness],'width': [width],'product_ref': [product_ref],
                                  'i_day': [i_day],'i_month': [i_month],'i_year': [i_year],'d_day': [d_day],'d_month': [d_month],
                                  'd_year': [d_year]})

    # Preprocess input data
    if st.button('Submit'):  
        prediction = reg_model.predict(input_data)
        st.write(f'Predicted Selling Price: {prediction[0]}')
    else:
        st.write('Please enter input data.')

elif task == 'Classification':
    col4,col5,col6=st.columns(3)
    with col4:
        i_day = st.selectbox('Select item day', options=list(range(1, 32)), index=0)
        i_month = st.selectbox('Select item month', options=list(range(1, 13)), index=0)
        i_year = st.number_input('Enter item year', min_value=2020)
        customer = st.number_input('enter customer number',min_value=12458,max_value=30408185)
        countries = [28., 32., 38., 78., 27., 30., 25., 77., 79., 39., 40., 26., 84., 80., 113., 107., 89.]
        country = st.selectbox('Select Country', options=countries)
        item=[4., 3., 1., 2., 5., 0.]
        st.write("'W'=5., 'WI'=6., 'S'=3., 'Others'=1., 'PL'=2., 'IPL'=0., 'SLAWR'=4.")
        item_type = st.selectbox('Select item type', options=item)
        application = st.number_input('enter application number',min_value=2,max_value=99)
    with col5:
        pass
    with col6:
        reference=[1670798778,     611993, 1668701376,  164141591,     628377,
        1671863738,     640665, 1332077137, 1668701718,     640405,
        1693867550, 1665572374, 1282007633, 1668701698,     628117,
        1690738206,  164337175, 1668701725, 1665572032, 1721130331,
        1693867563,     611733, 1690738219,  929423819]
        product_ref = st.selectbox('Select product reference', options=reference)
        quantity_tons = st.number_input('enter quantity',min_value=-18.0,max_value=151.0)
        thickness = st.number_input('enter thickness',min_value=0.1,max_value=6.4)
        width = st.number_input('enter width',min_value=735,max_value=1880)
        d_day = st.selectbox('Select delivery day', options=list(range(1, 32)), index=0)
        d_month = st.selectbox('Select delivery month', options=list(range(1, 13)), index=0)
        d_year = st.number_input('Enter delivery year', min_value=2020)
        selling_price=st.number_input('enter selling price',min_value=0)
    # Prepare input data
    input_data_1 = pd.DataFrame({'quantity tons': [quantity_tons],'customer': [customer],'country': [country],'item type': [item_type],
                    'application': [application],'thickness': [thickness],'width': [width],'product_ref': [product_ref],
                                  'i_day': [i_day],'i_month': [i_month],'i_year': [i_year],'d_day': [d_day],'d_month': [d_month],
                                  'd_year': [d_year],'selling_price':[selling_price]})
    if st.button('Submit'):  
        prediction = clf_model.predict(input_data_1)
        status = 'WON' if prediction[0] == 0. else 'LOST'
        st.write(f'Predicted Status: {status}')
    else:
        st.write('Please enter input data.')
