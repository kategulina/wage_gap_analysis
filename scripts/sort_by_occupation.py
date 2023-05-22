import pandas as pd

""" 
This script takes the cleaned table and remove all rows in Occupation and remove rows except rows with value Total.
"""

sort_method_occupation = ["Total"]

data = pd.read_excel('average_monthly_earnings_by_sex_and_occupation_cleaned_table.xlsx')

data2 = data[data['Occupation'].isin(sort_method_occupation)]

data2.to_excel('average_monthly_earnings_by_sex_and_occupation_is_total.xlsx')
