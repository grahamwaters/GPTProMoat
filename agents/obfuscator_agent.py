# Step 1: Import the necessary libraries
import pandas as pd
from faker import Faker
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder

# Step 2: Load the input data into a Pandas DataFrame
df = pd.read_csv('input_data.csv')

# Step 3: Define a function to classify each column's data type
def classify_data_type(column):
    if column.dtype == 'object':
        if len(column.unique()) < len(column)/2:
            return 'categorical'
        else:
            try:
                column.astype(float)
                return 'numeric'
            except ValueError:
                try:
                    column.astype(int)
                    return 'ordinal'
                except ValueError:
                    if column.str.contains('^[a-zA-Z]+\s\d+').any():
                        return 'physical address'
                    elif column.str.contains('^[a-zA-Z]+\s[a-zA-Z]+').any():
                        return 'name'
                    elif column.str.contains('^[0-9]{3}-[0-9]{2}-[0-9]{4}$').any():
                        return 'SSN'
                    elif column.str.contains('^[0-9]{3}-[0-9]{2}-[0-9]{4}$').any():
                        return 'phone number'
                    else:
                        return 'text'
    else:
        return 'numeric'

# Step 4: Apply the function to each column in the DataFrame and store the results in a dictionary
column_types = {}
for column in df.columns:
    column_types[column] = classify_data_type(df[column])

# Step 5: Create a new DataFrame with obfuscated data using the Faker() package
fake = Faker()
obfuscated_data = pd.DataFrame(columns=df.columns)
for column in df.columns:
    if column_types[column] == 'categorical':
        le = LabelEncoder()
        obfuscated_data[column] = le.fit_transform(df[column])
    elif column_types[column] == 'numeric' or column_types[column] == 'ordinal':
        obfuscated_data[column] = df[column] + fake.random_int(min=1, max=100)
    elif column_types[column] == 'text':
        cv = CountVectorizer()
        obfuscated_data[column] = cv.fit_transform(df[column]).toarray()
    else:
        obfuscated_data[column] = df[column].apply(lambda x: fake.address() if 'address' in column_types[column] else fake.name())

# Step 6: Export the obfuscated data to a new CSV file
obfuscated_data.to_csv('obfuscated_data.csv', index=False)
