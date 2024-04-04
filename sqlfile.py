import mysql.connector
class sql:
    
    @staticmethod
    def add(startTime,reachTime , price):
        conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Amir1383@",
        database = "mrbilit")
        
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS mrbilit")
        cursor.execute("CREATE TABLE IF NOT EXISTS buses (startTime VARCHAR(65) , reachTime VARCHAR(65) , price VARCHAR(65))")
        insert = "INSERT INTO buses (startTime, reachTime, price) VALUES ( %s, %s, %s)"
        data = (startTime, reachTime, price)
        cursor.execute(insert, data)
        conn.commit()



        



