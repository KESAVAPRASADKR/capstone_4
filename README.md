
# Project Title

Industrial Copper Modeling


## Module used for the project 
Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, and Streamlit.

## Project pipeline 
1. We convert the csv file into a data frame using pandas
2. We use the EDA Method To correct the data with inaccurate values.
3. We use various methods to find the scaring of the data.
4. We scale the Data which can be used for regression and categorical models.
5. We create both regressor and categorical model and pre train the model and store it in a file using pickle.
6. We develop a front end tool using streamlit where we use the pre trained model to predict the targeted values by getting the input datas from the users.
7. After getting the input data from the user the model will display the targeted output based on the user's input which can be used to take decisions.
## Data preprocessing
We create the data frame using the csv  file we have. After that we find the unique values for each column after finding the unique values we decided to drop id column since it is not related to the selling price and status. The material reference column has many uncertain values we try to convert that values after converting the value We find the null values in the material reference column where the null value is very high which is more than 50 percentage of the data in or null so the material reference column is dropped.

The item date column is in the format of float we convert that float format data into date time format and similarly we do the same for the delivery date columns once this is done we create new columns for item date and delivery date to split the data day month and year into separate columns. We find the difference between the delivery date and the item date where we find inconsistent in the dates so we change the delivery date column where the inconsistent data is happened Using mode.
## Scaling of numerical and categorical columns 
After data processing we find the values of many columns are not under same scale and Oregon not eventually distributed so we use Ordinal encoder to convert the category data into numerical one and for numerical values we use iqr method to scale the numerical columns Once this is done all the values in the data frame are under the same scaling format which can be used for machine learning models
## Correlations 
We use the correlation matrix heat map to find the correlations between futures and the targets in the correlation map we find that all the values are below one so we don't need to remove any columns.
## Splitting the data for models training and testing 
We separate the futures values and target values for the classification and regression models where we will split the data for training and testing of classification and regression models.
## Creating classification and regression models 
After splitting the data for regressor model we use random forest regressor for regression and for classifier We use extra tree classifier we set the features and target values for both the models and train the models after training we find the accuracy of the both the models.
## Save the trained models 
We use pickle method to save the Pre trained classification and regression models which can be used for predicting the target values if the user gives that values to the models
## Creating a front end tool using streamlit
We use the streamlined tab to create front end tool where the user can use the input data of feature's Values and then the model will predict the target values and display the value. We create a streamlit application in a way where the user will give the input data for regression and classification models and the target value will be displayed once the values are entered.
## Outcome of the project 
Using the industrial copper modelling app developed using streamlit and python the user will be able to predict the selling price of the copper and the status based on the users values Which can be helpful to Take decisions based on the predicted values.