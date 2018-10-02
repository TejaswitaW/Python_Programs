#pdbc programming creating table in oracle database
import cx_Oracle
try:
    con=cx_Oracle.connect('system/teju12345@localhost')
    query="create table employees(eno number,ename varchar2(10),esal number(10,2),eaddr varchar2(10))"
    cursor=con.cursor()
    cursor.execute(query)
    print("Table created successfully")
except cx_Oracle.DatabaseError as e:
    print("There is problem with db: ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()



