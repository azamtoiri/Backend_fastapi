import psycopg2
from psycopg2.extras import RealDictCursor
import time

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='1234',
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successfully!")
        break
    except Exception as error:
        print("Connecting database failed")
        print("Error: ", error)
        time.sleep(2)
