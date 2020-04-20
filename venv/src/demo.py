import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user = "",
                                  password = "",
                                  host = "cs645db.cs.umass.edu",
                                  port = "7645",
                                  database = "")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
    #closing database connection.
