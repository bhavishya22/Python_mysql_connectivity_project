import mysql.connector as m
print("""UPDATE OPERATIONS
1)UPDATE TABLE NAME-1
2)UPDATE COLUMN NAME-2
3)UPDATE RECORD DATA-3""")
def uptable():
        con=m.connect(host="localhost", user="root", password="12345")
        cur=con.cursor()
        cd="y"
        while cd=="y" or cd=="Y":
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
                        tblna=input("ENTER THE TABLE NAME TO UPDATE:")
                        if tblna.lower() in data1:
                                tblna1=input("ENTER THE NEW TABLE NAME TO UPDATE:")
                                cur.execute(f"RENAME TABLE {tblna} TO {tblna1}")
                                con.commit()
                                print("TABLE SUCESSFULLY UPDATED!!!")
                                cd=input("DO YOU WANT TO UPDATE MORE(Y/N):")
                        else:
                                print("TABLE DOES'NT EXISTS!!!")
                else:
                        print("DATABASE DOES'NT EXISTS!!!")
def upcolumn():
    con = m.connect(host="localhost", user="root", password="12345")
    cur = con.cursor()
    cd = "y"
    while cd.lower() == "y":
        cur.execute("SHOW DATABASES")
        data = [db[0] for db in cur.fetchall()]
        print("AVAILABLE DATABASES:", *data, sep="\n")
        seldb = input("ENTER THE SELECTED DB_NAME: ")
        if seldb.lower() in data:
            con = m.connect(host="localhost", user="root", password="12345", database=seldb)
            cur = con.cursor()
            cur.execute("SHOW TABLES")
            data1 = [df[0] for df in cur.fetchall()]
            print("AVAILABLE TABLES:", *data1, sep="\n")
            tblna = input("ENTER THE TABLE NAME TO UPDATE: ")
            if tblna.lower() in data1:
                cur.execute(f"DESCRIBE {tblna}")
                data2 = [(dg[0], dg[1]) for dg in cur.fetchall()]
                print("AVAILABLE COLUMNS:", *[col[0] for col in data2], sep="\n")
                colmn = input("ENTER THE OLD COLUMN NAME TO CHANGE: ")
                colmn1 = input("ENTER THE NEW COLUMN NAME TO UPDATE: ")
                column = next((col for col in data2 if col[0].lower() == colmn.lower()), None)
                if column:
                    cur.execute(f"ALTER TABLE {tblna} CHANGE {colmn} {colmn1} {column[1]}")
                    con.commit()
                    print("COLUMN SUCCESSFULLY UPDATED!!!")
                else:
                    print("COLUMN DOESN'T EXIST!!!!")
            else:
                print("TABLE DOESN'T EXIST!!!")
        else:
            print("DATABASE DOESN'T EXIST!!!")
        cd = input("DO YOU WANT TO UPDATE MORE (Y/N): ")
def uprecord():
    con = m.connect(host="localhost", user="root", password="12345")
    cur = con.cursor()
    cd = "y"
    while cd.lower() == "y":
        cur.execute("SHOW DATABASES")
        data = [db[0] for db in cur.fetchall()]
        print("AVAILABLE DATABASES:", *data, sep="\n")
        seldb = input("ENTER THE SELECTED DB_NAME: ")
        if seldb.lower() in [db.lower() for db in data]:
            con = m.connect(host="localhost", user="root", password="12345", database=seldb)
            cur = con.cursor()
            cur.execute("SHOW TABLES")
            data1 = [df[0] for df in cur.fetchall()]
            print("AVAILABLE TABLES:", *data1, sep="\n")
            tblna = input("ENTER THE TABLE NAME: ")
            if tblna.lower() in [table.lower() for table in data1]:
                cur.execute(f"DESCRIBE {tblna}")
                data2 = [dg[0] for dg in cur.fetchall()]
                print("AVAILABLE COLUMNS:", *data2, sep="\n")
                colmn = input("ENTER THE COLUMN NAME IN WHICH YOU WANT TO UPDATE: ")
                if colmn in data2:
                    colmn1 = input("ENTER THE NEW VALUE TO UPDATE: ")
                    cha = input("ENTER THE CONDITION COLUMN NAME: ")
                    if cha in data2:
                        pa = input("ENTER CONDITION COLUMN VALUE: ")
                        query = f"UPDATE {tblna} SET {colmn} = %s WHERE {cha} = %s"
                        cur.execute(query, (colmn1, pa))
                        con.commit()
                        if cur.rowcount > 0:
                            print("RECORD SUCCESSFULLY UPDATED!")
                        else:
                            print("NO RECORDS MATCH THE CONDITION.")
                    else:
                        print("CONDITION COLUMN DOESN'T EXIST!")
                else:
                    print("COLUMN TO UPDATE DOESN'T EXIST!")
            else:
                print("TABLE DOESN'T EXIST!")
        else:
            print("DATABASE DOESN'T EXIST!")
        cd = input("DO YOU WANT TO UPDATE MORE (Y/N): ")
    con.close()

co=int(input("ENTER YOUR CHOICE:"))
if co==1:
        uptable()
        co=int(input("ENTER YOUR CHOICE:"))
elif co==2:
        upcolumn()
        co=int(input("ENTER YOUR CHOICE:"))
elif co==3:
        uprecord()
        co=int(input("ENTER YOUR CHOICE:"))
else:
        print("WRONG CHOICE!!")
