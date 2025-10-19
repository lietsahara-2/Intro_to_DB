import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=" ",
    database="alx_book_store"
)

mycursor = mydb.cursor()
# Execute SQL statements using the execute() method on the cursor
mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
mydb.commit()

print("Database 'alx_book_store' created successfully!")

# Close connection to the databasse  
mycursor.close()
mydb.close()
