
# Predicting Medicaid Enrollment Using Machine Learning

## Project Overview

This project uses supervised machine learning to predict historical Medicaid enrollment among low-income adults in the United States.

Using CPS-ASEC data from 2008–2020, I develop and evaluate machine learning models to identify patterns associated with Medicaid enrollment.

## Dataset

- Source: Current Population Survey Annual Social and Economic Supplement (CPS-ASEC)
- Years: 2008–2020
- Population: Adults aged 18–64
- Income restriction: Family income at or below 138% of the federal poverty guideline
- Sample size: 256,722 observations

## Machine Learning Methods

The project includes:

- Data cleaning and feature engineering
- Categorical variable encoding
- Random Forest classification
- Histogram Gradient Boosting
- Hyperparameter tuning
- Model comparison and evaluation
- Permutation feature importance
- Probability calibration

## Final Model Performance

The final model is a Histogram Gradient Boosting classifier.

| Metric | Test Performance |
|---|---|
| ROC-AUC | 0.7968 |
| Accuracy | 71.92% |
| Balanced Accuracy | 72.38% |
| Recall (Enrolled) | 73.54% |
| Brier Score | 0.1611 |

## Streamlit Application

A Streamlit dashboard presents the project methodology and model performance.

To run the application locally:

```bash
python -m streamlit run app.py
```

## Limitations

This is a predictive machine learning project, not a causal inference study.

Medicaid coverage is measured for the previous calendar year, while some predictors are measured at the survey interview. Consequently, the model should not be interpreted as a prospective enrollment prediction tool.

The model does not determine Medicaid eligibility.

## Tools

Python, Pandas, NumPy, Scikit-learn, Matplotlib, Joblib, Streamlit.
