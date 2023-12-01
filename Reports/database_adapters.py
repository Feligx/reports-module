from Reports.database_services import Service, MongoService, SQLiteService


class Adapter:
    adapted: Service

    def insert(self, data):
        ...

    def update(self, id, data):
        ...

    def get(self, id):
        ...


class SQLAdapter(Adapter):
    adapted = SQLiteService()

    def insert(self, data):
        return self.adapted.insert(data)

    def update(self, id, data):
        return self.adapted.update(id, data)

    def get(self, id):
        return self.adapted.get(id)



class NoSQLAdapter(Adapter):

    adapted = MongoService()

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
