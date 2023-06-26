import pandas as pd
import env
import os

def get_connection(db, user=env.user, host=env.host, password=env.pwd):
    '''
    env.py file must hold 3 variables that hold MySQL credentials: user, host, and pwd
    Returns string of the MySQL connection required for pandas read_sql method
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_telco_data():
    '''
    If the csv file exists, it is read and returned as a pandas DataFrame
    If not, pandas reads in a SQL query that acquires telco customer data from a MySQL database.
    The query is stored into a DataFrame, saved, and returned.
    '''
    filename = "data/telco_churn_raw.csv"

    # Read the csv file if it exists
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # Fead the SQL query into a dataframe
        df = pd.read_sql('''SELECT * 
                            FROM customers
                             JOIN contract_types USING (contract_type_id)
                             JOIN internet_service_types USING (internet_service_type_id)
                             JOIN payment_types USING (payment_type_id)''',
                         get_connection('telco_churn'))
        # Write that DataFrame for prep
        df.to_csv(filename, index=False)
        # Return the DataFrame
        return df
