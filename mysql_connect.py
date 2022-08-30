import mysql.connector
from mysql.connector import Error
 
 
def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(database='sahanum',host='localhost',port='124',
                                       user='root',
                                       password='saha',charset='utf8mb4')
        if conn.is_connected():
            print('Connected to MySQL database')
        cursor = conn.cursor()
        cursor.execute('select product,kiloprice from productdb')
        for row in cursor.fetchall():
            print("{0:10} {1:8} \n".format(row[0],row[1]))
            #t +=row[2]
        #cursor.execute("SHOW DATABASES")
        #cursor.execute("ALTER TABLE numbers CHANGE COLUMN numintamil numintamil NVARCHAR(255) CHARACTER SET utf8mb3 NULL DEFAULT NULL ")
        #cursor.execute('commit')
        print('done')
                       
        
        
 
    except Error as e:
        print(e)
 
    #finally:
        cursor.close()
        conn.close()
 
 
if __name__ == '__main__':
    connect()

