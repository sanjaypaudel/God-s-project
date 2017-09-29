import mysql.connector
#sudo pip3 install --egg mysql-connector-python-rf

class dbconfig:
    config={
        "host":"db.cldktu424myz.us-east-2.rds.amazonaws.com",
        "user":"root",
        "password":"GodPassword",
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

# mysql -u root -p -h db.cldktu424myz.us-east-2.rds.amazonaws.com -P 3306 translation_db
# Password: GodPassword