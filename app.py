# https://discuss.streamlit.io/t/how-to-launch-streamlit-app-from-google-colab-notebook/42399
# %%writefile app.py

import streamlit as st
import requests
import numpy as np

st.set_page_config(layout="wide")
st.title("Prédiction de Prêt Bancaire")
API_URL = "https://p7pythonapi2.azurewebsites.net/predict"

# Création des champs de saisie
col1, col2, col3 = st.columns(3)

with col1:
  EXT_SOURCE_1 = st.number_input("EXT_SOURCE_1")
  EXT_SOURCE_2 = st.number_input("EXT_SOURCE_2")
  EXT_SOURCE_3 = st.number_input("EXT_SOURCE_3")
  CC_CNT_DRAWINGS_ATM_CURRENT_MEAN = st.number_input("CC_CNT_DRAWINGS_ATM_CURRENT_MEAN")
  CC_CNT_DRAWINGS_CURRENT_MAX = st.number_input("CC_CNT_DRAWINGS_CURRENT_MAX")
  BURO_DAYS_CREDIT_MEAN = st.number_input("BURO_DAYS_CREDIT_MEAN")
  CC_AMT_BALANCE_MEAN = st.number_input("CC_AMT_BALANCE_MEAN")
  CC_AMT_TOTAL_RECEIVABLE_MEAN = st.number_input("EXT_CC_AMT_TOTAL_RECEIVABLE_MEANSOURCE_3")
  CC_AMT_RECIVABLE_MEAN = st.number_input("CC_AMT_RECIVABLE_MEAN")
  CC_AMT_RECEIVABLE_PRINCIPAL_MEAN = st.number_input("CC_AMT_RECEIVABLE_PRINCIPAL_MEAN")
  CC_CNT_DRAWINGS_CURRENT_MEAN = st.number_input("CC_CNT_DRAWINGS_CURRENT_MEAN")
with col2:
  BURO_MONTHS_BALANCE_SIZE_MEAN = st.number_input("BURO_MONTHS_BALANCE_SIZE_MEAN")
  BURO_CREDIT_ACTIVE_Closed_MEAN = st.number_input("BURO_CREDIT_ACTIVE_Closed_MEAN")
  DAYS_BIRTH = st.number_input("DAYS_BIRTH")
  PREV_NAME_CONTRACT_STATUS_Refused_MEAN = st.number_input("PREV_NAME_CONTRACT_STATUS_Refused_MEAN")
  BURO_CREDIT_ACTIVE_Active_MEAN = st.number_input("BURO_CREDIT_ACTIVE_Active_MEAN")
  BURO_DAYS_CREDIT_MIN = st.number_input("BURO_DAYS_CREDIT_MIN")
  DAYS_EMPLOYED = st.number_input("DAYS_EMPLOYED")
  PREV_CODE_REJECT_REASON_XAP_MEAN = st.number_input("PREV_CODE_REJECT_REASON_XAP_MEAN")
  CC_AMT_INST_MIN_REGULARITY_MEAN = st.number_input("CC_AMT_INST_MIN_REGULARITY_MEAN")
  BURO_MONTHS_BALANCE_MIN_MIN = st.number_input("BURO_MONTHS_BALANCE_MIN_MIN")
with col3:
  CC_CNT_DRAWINGS_POS_CURRENT_MAX = st.number_input("CC_CNT_DRAWINGS_POS_CURRENT_MAX")
  BURO_DAYS_CREDIT_UPDATE_MEAN = st.number_input("BURO_DAYS_CREDIT_UPDATE_MEAN")
  CC_AMT_BALANCE_MAX = st.number_input("CC_AMT_BALANCE_MAX")
  CC_AMT_TOTAL_RECEIVABLE_MAX = st.number_input("CC_AMT_TOTAL_RECEIVABLE_MAX")
  CC_AMT_RECIVABLE_MAX = st.number_input("CC_AMT_RECIVABLE_MAX")
  DAYS_EMPLOYED_PERC = st.number_input("DAYS_EMPLOYED_PERC")
  CC_AMT_RECEIVABLE_PRINCIPAL_MAX = st.number_input("CC_AMT_RECEIVABLE_PRINCIPAL_MAX")
  ACTIVE_MONTHS_BALANCE_SIZE_MEAN = st.number_input("ACTIVE_MONTHS_BALANCE_SIZE_MEAN")
  REFUSED_DAYS_DECISION_MAX = st.number_input("REFUSED_DAYS_DECISION_MAX")

if st.button("Predict"):
    # Prepare feature data as JSON payload
  feature_data = {
      "EXT_SOURCE_1": EXT_SOURCE_1,
      "EXT_SOURCE_2": EXT_SOURCE_2,
      "EXT_SOURCE_3": EXT_SOURCE_3,
      "CC_CNT_DRAWINGS_ATM_CURRENT_MEAN": CC_CNT_DRAWINGS_ATM_CURRENT_MEAN,
      "CC_CNT_DRAWINGS_CURRENT_MAX": CC_CNT_DRAWINGS_CURRENT_MAX,
      "BURO_DAYS_CREDIT_MEAN": BURO_DAYS_CREDIT_MEAN,
      "CC_AMT_BALANCE_MEAN": CC_AMT_BALANCE_MEAN,
      "CC_AMT_TOTAL_RECEIVABLE_MEAN": CC_AMT_TOTAL_RECEIVABLE_MEAN,
      "CC_AMT_RECIVABLE_MEAN": CC_AMT_RECIVABLE_MEAN,
      "CC_AMT_RECEIVABLE_PRINCIPAL_MEAN": CC_AMT_RECEIVABLE_PRINCIPAL_MEAN,
      "CC_CNT_DRAWINGS_CURRENT_MEAN": CC_CNT_DRAWINGS_CURRENT_MEAN,
      "BURO_MONTHS_BALANCE_SIZE_MEAN": BURO_MONTHS_BALANCE_SIZE_MEAN,
      "BURO_CREDIT_ACTIVE_Closed_MEAN": BURO_CREDIT_ACTIVE_Closed_MEAN,
      "DAYS_BIRTH": DAYS_BIRTH,
      "PREV_NAME_CONTRACT_STATUS_Refused_MEAN": PREV_NAME_CONTRACT_STATUS_Refused_MEAN,
      "BURO_CREDIT_ACTIVE_Active_MEAN": BURO_CREDIT_ACTIVE_Active_MEAN,
      "BURO_DAYS_CREDIT_MIN": BURO_DAYS_CREDIT_MIN,
      "DAYS_EMPLOYED": DAYS_EMPLOYED,
      "PREV_CODE_REJECT_REASON_XAP_MEAN": PREV_CODE_REJECT_REASON_XAP_MEAN,
      "CC_AMT_INST_MIN_REGULARITY_MEAN": CC_AMT_INST_MIN_REGULARITY_MEAN,
      "BURO_MONTHS_BALANCE_MIN_MIN": BURO_MONTHS_BALANCE_MIN_MIN,
      "CC_CNT_DRAWINGS_POS_CURRENT_MAX": CC_CNT_DRAWINGS_POS_CURRENT_MAX,
      "BURO_DAYS_CREDIT_UPDATE_MEAN": BURO_DAYS_CREDIT_UPDATE_MEAN,
      "CC_AMT_BALANCE_MAX": CC_AMT_BALANCE_MAX,
      "CC_AMT_TOTAL_RECEIVABLE_MAX": CC_AMT_TOTAL_RECEIVABLE_MAX,
      "CC_AMT_RECIVABLE_MAX": CC_AMT_RECIVABLE_MAX,
      "DAYS_EMPLOYED_PERC": DAYS_EMPLOYED_PERC,
      "CC_AMT_RECEIVABLE_PRINCIPAL_MAX": CC_AMT_RECEIVABLE_PRINCIPAL_MAX,
      "ACTIVE_MONTHS_BALANCE_SIZE_MEAN": ACTIVE_MONTHS_BALANCE_SIZE_MEAN,
      "REFUSED_DAYS_DECISION_MAX": REFUSED_DAYS_DECISION_MAX,
  }

  # Afficher le JSON pour vérification
  st.write(feature_data)
  # Call FastAPI endpoint and get prediction result
  headers = {'Content-Type': 'application/json'}
  response = requests.post(API_URL, json=feature_data)
  # Display prediction result
  st.write(f"Prediction: {response}")
