from Reports.database_services import Service


class SQLClient:
    adapted: Service
    def __init__(self):
        ...

    def connect(self):
        ...

    def get_session(self):
        ...

    def get_report(self):
        ...

    def insert_report(self):
        ...

    def update_report(self):
        ...


class NoSQLClient:
    adapted: Service
    def __init__(self):
        ...

    def connect(self):
        ...

    def get_session(self):
        ...

    def get_form_metadata(self):
        ...
