from pymysql import connect, Error
import dbconfig


class DBHelper:

    def connect(self, database='crime_map'):
        return connect(
            host='localhost',
            user='root',
            password=dbconfig.password,
            db=database
        )

    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(e)
        finally:
            connection.close()

    def add_input(self, data):
        connection = self.connect()
        try:
            query = """
            INSERT INTO crimes
            (description)
            VALUES (%s);
            """
            with connection.cursor() as cursor:
                cursor.execute(query, data)
                connection.commit()
        except Error as e:
            print(e)
        finally:
            connection.close()

    def clear_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        except Error as e:
            print(e)
        finally:
            connection.close()