import streamlit as st
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Medicaid Enrollment Prediction",
    page_icon="📊"
)

st.title("Predicting Medicaid Enrollment")

st.write(
    "A supervised machine learning project using "
    "CPS-ASEC data from 2008–2020."
)

st.subheader("Project Overview")

st.write(
    "This project predicts historical Medicaid enrollment "
    "among low-income adults aged 18–64 using demographic, "
    "employment, health, and income characteristics."
)

st.write(
    "The sample includes 256,722 observations with "
    "family income at or below 138% of the federal "
    "poverty guideline."
)

st.subheader("Model Performance")

col1, col2, col3 = st.columns(3)

col1.metric("Test ROC-AUC", "0.7968")
col2.metric("Test Accuracy", "71.92%")
col3.metric("Test Recall", "73.54%")

st.subheader("Machine Learning Methods")

st.write(
    "Models evaluated include Random Forest and "
    "Histogram Gradient Boosting. "
    "The final model is Histogram Gradient Boosting."
)

st.subheader("Saved Model")

model_path = Path(__file__).parent / "models" / "medicaid_gradient_boosting.joblib"

if model_path.exists():
    model = joblib.load(model_path)
    st.success("Trained model loaded successfully.")
else:
    st.warning("Saved model not found.")

st.info(
    "This project is for educational and research purposes. "
    "It predicts historical Medicaid coverage, not "
    "Medicaid eligibility or future enrollment."
)
