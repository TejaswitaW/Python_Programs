#inserting multiple data in database
import cx_Oracle
con=cx_Oracle.connect('system/teju12345@localhost')
cursor=con.cursor()
try:
    while True:
        eno=int(input("Enter employee number"))
        ename=input("Enter employee name")
        esal=int(input("Enter employee salary"))
        eadd=input("Enter employee address")
        query= "insert into employees values(%d,'%s',%f,'%s')"
        cursor.execute(query %(eno,ename,esal,eadd))
        con.commit()
        print("Information inserted successfully")
        a=input("Do you want to continue,please enter yes or no")
        if a=='no':
            break;
except cx_Oracle.DatabaseError as e:
    print("There is problem in db:",e)
finally:
    if cursor:
          cursor.close()
    if con:
          con.close()
        
