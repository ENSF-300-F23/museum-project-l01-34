import mysql.connector
from menu import *
from operation import *

#passwrd = input("Enter Password:\n")

cnx = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "803134001",
    database = "ARTOBJECT"
)

curr = cnx.cursor(buffered=True)

operations[menu()](curr)

cnx.commit()
cnx.close()