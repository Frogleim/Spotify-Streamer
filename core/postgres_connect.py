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
        conn = connect()
        cursor = conn.cursor()
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
        for item in accounts_data:
            insert_query = """
                INSERT INTO accounts (gender, birth_year, birth_month, birth_day, password, username, email)
                VALUES (%(gender)s, %(birth_year)s, %(birth_month)s, %(birth_day)s, %(password)s, %(username)s, %(email)s)
            """
            cursor.execute(insert_query, item)
        conn.commit()
        print("Table created and data inserted successfully.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
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
    cursor = connection.cursor()
    table_name = "accounts"
    column_name = "email"
    remove_duplicates_query = f"""
        DELETE FROM {table_name} a
        WHERE a.ctid <> (
            SELECT min(b.ctid)
            FROM {table_name} b
            WHERE a.{column_name} = b.{column_name}
        );
    """

    try:
        cursor.execute(remove_duplicates_query)
        connection.commit()
        print("Duplicates removed successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    remove_duplicates()
