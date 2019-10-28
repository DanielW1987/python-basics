import mysql.connector

# connect to database
connection = mysql.connector.connect(host='localhost',
                                     port='3306',
                                     database='db',
                                     user='root',
                                     password='')

# test if connection is established
if connection.is_connected():
    print("Connected to mysql database")

    # execute SELECT statement
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM releases")

    # fetch one record at a time
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()

    cursor.close()

    # fetch all records
    cursor2 = connection.cursor()
    cursor2.execute("SELECT * FROM releases")
    rows = cursor2.fetchall()
    print("Rowcount is {}".format(cursor2.rowcount))
    cursor2.close()

    # execute CREATE statement
    cursor3 = connection.cursor()
    try:
        cursor3.execute("INSERT INTO releases(artist, album_title, state) values('Test', 'Test', 'NOT_SET')")
        connection.commit()
        print("Record inserted")
    except:
        connection.rollback()
    finally:
        cursor3.close()

    # execute DELETE statement
    cursor4 = connection.cursor()
    delete_statement: str = "DELETE FROM releases WHERE artist = '%s' AND album_title = '%s'"
    args = ('Test', 'Test')
    try:
        cursor4.execute(delete_statement % args)
        connection.commit()
        print("{} test record(s) deleted".format(cursor4.rowcount))
    except:
        connection.rollback()
    finally:
        cursor4.close()

# close connection
connection.close()
