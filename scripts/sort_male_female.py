import pandas as pd

""" 
This script take the original cleaned table and remove rows with 'Total' in the Sex column.
"""

sort_sex = ["Male", "Female"]

data_raw = pd.read_excel('average_monthly_earnings_by_sex_and_occupation_cleaned_table.xlsx')

data_male_female = data_raw[data_raw['Sex'].isin(sort_sex)]

data_male_female.to_excel('average_monthly_earnings_by_sex_and_occupation_male_female.xlsx')
