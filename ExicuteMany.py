#pdbc programming creating table in oracle database
import cx_Oracle
try:
    con=cx_Oracle.connect('system/teju12345@localhost')
    query="insert into employees values(:eno,:ename,:esal,:eaddr)"
    records=[(100,'Tejaswita',70000,'Bengluru'),(101,'Minakshi',50000,'Pune'),(102,'Asmita',60000,'Mumbai'),(103,'Anita',70000,'Coimator'),(104,'Ankita',80000,'Mangalore')]
    cursor=con.cursor()
    cursor.executemany(query,records)
    con.commit()
    print("Data inserted successfully")
except cx_Oracle.DatabaseError as e:
    print("There is problem with db: ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
