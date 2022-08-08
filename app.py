import streamlit as st
import pandas as pd
import numpy as np
import pickle
# from sklearn.ensemble import RandomForestClassifier
# from sklearn import datasets

pickle_in = open('bengaluru_home_price_prediction.pickle', 'rb')
classifier = pickle.load(pickle_in)
def Welcome():
    return 'Welcome All!'

def predict_price(location,sqft,bath,bhk):
#   loc_index = np.where(X.columns==location)[0][0]
  x = np.zeros(244)
  x[0] = sqft
  x[1] = bath
  x[2] = bhk
#   if loc_index >= 0:
#     x[loc_index] = 1
  return np.round(classifier.predict([x])[0],2)

def main():
    home = pd.read_csv("Bengaluru_House_Data.csv")
    loc = home['location'].unique()
    st.title("Bengaluru House Price Predictor")
    st.header("Streamlit House Price Prediction ML App")
    st.subheader('Please enter the required(*) details: ')
    location = st.selectbox('Location* :',loc)
    sqft = st.text_input("Sq-Ft Area* :","")
    bhk = st.text_input("BHK* :","")
    bath = st.text_input("Number of Bathrooms* :","")
    result=""
    if st.button("House Price in INR"):
        result= predict_price(location,sqft,bath,bhk)
    st.success("The Final Price is INR {} Lacs".format(result))

if __name__ == '__main__':
    main()
