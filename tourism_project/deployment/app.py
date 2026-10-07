import streamlit as st
import pandas as pd
import joblib
import numpy as np

def run():
    st.set_page_config(
        page_title="Wellness Tourism Package Prediction",
        page_icon="✈️",
        layout="centered",
        initial_sidebar_state="expanded",
    )

    st.title("Wellness Tourism Package Prediction")
    st.markdown("Enter customer details to predict if they will purchase the Wellness Tourism Package.")

    # Load the trained model
    model = joblib.load('tourism_project/deployment/best_model.joblib')

    # Load X_train to get the correct column order and dummy variable names
    # This is crucial for consistent preprocessing at inference
    X_train_cols = pd.read_csv('Xtrain.csv').columns.tolist()

    # Input widgets for user features
    st.sidebar.header("Customer Information")

    age = st.sidebar.slider("Age", 18, 90, 30)
    monthly_income = st.sidebar.number_input("Monthly Income", min_value=0.0, value=30000.0, step=1000.0)
    number_of_trips = st.sidebar.slider("Number of Trips (annually)", 1, 20, 5)
    number_of_person_visiting = st.sidebar.slider("Number of Persons Visiting", 1, 10, 1)
    number_of_children_visiting = st.sidebar.slider("Number of Children Visiting (under 5)", 0, 5, 0)
    duration_of_pitch = st.sidebar.slider("Duration of Pitch (minutes)", 5, 60, 15)
    number_of_followups = st.sidebar.slider("Number of Follow-ups", 0, 10, 2)
    pitch_satisfaction_score = st.sidebar.slider("Pitch Satisfaction Score (1-5)", 1, 5, 3)
    preferred_property_star = st.sidebar.slider("Preferred Property Star (1-5)", 1, 5, 3)

    type_of_contact = st.sidebar.selectbox("Type of Contact", ['Self Inquiry', 'Company Invited'])
    city_tier = st.sidebar.selectbox("City Tier", [1, 2, 3])
    occupation = st.sidebar.selectbox("Occupation", ['Salaried', 'Small Business', 'Large Business', 'Free Lancer', 'Government Sector', 'Retired', 'Student'])
    gender = st.sidebar.selectbox("Gender", ['Male', 'Female'])
    marital_status = st.sidebar.selectbox("Marital Status", ['Married', 'Single', 'Divorced', 'Unmarried'])
    designation = st.sidebar.selectbox("Designation", ['Manager', 'Executive', 'Senior Manager', 'AVP', 'VP', 'Senior Executive', 'Junior Executive', 'President', 'Director'])
    product_pitched = st.sidebar.selectbox("Product Pitched", ['Basic', 'Deluxe', 'Standard', 'Super Deluxe', 'King'])

    passport = st.sidebar.radio("Has Passport?", [0, 1])
    own_car = st.sidebar.radio("Owns Car?", [0, 1])

    # Create a DataFrame from user inputs
    user_input_dict = {
        'Age': age,
        'MonthlyIncome': monthly_income,
        'NumberOfTrips': number_of_trips,
        'NumberOfPersonVisiting': number_of_person_visiting,
        'NumberOfChildrenVisiting': number_of_children_visiting,
        'DurationOfPitch': duration_of_pitch,
        'NumberOfFollowups': number_of_followups,
        'PitchSatisfactionScore': pitch_satisfaction_score,
        'PreferredPropertyStar': preferred_property_star,
        'TypeofContact': type_of_contact,
        'CityTier': city_tier,
        'Occupation': occupation,
        'Gender': gender,
        'MaritalStatus': marital_status,
        'Designation': designation,
        'ProductPitched': product_pitched,
        'Passport': passport,
        'OwnCar': own_car
    }

    input_df = pd.DataFrame([user_input_dict])

    # Apply one-hot encoding to categorical features, consistent with prep.py
    categorical_cols = ['TypeofContact', 'Occupation', 'Gender', 'MaritalStatus', 'Designation', 'ProductPitched']
    input_df_encoded = pd.get_dummies(input_df, columns=categorical_cols, drop_first=True)

    # Align columns with training data - this ensures all features are present and in the correct order
    # Fill missing columns (e.g., categories not present in current input) with 0
    # Drop columns that were not in the training set
    final_input_df = input_df_encoded.reindex(columns=X_train_cols, fill_value=0)

    # Make prediction
    if st.sidebar.button('Predict'):
        prediction = model.predict(final_input_df)
        prediction_proba = model.predict_proba(final_input_df)

        st.subheader("Prediction Result:")
        if prediction[0] == 1:
            st.success("The customer is likely to purchase the Wellness Tourism Package!")
        else:
            st.info("The customer is unlikely to purchase the Wellness Tourism Package.")

        st.write(f"**Probability of Purchase:** {prediction_proba[0][1]:.2f}")
        st.write(f"**Probability of No Purchase:** {prediction_proba[0][0]:.2f}")

    st.sidebar.markdown("--- Personal Information ---")
    st.sidebar.markdown("This app is for demonstration purposes only.")


if __name__ == '__main__':
    run()
