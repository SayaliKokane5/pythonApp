import mysql.connector

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="mysql",
            user="root",
            password="rootpassword",
            database="my_database"
        )
        print("Successfully connected to the database!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    connect_to_mysql()
