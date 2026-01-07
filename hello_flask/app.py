import os
from flask import Flask
import MySQLdb
import time

app = Flask(__name__)

def get_db_connection():
    # Retry until MySQL is ready
    for _ in range(10):
        try:
            return MySQLdb.connect(
                host=os.getenv("MYSQL_HOST", "mysql_db"),
                user=os.getenv("MYSQL_USER", "myuser"),
                passwd=os.getenv("MYSQL_PASSWORD", "mypassword"),
                db=os.getenv("MYSQL_DATABASE", "mydatabase")
            )
        except MySQLdb.OperationalError:
            time.sleep(2)
    raise Exception("Could not connect to MySQL")

@app.route("/")
def hello_world():
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()
    db.close()
    return f"Hello, World! MySQL version: {version[0]}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

    
