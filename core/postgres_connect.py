import psycopg2


def connect():
    conn = psycopg2.connect(
        host="localhost",
        database="spotify_accounts",
        user="postgres",
        password="0000"
    )
    return conn





def create_table_and_insert_data(accounts_data):
    try:
        # Establish a connection to the PostgreSQL database
        conn = connect()

        cursor = conn.cursor()

        # Define the table creation SQL statement
        create_table_query = """
            CREATE TABLE IF NOT EXISTS accounts (
                id SERIAL PRIMARY KEY,
                gender VARCHAR(255),
                birth_year INT,
                birth_month INT,
                birth_day INT,
                password VARCHAR(255),
                username VARCHAR(255),
                email VARCHAR(255)
            )
        """
        cursor.execute(create_table_query)

        # Insert data into the table
        for item in accounts_data:
            insert_query = """
                INSERT INTO accounts (gender, birth_year, birth_month, birth_day, password, username, email)
                VALUES (%(gender)s, %(birth_year)s, %(birth_month)s, %(birth_day)s, %(password)s, %(username)s, %(email)s)
            """
            cursor.execute(insert_query, item)

        # Commit changes
        conn.commit()
        print("Table created and data inserted successfully.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()


def fetch_accounts_from_postgresql():
    accounts = None
    try:

        conn = connect()
        cursor = conn.cursor()
        select_query = """
            SELECT email, password FROM accounts
        """
        cursor.execute(select_query)
        accounts = cursor.fetchall()

        print(f'Accounts retrieved from PostgreSQL successfully.')

    except Exception as e:
        print(f'Error: {e}')

    finally:
        cursor.close()
        conn.close()

    return accounts


def remove_duplicates():


    connection = connect()
    # Create a cursor object
    cursor = connection.cursor()

    # Define the table name and the column(s) based on which you want to remove duplicates
    table_name = "accounts"
    column_name = "email"

    # SQL query to remove duplicates and keep only the row with the lowest ID
    remove_duplicates_query = f"""
        DELETE FROM {table_name} a
        WHERE a.ctid <> (
            SELECT min(b.ctid)
            FROM {table_name} b
            WHERE a.{column_name} = b.{column_name}
        );
    """

    try:
        # Execute the SQL query to remove duplicates
        cursor.execute(remove_duplicates_query)

        # Commit the changes to the database
        connection.commit()

        print("Duplicates removed successfully.")
    except Exception as e:
        # Handle any exceptions or errors
        print(f"Error: {str(e)}")
        connection.rollback()
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()


if __name__ == "__main__":
    accounts = remove_duplicates()
    print(accounts)