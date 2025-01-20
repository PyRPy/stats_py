import sqlite3 

try:
    connection = sqlite3.connect("C:/Users/me/Downloads/sklearn/pandas_sql/simple_tables.db")
    print("connected to database sucessfully.")

    cursor = connection.cursor() 
    cursor.execute("select * from table1")
    rows = cursor.fetchall() 

    for row in rows:
        print(row) 

except sqlite3.Error as e: 
    print(f"An error occurred: {e}")

finally:
    if connection:
        connection.close() 