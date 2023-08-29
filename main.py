# This entrypoint file to be used in development. Start by reading README.md
import pandas as pd
import demographic_data_analyzer
from unittest import main


data = {
    'age': [39, 50, 38, 53, 28],
    'workclass': ['State-gov', 'Self-emp-not-inc', 'Private', 'Private', 'Private'],
    'fnlwgt': [77516, 83311, 215646, 234721, 338409],
    'education': ['Bachelors', 'Bachelors', 'HS-grad', '11th', 'Bachelors'],
    'education-num': [13, 13, 9, 7, 13],
    'marital-status': ['Never-married', 'Married-civ-spouse', 'Divorced', 'Married-civ-spouse', 'Married-civ-spouse'],
    'occupation': ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Handlers-cleaners', 'Prof-specialty'],
    'relationship': ['Not-in-family', 'Husband', 'Not-in-family', 'Husband', 'Wife'],
    'race': ['White', 'White', 'White', 'Black', 'Black'],
    'sex': ['Male', 'Male', 'Male', 'Male', 'Female'],
    'capital-gain': [2174, 0, 0, 0, 0],
    'capital-loss': [0, 0, 0, 0, 0],
    'hours-per-week': [40, 13, 40, 40, 40],
    'native-country': ['United-States', 'United-States', 'United-States', 'United-States', 'Cuba'],
    'salary': ['<=50K', '<=50K', '<=50K', '<=50K', '<=50K']
}

df = pd.DataFrame(data)

race_count = df['race'].value_counts()
average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
percentage_bachelors = round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)
print("Percentage Bachelors:", percentage_bachelors)

higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
higher_education_rich = round((df[(higher_education) & (df['salary'] == '>50K')].shape[0] / df[higher_education].shape[0]) * 100, 1)

lower_education = ~higher_education
lower_education_rich = round((df[(lower_education) & (df['salary'] == '>50K')].shape[0] / df[lower_education].shape[0]) * 100, 1)

min_work_hours = df['hours-per-week'].min()

num_min_workers_rich = df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].shape[0]
percentage_min_workers_rich = (num_min_workers_rich / df[df['hours-per-week'] == min_work_hours].shape[0]) * 100

# Verifica si hay registros con salario '>50K' antes de calcular el país con el porcentaje más alto
if df[df['salary'] == '>50K']['native-country'].value_counts().any():
    highest_earning_country = ((df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()) * 100).idxmax()
else:
    highest_earning_country = None

# Luego, verifica si highest_earning_country es None antes de intentar calcular el highest_earning_country_percentage
if highest_earning_country and df[df['native-country'] == highest_earning_country].shape[0] != 0:
    highest_earning_country_percentage = round((df[(df['native-country'] == highest_earning_country) & (df['salary'] == '>50K')].shape[0] / df[df['native-country'] == highest_earning_country].shape[0]) * 100, 1)
else:
    highest_earning_country_percentage = 0


indian_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
if not indian_rich.empty:
    top_IN_occupation = indian_rich['occupation'].value_counts().idxmax()
else:
    top_IN_occupation = "No data available"

print(race_count)
print(average_age_men)
print(percentage_bachelors)
print(higher_education_rich)
print(lower_education_rich)
print(min_work_hours)
print(percentage_min_workers_rich)
print(highest_earning_country, highest_earning_country_percentage)
print(top_IN_occupation)

# Test your function by calling it here
demographic_data_analyzer.calculate_demographic_data()

# Run unit tests automatically
main(module='test_module', exit=False)
