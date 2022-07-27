from pymysql import connect, Error
import dbconfig

try:
    with connect(
        host='localhost',
        user='root',
        password=dbconfig.password
    ) as connection:
        create_db_query = "CREATE DATABASE crimemap"
        create_table_query = """CREATE TABLE crimemap.crimes (
            id INT AUTO_INCREMENT PRIMARY_KEY,
            latitude FLOAT(10,6),
            longitude FLOAT(10,6),
            date DATETIME,
            category VARCHAR(50),
            description VARCHAR(1000),
            updated_at TIMESTAMP,
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
            cursor.execute(create_table_query)
            connection.commit()
finally:
    connection.close()

