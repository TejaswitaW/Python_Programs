#pdbc programming creating table in oracle database
import cx_Oracle
try:
    con=cx_Oracle.connect('system/teju12345@localhost')
    query="drop table employees"
    cursor=con.cursor()
    cursor.execute(query)
    print("Table deleted successfully")
except cx_Oracle.DatabaseError as e:
    print("There is problem with db: ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
