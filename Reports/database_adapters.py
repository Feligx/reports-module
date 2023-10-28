from Reports.database_clients import SQLClient, NoSQLClient
from Reports.database_services import Service


class Adapter:
    adapted: Service

    def insert(self):
        ...

    def update(self):
        ...

    def get(self):
        ...


class SQLAdapter(SQLClient, Adapter):
    ...


class NoSQLAdapter(NoSQLClient, Adapter):
    ...
