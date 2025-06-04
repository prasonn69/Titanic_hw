import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

@st.cache_data
def load_and_train_model():
    try:
        df = pd.read_csv('/Users/prason/Downloads/titanic.csv')
        
        df['Sex'] = df['Sex'].map({'female': 0, 'male': 1})
        df['Age'].fillna(df['Age'].median(), inplace=True)
        df['Fare'].fillna(df['Fare'].median(), inplace=True)
        
        features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
        X = df[features]
        y = df['Survived']
        
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X, y)
        
        return model, "Model trained successfully!"
    except FileNotFoundError:
        return None, "CSV file not found at the specified path."
    except Exception as e:
        return None, f"Error loading data: {str(e)}"

model, status = load_and_train_model()

st.title("Titanic Survival Predictor")
st.write("Predict if a passenger would survive the Titanic disaster")

if model is None:
    st.error(status)
    st.stop()
else:
    st.success(status)

pclass = st.selectbox("Passenger Class:", [1, 2, 3])
sex = st.radio("Gender:", ["Female", "Male"])
age = st.number_input("Age:", min_value=0, max_value=100, value=30)
siblings = st.number_input("Siblings/Spouses:", min_value=0, value=0)
parents = st.number_input("Parents/Children:", min_value=0, value=0)
fare = st.number_input("Fare:", min_value=0.0, value=32.0)

gender_num = 0 if sex == "Female" else 1

if st.button("Predict Survival"):
    data = [[pclass, gender_num, age, siblings, parents, fare]]
    prediction = model.predict(data)[0]
    
    if prediction == 1:
        st.success("Passenger would have SURVIVED!")
    else:
        st.error("Passenger would NOT have survived")