import pandas as pd
import datetime as dt
import uuid
import numpy as np

# Step 1 Load data into python 
df = pd.read_csv("data/School_Learning_Modalities (1).csv")
# Step 2 Print the counts of columns and rows 
print(df.shape)
# Step 3 Provide a print out of the column names 
print(df.columns)
# Step 4 Clean the column names 
# Step 5 Clean the strings that might exist within each column 
df.rename(columns={'District NCES ID' :' district_nes_id','District Name': 'district_name','Learning Modality': 'learning_modality', 'Operational Schools': 'operational_schools', 'Student Count': 'student_count', 'ZIP Code':'zip_code', 'City' : 'city', 'State':'state', 'Week':'week'}, inplace=True)
print(df.columns)
# Step 6 Assess white space or special characters 
# Step 7 Convert the column types to the correct types 
print(df.dtypes)
# Step 8 Remove any duplicate rows 
print(len(df[df.duplicated()])) # checking if duplicates
# Step 9 Assess any missing values per column 
print(df[df.isnull().any(axis=1)])
print(df.loc[:, df.isnull().any()])
df.fillna(value=0, inplace=True)
print(df[df.isnull().any(axis=1)])
# Step 10 Create modality_inperson
def label_modality_ineperson(row):
    if row['learning_modality'] == 'In Person':
        return True
    if row['learning_modality'] == 'Remote':
        return False
    if row['learning_modality'] == 'Hybrid':
        return False
df['modality_inperson']=df.apply (lambda row: label_modality_ineperson(row),axis =1)
print(df.columns)
print(df['modality_inperson'])
