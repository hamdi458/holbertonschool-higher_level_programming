#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    cnx = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])
    cursor = cnx.cursor()
    cursor.execute("select cities.name from cities join states on\
                 cities.state_id = states.id WHERE states.name \
                 like '{}' order by cities.id".format(argv[4]))
    lines = cursor.fetchall()
    print(", ".join(x[0] for x in lines))
    cursor.close()
