import mysql.connector
class dbconfig:
    config={
        "host":"localhost",
        "user":"root",
        "password":"root",
        "database":"translation_db"
        }

    def __init__(self):
        self.db = mysql.connector.connect(**self.config)
        self.cursor = self.db.cursor(buffered=True)

    def __enter__(self):
        return dbconfig()

    def __exit__(self):
        if self.db:
            self.db.close()