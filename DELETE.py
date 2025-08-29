import mysql.connector as m
print("""DELETE OPERATION!!!!!!
1)DELETE DATABASE-1
NOTE: DATABASES LIKE "PERFORMANCE_SCHEMA",
"MYSQL",
"INFORMATION_SCHEMA"
CANNOT BE DELETED AS IT IS PART
OF MYSQL
2)DELETE TABLE-2
3)DELETE TABLE RECORDS-3
4)DELETE RECORD ELEMENT-4""")
def database():
        con=m.connect(host="localhost", user="root", password="12345")
        cur=con.cursor()
        cd="Y"
        while cd=="y" or cd=="Y":
                      cur.execute("SHOW DATABASES")
                      data=[db[0] for db in cur.fetchall()]
                      print("AVAILABLE DATABASES:", *data, sep="\n")
                      seldb=input("ENTER THE SELECTED DB_NAME TO DELETE IT: ")
                      con=m.connect(host="localhost", user="root", password="12345",database=f"{seldb}")
                      cur=con.cursor()
                      if seldb.lower() in data:
                              cur.execute(f"DROP DATABASE IF EXISTS {seldb}")
                              con.commit()
                              print("SUCCESSFULLY DELETED!!!!")
                              cd=input("DO YOU WANT TO DELETE MORE(Y/N):")
                      else:
                              print("DATABASE DOES'NT EXISTS!!!")
def table():
        con=m.connect(host="localhost", user="root", password="12345")
        cur=con.cursor()
        cur.execute("SHOW DATABASES")
        data=[db[0] for db in cur.fetchall()]
        print("AVAILABLE DATABASES:", *data, sep="\n")
        seldb=input("ENTER THE SELECTED DB_NAME: ")
        if seldb.lower() in data:
                con=m.connect(host="localhost", user="root", password="12345",database=f"{seldb}")
                cur=con.cursor()
                cur.execute("SHOW TABLES")
                data1=[df[0] for df in cur.fetchall()]
                print("AVAILABLE TABLES:", *data1, sep="\n")
                tblna=input("ENTER THE TABLE NAME:")
                if tblna.lower() in data1:
                        cur.execute(f"DROP TABLE IF EXISTS {tblna}")
                        con.commit()
                        print("TABLE SUCESSFULLY DELETED!!!")
                        cd=input("DO YOU WANT TO DELETE MORE(Y/N):")
                else:
                        print("TABLE DOES'NT EXISTS!!!")
        else:
                print("DATABASE DOES'NT EXISTS!!!")
def records():
        con=m.connect(host="localhost", user="root", password="12345")
        cur=con.cursor()
        cd="y"
        while cd=="Y" or cd=="y":
                cur.execute("SHOW DATABASES")
                data=[db[0] for db in cur.fetchall()]
                print("AVAILABLE DATABASES:", *data, sep="\n")
                seldb=input("ENTER THE SELECTED DB_NAME: ")
                if seldb.lower() in data:
                        con=m.connect(host="localhost", user="root", password="12345",database=f"{seldb}")
                        cur=con.cursor()
                        cur.execute("SHOW TABLES")
                        data1=[df[0] for df in cur.fetchall()]
                        print("AVAILABLE TABLES:", *data1, sep="\n")
                        tblna=input("ENTER THE TABLE NAME:")
                        if tblna.lower() in data1:
                                cur.execute(f"desc {tblna}")
                                data2=[dt[0] for dt in cur.fetchall()]
                                print("RECORDS:", *data2, sep="\n")
                                re=input("ENTER THE COLLUMN NAME:")
                                va=input("ENTER THE VALUE OF THE COLLUMN TO DELETE THE RECORD:")
                                cur.execute(f"DELETE FROM {tblna} WHERE {re} = %s", (va,))
                                con.commit()
                                print("SUCCESSFULLY DELETED!!!!!")
                               
                                cd=input("DO YOU WANT TO DELETE MORE(Y/N):")
                        else:
                                print("TABLE DOES'NT EXISTS!!!")
                else:
                        print("DATABASE DOES'NT EXISTS!!!")
sf="Y"
while sf=="y" or sf=="Y":
        h=int(input("ENTER YOUR CHOICE:"))
        if h==1:
                database()
                sf=input("WANT TO DELETE ANYTHING MORE??(Y/N)")
        elif h==2:
                table()
                sf=input("WANT TO DELETE ANYTHING MORE??(Y/N)")
        elif h==3:
                records()
                sf=input("WANT TO DELETE ANYTHING MORE??(Y/N)")
        elif h==4:
                element()
                sf=input("WANT TO DELETE ANYTHING MORE??(Y/N)")
        else:
                print("WRONG CHOICE!!!")
                sf=input("WANT TO DELETE ANYTHING MORE??(Y/N)")
        
