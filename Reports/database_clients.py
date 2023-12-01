from Reports.database_adapters import SQLAdapter, NoSQLAdapter


class SQLClient:
    SQLSession: SQLAdapter = SQLAdapter()

    def get_report(self, id):
        return self.SQLSession.get(id)

    def insert_report(self, data):
        try:
            self.SQLSession.insert(data)
            return True
        except Exception as e:
            return False

    def update_report(self, id, data):
        try:
            self.SQLSession.update(id, data)
            return True
        except Exception as e:
            return False


class NoSQLClient:
    NoSQLSession: NoSQLAdapter = NoSQLAdapter()

    def get_form_metadata(self):
        return self.NoSQLSession.get()
