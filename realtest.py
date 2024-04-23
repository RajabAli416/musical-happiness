import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host='45.76.8.111',
    user='karama_stag_r',
    password='hfppr-4$working4Cooper',
    database='karama_staging'
)

# Initialize an empty dictionary to store column names for each table
table_column_names = {}

# Execute SQL queries and fetch data for both tables
tables = ['family_details', 'caregiver_details']

for table in tables:
    cursor = conn.cursor()
    query = f"SHOW COLUMNS FROM {table};"
    cursor.execute(query)

    # Fetch all rows
    data = cursor.fetchall()

    # Close cursor
    cursor.close()

    # Extract column names for the current table
    column_names = [column[0] for column in data]

    # Store column names in the dictionary
    table_column_names[table] = column_names

# Print column names for both tables
for table, column_names in table_column_names.items():
    print(f"Column names for {table}: {column_names}")

# Close the connection
conn.close()
