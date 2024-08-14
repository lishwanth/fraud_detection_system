from .db_connection import DatabaseConnection

class DatabaseOperations:
    def __init__(self, connection):
        self.connection = connection

    def create_table(self, table_name, schema):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({schema});"
        self.connection.cursor.execute(query)
        self.connection.connection.commit()

    def insert_data(self, table_name, data):
        columns = ', '.join(data.keys())
        values = ', '.join([f"'{v}'" for v in data.values()])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
        self.connection.cursor.execute(query)
        self.connection.connection.commit()

    def fetch_data(self, query):
        self.connection.cursor.execute(query)
        return self.connection.cursor.fetchall()

if __name__ == "__main__":
    connection = DatabaseConnection('fraud_db', 'user', 'password', 'localhost', '5432')
    db_operations = DatabaseOperations(connection)

    schema = "id SERIAL PRIMARY KEY, amount FLOAT, label INT"
    db_operations.create_table('fraud_transactions', schema)
    connection.close()
