from Reports.database_adapters import SQLAdapter, NoSQLAdapter


class SQLClient:
    SQLSession: SQLAdapter = SQLAdapter()

    def get_report(self, id):
        self.SQLSession.get(id)

    def insert_report(self, data):
        self.SQLSession.insert(data)

    def update_report(self, id, data):
        self.SQLSession.update(id, data)


class NoSQLClient:
    NoSQLSession: NoSQLAdapter = NoSQLAdapter()

    def get_form_metadata(self):
        return self.NoSQLSession.get()
