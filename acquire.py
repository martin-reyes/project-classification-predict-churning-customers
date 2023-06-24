import pandas as pd
import env
import os

def get_connection(db, user=env.user, host=env.host, password=env.pwd):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_telco_data():
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
