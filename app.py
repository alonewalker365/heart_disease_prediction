import streamlit as st
import numpy as np
import pandas as pd
import pickle

pickle_in=open('model.pkl','rb')
model=pickle.load(pickle_in)



def main():
    st.title('Heart Disease')
    html_tnp = """
    <div style="background-color:tomato; padding:10px;">
        <h2 style="color:white; text-align:center;">Heart Disease Prediction</h2>
    </div>
    """
    st.markdown(html_tnp, unsafe_allow_html=True)

    age=st.number_input("Age")
    sex=st.text_input("Sex")
    chest_pain=st.number_input("Chest pain type")
    bp=st.number_input("BP")
    cholesterol=st.number_input("Cholesterol")
    fbs=st.number_input("Blood Sugar")
    ekg=st.number_input("EKG results")
    hr=st.number_input("MAX HR")
    angina=st.number_input("Exercise angina")
    st_depression=st.number_input("ST depression")
    slope_st=st.number_input("Slope of ST")
    fluro=st.number_input("Number of vessels fluro")
    thallium=st.number_input("Thallium")

    if sex=='male':
        sx=1
    else:
        sx=0

    if fbs>120:
        bs=1
    else:
        bs=0


    if st.button('Predict'):
        input_data=np.array([[age,sx,chest_pain,bp,cholesterol,bs,ekg,hr,angina,st_depression,slope_st,fluro,thallium]])

        pred = model.predict(input_data)
        if pred<0 or pred>1:
            pred=np.round(pred)

        pred_percentage =pred*100

        st.success("you have {}% chance of getting heart disease".format(pred_percentage))

    
if __name__ == '__main__' :
    main()
