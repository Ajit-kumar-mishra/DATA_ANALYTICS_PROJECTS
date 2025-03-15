import joblib
import pandas as pd

# Load the model and scaler
model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')

# Example employee data (replace with actual data)
df_employee = pd.DataFrame({
    'Age': [41],
    'DailyRate': [1102],
    'DistanceFromHome': [1],
    'EnvironmentSatisfaction': [2],
    'HourlyRate': [94],
    'JobInvolvement': [3],
    'JobLevel': [2],
    'JobSatisfaction': [4],
    'MonthlyIncome': [5993],
    'MonthlyRate': [19479],
    'NumCompaniesWorked': [8],
    'PercentSalaryHike': [11],
    'PerformanceRating': [3],
    'RelationshipSatisfaction': [1],
    'StockOptionLevel': [0],
    'TotalWorkingYears': [8],
    'TrainingTimesLastYear': [0],
    'WorkLifeBalance': [1],
    'YearsAtCompany': [6],
    'YearsInCurrentRole': [4],
    'YearsSinceLastPromotion': [0],
    'YearsWithCurrManager': [5],
    'Gender_encoded': [0],
    'OverTime_encoded': [1],
    'BT_Non-Travel': [0],
    'BT_Travel_Frequently': [1],
    'BT_Travel_Rarely': [0],
    'Dept_Human Resources': [0],
    'Dept_Research & Development': [1],
    'Dept_Sales': [0],
    'Edu_Human Resources': [0],
    'Edu_Life Sciences': [0],
    'Edu_Marketing': [0],
    'Edu_Medical': [0],
    'Edu_Other': [0],
    'Edu_Technical Degree': [1],
    'Job_Healthcare Representative': [0],
    'Job_Human Resources': [0],
    'Job_Laboratory Technician': [0],
    'Job_Manager': [1],
    'Job_Manufacturing Director': [0],
    'Job_Research Director': [0],
    'Job_Research Scientist': [0],
    'Job_Sales Executive': [0],
    'Job_Sales Representative': [0],
    'Marital_Divorced': [0],
    'Marital_Married': [1],
    'Marital_Single': [0]
})

# Encode categorical features
df_employee_encoded = pd.get_dummies(df_employee)

# Align the columns with the training data (reorder and fill missing with 0)
training_columns = scaler.feature_names_in_
df_employee_encoded = df_employee_encoded.reindex(columns=training_columns, fill_value=0)

# Feature scaling
df_employee_scaled = scaler.transform(df_employee_encoded)

# Make predictions
employee_churn_prob = model.predict_proba(df_employee_scaled)[:, 1]  # Probability for class 1 (likely to leave)
employee_churn_class = (employee_churn_prob >= 0.5).astype(int)

# Print the results
print(f"Probability of employee leaving: {employee_churn_prob[0]:.2f}")
if employee_churn_class == 1:
    print("The employee is likely to leave the company.")
else:
    print("The employee is likely to stay with the company.")
