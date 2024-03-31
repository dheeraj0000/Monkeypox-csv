# -- coding: utf-8 --
"""
Created on Wed Mar 13 11:33:56 2024

@author: Dell
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('monkey_pox_model.sav', 'rb'))


# creating a function for Prediction
def monkeypox_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    return prediction


def main():
    # giving a title
    st.title('Monkeypox Prediction Web App')`
    
    # getting the input data from the user
    patient_ID = st.text_input('Enter the patient ID')
    Systemic_Illness = st.text_input('Enter the Systemic Illness')
    Rectal_Pain = st.text_input('Enter the Rectal Pain')
    Sore_Throat = st.text_input('Enter the Sore Throat')
    Penile_Oedema = st.text_input('Enter the Penile Oedema')
    Oral_Lesions = st.text_input('Enter the Oral Lesions')
    Solitary_Lesion = st.text_input('Enter the Solitary Lesion')
    Swollen_Tonsils = st.text_input('Enter the Swollen Tonsils')
    HIV_Infection = st.text_input('Enter the HIV Infection')
    Sexually_Transmitted_Infection = st.text_input('Enter the Sexually Transmitted Infection')
    
    # code for Prediction
    Monkey_disease = ''
    
    # creating a button for Prediction
    if st.button('Monkeypox Test Result'):
        prediction = monkeypox_prediction([patient_ID, Systemic_Illness, Rectal_Pain, Sore_Throat, Penile_Oedema, 
                                           Oral_Lesions, Solitary_Lesion, Swollen_Tonsils, HIV_Infection, 
                                           Sexually_Transmitted_Infection])
        if prediction[0] == 0:
            Monkey_disease = 'The patient has monkeypox disease.'
        else:
            Monkey_disease = 'The patient does not have monkeypox disease.'
            
    st.success(Monkey_disease)
    
if __name__ == '__main__':
    main()
