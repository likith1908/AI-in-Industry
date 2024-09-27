import psycopg2
from psycopg2 import sql


db_params = {
    'dbname': 'sensordata',
    'user': 'likith',      
    'password': '1234',  
    'host': '15.206.164.185',  
    'port': '5432'           
}

try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    print("Database connection established.")

    create_table_query = """
    CREATE TABLE IF NOT EXISTS weather_data (
        id SERIAL PRIMARY KEY,
        timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
        temperature_value FLOAT,
        humidity_value FLOAT
    );
    """
    cursor.execute(create_table_query)
    print("Table created successfully.")

    insert_data_query = """
    INSERT INTO weather_data (temperature_value, humidity_value)
    VALUES (%s, %s);
    """
    data_to_insert = (25.5, 60.5)
    cursor.execute(insert_data_query, data_to_insert)
    conn.commit() 
    print("Data inserted successfully.")

except Exception as error:
    print(f"Error: {error}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("Database connection closed.")
