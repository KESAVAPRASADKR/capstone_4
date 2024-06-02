import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load models and columns used for training
with open('model.pkl', 'rb') as f:
    reg_model = pickle.load(f)

with open('model_2.pkl', 'rb') as f:
    clf_model = pickle.load(f)

with open('X_reg_columns.pkl', 'rb') as f:
    X_reg_columns = pickle.load(f)

with open('X_clf_columns.pkl', 'rb') as f:
    X_clf_columns = pickle.load(f)

st.title('Copper Industry Price and Lead Prediction')

# Task selection
task = st.selectbox('Select Task', ['Regression', 'Classification'])

def preprocess_input(input_data, model_columns):
    # Handle missing values
    
    
    # Impute missing values
    for column in input_data.select_dtypes(include=['float64', 'int64']).columns:
        input_data[column] = input_data[column].fillna(input_data[column].median())
    
    for column in input_data.select_dtypes(include=['object']).columns:
        input_data[column] = input_data[column].fillna(input_data[column].mode()[0])
    
    # Check for skewness and apply log transformation
    numerical_cols = input_data.select_dtypes(include=['float64', 'int64']).columns
    skewed_cols = input_data[numerical_cols].apply(lambda x: x.skew()).sort_values(ascending=False)
    skewed_cols = skewed_cols[skewed_cols > 0.75]
    for col in skewed_cols.index:
        input_data[col] = np.log1p(input_data[col])
    
    # Encode categorical variables
    categorical_cols = ['customer', 'country', 'item type', 'application', 'product_ref']
    input_data = pd.get_dummies(input_data, columns=categorical_cols)
    
    # Reindex to ensure all necessary columns are present
    input_data = input_data.reindex(columns=model_columns, fill_value=0)
    
    return input_data

# Input fields
if task == 'Regression':
    item_day = st.number_input('Enter item day', min_value=0.0)
    item_month = st.number_input('Enter item month', min_value=0.0)
    item_year = st.number_input('Enter item year', min_value=0.0)
    customer = st.text_input('Customer')
    country = st.text_input('Country')
    item_type = st.text_input('Item Type')
    application = st.text_input('Application')
    product_ref = st.text_input('Product Reference')
    quantity_tons = st.number_input('Quantity Tons', min_value=0.0)
    thickness = st.number_input('Thickness', min_value=0.0)
    width = st.number_input('Width', min_value=0.0)
    d_day = st.number_input('Enter delivery day', min_value=0.0)
    d_month = st.number_input('Enter delivery month', min_value=0.0)
    d_year = st.number_input('Enter delivery year', min_value=0.0)

    # Prepare input data
    input_data = pd.DataFrame({
        'item_day': [item_day],
        'item_month': [item_month],
        'item_year': [item_year],
        'customer': [customer],
        'country': [country],
        'item type': [item_type],
        'application': [application],
        'product_ref': [product_ref],
        'quantity tons': [quantity_tons],
        'thickness': [thickness],
        'width': [width],
        'd_day': [d_day],
        'd_month': [d_month],
        'd_year': [d_year]
    })

    # Preprocess input data
    input_data = preprocess_input(input_data, X_reg_columns)

    # Make prediction
    prediction = reg_model.predict(input_data)
    st.write(f'Predicted Selling Price: {prediction[0]}')

elif task == 'Classification':
    item_day = st.number_input('Enter item day', min_value=0.0)
    item_month = st.number_input('Enter item month', min_value=0.0)
    item_year = st.number_input('Enter item year', min_value=0.0)
    customer = st.text_input('Customer')
    country = st.text_input('Country')
    item_type = st.text_input('Item Type')
    application = st.text_input('Application')
    #material_ref = st.text_input('Material Reference')
    product_ref = st.text_input('Product Reference')
    quantity_tons = st.number_input('Quantity Tons', min_value=0.0)
    thickness = st.number_input('Thickness', min_value=0.0)
    width = st.number_input('Width', min_value=0.0)
    d_day = st.number_input('Enter delivery day', min_value=0.0)
    d_month = st.number_input('Enter delivery month', min_value=0.0)
    d_year = st.number_input('Enter delivery year', min_value=0.0)

    # Prepare input data
    input_data = pd.DataFrame({
        'item_day': [item_day],
        'item_month': [item_month],
        'item_year': [item_year],
        'customer': [customer],
        'country': [country],
        'item type': [item_type],
        'application': [application],
        'product_ref': [product_ref],
        'quantity tons': [quantity_tons],
        'thickness': [thickness],
        'width': [width],
        'd_day': [d_day],
        'd_month': [d_month],
        'd_year': [d_year]
    })

    # Preprocess input data
    input_data = preprocess_input(input_data, X_clf_columns)

    # Make prediction
    prediction = clf_model.predict(input_data)
    status = 'WON' if prediction[0] == 1 else 'LOST'
    st.write(f'Predicted Status: {status}')
