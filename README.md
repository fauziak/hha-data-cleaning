# Step 1 Loading the data into python using df=pd.read_csv function and grabbing the data from the subdata folder that was created.


# Step 2 Printing out the total counts of columns and rows using df.shape.


# Step 3 Printing out the column names using df.columns


# Step 4,5,6 Cleaning out the column names, column strings, and assessing white spaces or special characters within each column using df.rename


# Step 7 Confirming that all the columns have correct data types using df.dtypes.Since all the columns have the correct data types no additional work was needed.


# Step 8 Using df.duplicated to check if there are any duplicate rows.There are no duplicate rows so no additional work was needed.


# Step 9 Assessed any missing values by using df.isnull. Finding out the columns that have null on line 23. Student count was the only column that had null, so filled it in with the vlaue of 0 using df.fillna.Confirming null values again by using isnull.


# Step 10 Creating a new column named moadlity_inperson by df.apply that calls a helper function named label_modalityinperson. label_modality_inperson returns true if learning_modality is in person. label_modality_inperson returns false if leanrning_moadlity is remote or hybrid.confrimed new column was created by printing df.columns, confirmed new value for modality_inperson was added to the rows.