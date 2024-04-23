import mysql.connector
import pandas as pd

config = {
    'user': 'karama_stag_r',
    'password': 'hfppr-4$working4Cooper',
    'host': '45.76.8.111',
    'database': 'karama_staging',
    'raise_on_warnings': True
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

cursor.execute('SELECT * FROM family_details')
family_data = cursor.fetchall()
family_columns = [i[0] for i in cursor.description]

cursor.execute('SELECT * FROM caregiver_details')
caregiver_data = cursor.fetchall()
caregiver_columns = [i[0] for i in cursor.description]

cnx.close()

family_df = pd.DataFrame(family_data, columns=family_columns)
caregiver_df = pd.DataFrame(caregiver_data, columns=caregiver_columns)

family_df.to_csv('family_details.csv', index=False)
caregiver_df.to_csv('caregiver_details.csv', index=False)

