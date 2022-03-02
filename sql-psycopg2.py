import psycopg2

# connect library to db
connection = psycopg2.connect(database="chinook")

# build cursor object will list the data
cursor = connection.cursor()

# QUERY 1
# cursor.execute('SELECT * FROM "Artist"')

# QUERY 2
# cursor.execute('SELECT "Name" FROM "Artist"')

# QUERY 3
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# QUERY 4
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# retreive data using fetchall() to retreve multiple records
results = cursor.fetchall()

# retreive data using fetchall() to retreve multiple records
# results = cursor.fetchone()

# end connection
connection.close()

# iterate through data
for result in results:
    print(result)
