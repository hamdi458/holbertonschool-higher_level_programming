#!/usr/bin/python3
""" script that takes in an argument and displays all values """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    cnx = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])
    cursor = cnx.cursor()
    cursor.execute(
        "select cities.id ,cities.name,states.name FROM cities join states \
     on states.id = cities.state_id")
    lines = cursor.fetchall()
    for i in lines:
        print(i)
    cursor.close()
    cnx.close()
