import acquire as a
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import os


def identify_cols_with_white_space(df):
    '''
    Takes in a DataFrame
    Prints columns with any values that are whitespace
    Returns columns in a list
    '''
    
    cols_w_white_space = []
    
    for col in df.columns:
        # check string/object columns
        if df[col].dtype == 'O':
            # check for any values in the column that are empty or whitespace
            is_whitespace = df[col].str.isspace()
            has_whitespace = is_whitespace.any()
            if has_whitespace:
                print(f'{col} has whitespace')
                cols_w_white_space.append(col)
    return cols_w_white_space


def prep_telco(telco_raw=a.get_telco_data()):
    '''
    Accepts the raw telco data
    Returns the data with the transformations above applied
    '''
    filename = "data/telco_churn_prep.csv"
    
    # read and return prepped_data if file exists
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    else:
        # drop foreign keys
        telco = telco_raw.iloc[:,3:]

        # replace empty space with np.nan and convert column to float
        telco['total_charges'] = telco['total_charges'].replace(' ', np.nan).astype(float)
        # impute median
        telco['total_charges'] = telco['total_charges'].fillna(telco['total_charges'].median())

        # encode binary variables
        binary_cols = ['partner','dependents','phone_service', 'paperless_billing', 'churn']
        for col in binary_cols:
            telco[col] = telco[col].replace({'Yes': 1, 'No': 0})

        telco['gender'] = telco['gender'].replace({'Male': 1, 'Female': 0})

        # encode multiclass variables
        dummy_df = pd.get_dummies(telco[['multiple_lines', 'online_security',
                                               'online_backup', 'device_protection', 
                                               'tech_support', 'streaming_tv', 
                                               'streaming_movies', 'contract_type',
                                               'internet_service_type', 'payment_type']],
                                    dummy_na=False, drop_first=True)
        telco_clean = pd.concat([telco, dummy_df], axis=1)

        # rename columns to be lowercased with underscores
        telco_clean.columns = [col.lower().replace(" ", "_") for col in telco_clean.columns]
        # rename gender column to gender_male
        telco_clean = telco_clean.rename(columns={'gender':'gender_male'})
        
        # Write the clean DataFrame for exploration and modeling
        telco_clean.to_csv(filename, index=False)    
        
        return telco_clean


def split_data(df, test_size=.15, validate_size=.15, stratify_col=None, random_state=None):
    '''
    Takes in a DataFrame, desired test and validate sizes, an optional column to stratify on and a random state;
    Returns train, validate, and test DataFrames.
    '''
    # no stratification
    if stratify_col == None:
        # split test data
        train_validate, test = train_test_split(df, test_size=test_size, random_state=random_state)
        # split validate data
        train, validate = train_test_split(train_validate, test_size=validate_size/(1-test_size),
                                                                           random_state=random_state)
    # stratify split
    else:
        # split test data
        train_validate, test = train_test_split(df, test_size=test_size,
                                                random_state=random_state, stratify=df[stratify_col])
        # split validate data
        train, validate = train_test_split(train_validate, test_size=validate_size/(1-test_size),
                                           random_state=random_state, stratify=train_validate[stratify_col])       
    return train, validate, test

