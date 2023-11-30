from Reports.database_clients import SQLClient, NoSQLClient
from Reports.database_services import Service


class Adapter:
    adapted: Service

    def insert(self, data):
        ...

    def update(self, id, data):
        ...

    def get(self, id):
        ...


class SQLAdapter(SQLClient, Adapter):

    def insert(self, data):
        return self.adapted.insert(data)

    def update(self, id, data):
        return self.adapted.update(id, data)

    def get(self, id):
        return self.adapted.get(id)


class NoSQLAdapter(NoSQLClient, Adapter):

    def insert(self, data):
        return self.adapted.insert(
            {
                "_id": "123456789",
                "name": "test",
                "age": 20,
                "city": "New York"
            }
        )

    def update(self, id, data):
        return self.adapted.update(
            id,
            data
        )

    def get(self, id =""):
        return self.adapted.get()
