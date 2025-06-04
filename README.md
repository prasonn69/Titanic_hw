# Titanic Survival Predictor

A simple Streamlit web application that predicts whether a passenger would have survived the Titanic disaster based on their characteristics.

## Features

- Interactive web interface built with Streamlit
- Machine learning prediction using Random Forest classifier
- Automatic model training from CSV data
- Real-time predictions based on passenger information

## Requirements

- Python 3.7+
- streamlit
- pandas
- scikit-learn
- numpy

## Installation

1. Clone or download this repository
2. Install the required packages:
```bash
pip install streamlit pandas scikit-learn numpy
```

## Usage

1. Make sure you have the Titanic dataset CSV file
2. Update the file path in the code to point to your CSV file:
```python
df = pd.read_csv('/path/to/your/titanic.csv')
```
3. Run the Streamlit app:
```bash
streamlit run titanic_predictor.py
```
4. Open your web browser and go to the displayed URL (usually http://localhost:8501)

## How to Use the App

1. Enter passenger information:
   - **Passenger Class**: 1 (First), 2 (Second), or 3 (Third)
   - **Gender**: Female or Male
   - **Age**: Age in years
   - **Siblings/Spouses**: Number of siblings or spouses aboard
   - **Parents/Children**: Number of parents or children aboard
   - **Fare**: Ticket price paid

2. Click "Predict Survival" to get the prediction

## Dataset

The app expects a Titanic dataset CSV file with the following columns:
- `Pclass`: Passenger class (1, 2, 3)
- `Sex`: Gender (male, female)
- `Age`: Age in years
- `SibSp`: Number of siblings/spouses aboard
- `Parch`: Number of parents/children aboard
- `Fare`: Passenger fare
- `Survived`: Survival status (0 = No, 1 = Yes) - target variable

## Model

The application uses a Random Forest classifier with 100 estimators. The model:
- Automatically handles missing values by filling with median values
- Maps gender from text to numeric values (female=0, male=1)
- Uses 6 features for prediction
- Is cached for better performance

## File Structure

```
titanic-predictor/
│
├── titanic_predictor.py    # Main Streamlit application
├── README.md              # This file
└── titanic.csv           # Dataset (not included)
```

## Notes

- The model trains automatically when the app starts for the first time
- Training data is cached to improve performance on subsequent runs
- Make sure your CSV file path is correct in the code
- The app will show an error message if the CSV file is not found
