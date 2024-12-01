from sqlalchemy import create_engine

# Replace with your actual connection string
DATABASE_URL = "postgresql://dhanush12:1234@localhost/dhanush_db"


def test_sqlalchemy_connection():
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        print("Connection successful!")
        connection.close()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_sqlalchemy_connection()
