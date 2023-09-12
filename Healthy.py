# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 16:21:22 2022

@author: Ammar
"""

import streamlit as st
import joblib


def main():
    
    html_temp="""
    <div style ="background-color:lightblue;padding:16px">
    <h2 style ="color:blue;text-align=center">Health Insurance Cost Prodiction Using ML</h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    model = joblib.load('model_joblib_gr')
    
   
    p1 = st.slider("Enter Your Age",18,100)
    
    s1=st.selectbox("Sex",("Male","Female"))
    if s1=="Male":
        p2=1
    else:
        p2=0

    p3 =st.number_input("Enter Your BMI Value")
    p4 = st.slider("Enter Number of Children",0,4) 
    
    s2=st.selectbox("Smoker",("Yes","No"))
    if s2=="Yes":
        p5=1
    else:
        p5=0
    s3=st.selectbox("Region",("southwest","southeast","northwest","northeast")) 
    if s3=="southwest":
        p6=1
    elif s3=="southeast":
        p6=2    
    elif s3=="northwest":
        p6=3
    else:
        p6=4  
    
    
    if st.button('Predict'):
        prediction = model.predict([[p1,p2,p3,p4,p5,p6]])
        st.balloons()
        st.success('Insurance Amount is {} '.format(round(prediction[0],2)))    
    
          
    
if __name__ == '__main__':
    main()