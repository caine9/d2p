import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                    user="root", # your username
                    passwd="yamol123", # your password
                    db="a") # name of the data base
					
cur = db.cursor() 

# Use all the SQL you like
cur.execute("insert into a values ('Pan Fu')")
cur.execute("SELECT * from a")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row[0]