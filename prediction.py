import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

# Load the trained model
model = joblib.load('model/attrition_model.joblib')
data = joblib.load('model/data.joblib')
X = joblib.load('model/X.joblib')

# Data inputan untuk prediksi (ganti dengan data baru Anda)
new_data = pd.DataFrame({
    'Age': [30],
    'BusinessTravel': ['Travel_Rarely'],
    'Department': ['Sales'],
    'EducationField': ['Life Sciences'],
    'EnvironmentSatisfaction': [3],
    'Gender': ['Male'],
    'JobInvolvement': [3],
    'JobLevel': [2],
    'JobRole': ['Sales Executive'],
    'MaritalStatus': ['Single'],
    'MonthlyIncome': [5000],
    'OverTime': ['Yes'],
    'StockOptionLevel': [0],
    'TotalWorkingYears': [5],
    'YearsAtCompany': [2],
    'YearsInCurrentRole': [2],
    'YearsWithCurrManager': [1]
})

# Langkah-langkah praproses
categorical_cols = new_data.select_dtypes(include='object').columns
for col in categorical_cols:
    le = LabelEncoder()
    # Sesuaikan encoder label pada kategori data pelatihan asli
    le.fit(data[col]) # Menggunakan data pelatihan asli untuk pemetaan
    new_data[col] = le.transform(new_data[col])

scaler = StandardScaler()
# Sesuaikan scaler pada data pelatihan asli
scaler.fit(X) # Menggunakan data pelatihan asli untuk penskalaan
X_scaled_new = scaler.transform(new_data)

# Membuat prediksi
prediction = model.predict(X_scaled_new)

# Menafsirkan prediksi
if prediction[0] == 1:
    print('Prediction: Attrition')
else:
    print('Prediction: No Attrition')