import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    
    # Removing duplicates
    df.drop_duplicates(inplace=True)
    
    # Handling missing values
    df.fillna(method='ffill', inplace=True)
    
    # Standardizing column names
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    # Save cleaned data
    df.to_csv('data/cleaned/cleaned_data.csv', index=False)
    
clean_data('data/raw/raw_data.csv')
