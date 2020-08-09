#!/usr/bin/python3
""" script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    cnx = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])
    cursor = cnx.cursor()
    cursor.execute(
        "select * from states where name like binary 'N%' order by id")
    lines = cursor.fetchall()
    for x in lines:
        print(x)
    cursor.close()
    cnx.close()
