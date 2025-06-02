import streamlit as st
import pandas as pd
import pickle

# Load the trained model
XGB = pickle.load(open('XGB.pkl', 'rb'))

def recommendation(Age, BusinessTravel, Department, DistanceFromHome, Education, EducationField, EnvironmentSatisfaction, Gender, jobLevel, JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, NumCompaniesWorked, OverTime, PercentSalaryHike, PerformanceRating, RelationshipSatisfaction, StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole):
    features = pd.DataFrame([[Age, BusinessTravel, Department, DistanceFromHome, Education, EducationField, EnvironmentSatisfaction, Gender, jobLevel, JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, NumCompaniesWorked, OverTime, PercentSalaryHike, PerformanceRating, RelationshipSatisfaction, StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole]],
                            columns=['Age', 'BusinessTravel', 'Department', 'DistanceFromHome', 'Education', 'EducationField', 'EnvironmentSatisfaction', 'Gender', 'jobLevel', 'JobRole', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome', 'NumCompaniesWorked', 'OverTime', 'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction', 'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole'])

    prediction = XGB.predict(features)

    attrition_mapping = {0: 'No', 1: 'Yes'}
    predicted_label = attrition_mapping.get(prediction[0], 'Unknown')

    return prediction[0], predicted_label

# Streamlit app
def main():
    st.title("Employee Attrition Prediction")

    # Set background image
    st.markdown(
        """
        <style>
            body {
                background-image: url('your_background_image_url.jpg');
                background-size: cover;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Collect input features from the user
    col1, col2, col3 = st.columns(3)

    # Column 1
    with col1:
        Age = st.slider('Age', min_value=18, max_value=65, value=30)
        BusinessTravel_mapping = {0: 'Non Travel', 1: 'Travel Frequently', 2: 'Travel Rarely'}
        BusinessTravel = st.selectbox("Business Travel", [0, 1, 2], format_func=lambda x: BusinessTravel_mapping[x])
        Department_mapping = {0: 'Human Resources', 1: 'Research & Development', 2: 'sales'}
        Department = st.selectbox("Department", [0, 1, 2], format_func=lambda x: Department_mapping[x])
        
        DistanceFromHome = st.selectbox('DistanceFromHome', list(range(1, 29)), index=27)
        Education_mapping = {1: '12', 2: "Bachelor's",3:"Master's",4:"PHD",5:"Doctor"}
        Education = st.selectbox("Education", [1, 2,3,4,5], format_func=lambda x: Education_mapping[x])
        EducationField_mapping = {0:"HR",1:'Life Science', 2: "Marketing",3:"Medical",4:"Other",5:"Technical Degree"}
        EducationField = st.selectbox("Education", [0,1, 2,3,4,5], format_func=lambda x: EducationField_mapping[x])
        EnvironmentSatisfaction = st.selectbox('EnvironmentSatisfaction', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        Gender_mapping = {0:"Male",1:"Female"}
        Gender = st.selectbox("Gender", [0,1], format_func=lambda x: Gender_mapping[x])

    # Column 2
    with col2:
        OverTime_mapping = {0:"No",1:"Yes"}
        OverTime = st.selectbox("OverTime", [0,1], format_func=lambda x: OverTime_mapping[x])
        jobLevel = st.selectbox('Job Level', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        JobRole_mapping = {0:"Healthcare Represenative",1:"Human Resource",2:"Laboratory Technician",3:"Manager",4:"Manufacturing Director",5:"Research Director",6:"Research Scientist",7:"Sales Executive",8:"Sales Representative"}
        JobRole = st.selectbox("Job Role", [0,1,2,3,4,5,6,7,8], format_func=lambda x: JobRole_mapping[x])
        JobSatisfaction = st.selectbox('Job Satisfaction', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        MaritalStatus_mapping = {1:"Single",2:"Married",3:"Divorced"}
        MaritalStatus = st.selectbox("Marital Status", [1,2,3], format_func=lambda x: MaritalStatus_mapping[x])
        MonthlyIncome = st.slider('Monthly Income', min_value=1009, max_value=19999, value=19999)
        NumCompaniesWorked = st.selectbox('Num Companies Worked', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        PercentSalaryHike = st.selectbox('Percent Salary Hike', list(range(11, 26)), index=14)

    # Column 3
    with col3:
        PerformanceRating = st.selectbox('Performance Rating', [0, 3, 4])
        RelationshipSatisfaction = st.selectbox('Relationship Satisfaction', [0, 1, 2, 3, 4])
        StockOptionLevel_mapping = {0:"No",1:"Yes"}
        StockOptionLevel = st.selectbox("Stock Option", [0,1], format_func=lambda x: StockOptionLevel_mapping[x])
        TotalWorkingYears = st.selectbox('TotalWorkingYears', list(range(1, 40)), index=19)
        TrainingTimesLastYear = st.selectbox('Training Times Last Year', [0, 1, 2, 3, 4, 5, 6])
        WorkLifeBalance_mapping = {1:"Bad",2:"Good",3:"Better",4:"Excellent"}
        WorkLifeBalance = st.selectbox("WorkLifeBalance", [1,2,3,4], format_func=lambda x: WorkLifeBalance_mapping[x])
        YearsAtCompany = st.selectbox('Years At Company', list(range(1, 41)), index=39)
        YearsInCurrentRole = st.selectbox('Years In Current Role', list(range(1, 19)), index=7)

        # Predict
        if st.button("Predict"):
            prediction_numeric, prediction_label = recommendation(Age, BusinessTravel, Department, DistanceFromHome, Education, EducationField, EnvironmentSatisfaction, Gender, jobLevel, JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, NumCompaniesWorked, OverTime, PercentSalaryHike, PerformanceRating, RelationshipSatisfaction, StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole)
            st.success(f"Predicted Attrition: {prediction_label}")

if __name__ == "__main__":
    main()
