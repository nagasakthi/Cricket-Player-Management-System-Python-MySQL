import pymysql


def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="S.naga@123",
        database="cricket"
    )