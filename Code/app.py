import streamlit as st
import pickle
import pandas as pd
from zipfile import ZipFile
import os


import sys
sys.path.insert(0, '../src')
import unittest

st.set_page_config(page_title='Credit Score App', page_icon='🕰️',  layout='wide',
                   initial_sidebar_state='auto', menu_items={
                        'Get Help': None,
                        'Report a bug': 'https://github.com/gentallman/Capstone/blob/main/issues',
                        'About': '''
                        This app was made by **Group 11 (Section 002)** and its purpose is to showcase how a Credit Score Evaluation is done under Capstone Project Work. 
                        
                        This evaluation is using a Machine Learning model, and you can learn more about how the model work and how I got here by going to the GitHub [repository](https://github.com/gentallman/Capstone).
                        '''
     })

def transform_resp(resp):
    df = pd.DataFrame.from_dict(resp, orient='index').T  # Convert dictionary to a pandas DataFrame
    return df

path = os.path.dirname(__file__)
folder_path = os.path.join(path,'..\\models')

@st.cache_resource()
def unzip_load(name):
    path_zip = os.path.join(path,'/main/code/models/' +name+ '.zip')
    ZipFile(path_zip).extractall(folder_path)
    path_obj = os.path.join(path,'/main/code/models/' +name+ '.obj')
    return  pickle.load(open(path_obj, 'rb'))

scaler = unzip_load('scaler')
rf = unzip_load('rf')

CreditMix = [-1,0,1]
Credit_mix_default = 2
Num_of_Delayed_Payment_default = 0
Num_Credit_Card_default = 0
Num_Bank_Accounts_default = 0
Outstanding_Debt_default = 0.00
Interest_Rate_default = 0
Num_of_Loan_default = 0
Delay_from_due_date_default = 0

Payment_of_Min_Amount_default = 0

Num_Credit_Inquiries_default = 0
Credit_history_default = 0

st.title('Credit Scoring System')
st.caption('Made by Group 11')

st.markdown('''
            This is merely a mock-up that has been created for the purpose of providing information(as Capstone Project Work); if you are interested in learning more about the model that underlies this, please visit the GitHub [repository](https://github.com/gentallman/Capstone). \n
            On the left, there's a sidebar (click `>` if you don't see it). Where you can fill out a form - _this data is not saved_ - click on the button `See` to see how each piece of information you provided impacts credit score.
''')

profile = st.radio('Choose a profile:', options=['Smit', 'Avi','Vaibhav'], horizontal=True)
if profile == 'Smit':
    Credit_mix_default = 2
    Num_Credit_Card_default = 2
    Num_Bank_Accounts_default = 2
    Outstanding_Debt_default = 400.00
    Interest_Rate_default = 3
    Delay_from_due_date_default = 0
    Num_of_Delayed_Payment_default = 3
    Num_of_Loan_default = 1
    Payment_of_Min_Amount_default = 1
    Num_Credit_Inquiries_default = 1
    Credit_history_default = 300
elif profile == 'Avi':
    Credit_mix_default = 1
    Num_Credit_Card_default = 6
    Num_Bank_Accounts_default = 7
    Outstanding_Debt_default = 100.00
    Interest_Rate_default = 14
    Delay_from_due_date_default = 3
    Num_of_Delayed_Payment_default = 11
    Num_of_Loan_default = 5
    Payment_of_Min_Amount_default = 0
    Num_Credit_Inquiries_default = 6
    Credit_history_default = 278
elif profile == 'Vaibhav':
    Credit_mix_default = 0
    Num_Credit_Card_default = 3
    Num_Bank_Accounts_default = 3
    Outstanding_Debt_default = 777.00
    Interest_Rate_default = 6
    Delay_from_due_date_default = 3
    Num_of_Delayed_Payment_default = 6
    Num_of_Loan_default = 1
    Payment_of_Min_Amount_default = 1
    Num_Credit_Inquiries_default = 3
    Credit_history_default = 400

with st.sidebar:
    st.header('Evaluation Section')
    Num_Credit_Card = st.number_input('No. of Credit Cards Owns', min_value=0, max_value=11, step=1, value=Num_Credit_Card_default)
    Num_Bank_Accounts = st.number_input('No. of Bank Accounts there', min_value=0, max_value=11, step=1, value=Num_Bank_Accounts_default)
    Outstandin_Debt = st.number_input('Outstanding Balance', min_value=0.00, max_value=5000.00, value=Outstanding_Debt_default)
    Interest_Rate = st.number_input('Interest Rate on Loans ', min_value=0, max_value=33, value=Interest_Rate_default)
    Delay_from_due_date = st.number_input('Average No. of Days delayed from the date of bill payment', min_value=0, max_value=20, step=1, value=Delay_from_due_date_default)
    Num_of_Delayed_Payment = st.number_input('No. of Delay Payment', min_value=0, max_value=25, step=1, value=Num_of_Delayed_Payment_default)
    Credit_mix = st.radio("Credit Mix", CreditMix , Credit_mix_default)
    Num_of_Loan = st.number_input('No. of Loans', min_value=0, max_value=9, step=1, value=Num_of_Loan_default)
    Payment_of_Min_Amount = st.radio('Yes if the person paid the minimum amount to be paid only, otherwise no.', [1, 0], index=Payment_of_Min_Amount_default)
    Credit_history = st.number_input('Age of the Credit History (Months)', min_value=0, max_value=500, step=1, value=Credit_history_default)
    Num_Credit_Inquiries = st.number_input('No. of Credit Card Inquiries', min_value=0, max_value=15, step=1, value=Num_Credit_Inquiries_default)


    run = st.button('See')

st.header('Credit Score Results')

col1, col2 = st.columns([3, 2])


with col1:

    placeholder = st.empty()

    if run:
        resp = {
            'Num_Credit_Card': Num_Credit_Card,
            'Num_Bank_Accounts': Num_Bank_Accounts,
            'Outstandin_Debt': Outstandin_Debt,
            'Interest_Rate' : Interest_Rate,
            'Delay_from_due_date': Delay_from_due_date,
            'Num_of_Delayed_Payment' : Num_of_Delayed_Payment,
            'Credit_mix': Credit_mix,
            'Num_of_Loan': Num_of_Loan,
            'Payment_of_Min_Amount': Payment_of_Min_Amount,
            'Credit_history': Credit_history,
            'Num_Credit_Inquiries': Num_Credit_Inquiries
        }
        output = transform_resp(resp)
        output = pd.DataFrame(output, index=[0])
        output.loc[:,:] = scaler.transform(output)

        credit_score = rf.predict(output)[0]
        
        if credit_score == 1:
            st.success('Your credit score is **GOOD**! Congratulations!', icon="✅")
            st.markdown('This person`s credit score suggests they are likely to make their loan payments on time, making them a low credit risk.')
        elif credit_score == 0:
            st.warning('Your credit score is **REGULAR**', icon="⚠️")
            st.markdown('This person`s credit score shows that they are likely to pay back a loan, but they may sometimes miss a payment. This means that there is a medium risk in giving them credit.')
        elif credit_score == -1:
            st.error('Your credit score is **POOR**.', icon="🚨")
            st.markdown('')







