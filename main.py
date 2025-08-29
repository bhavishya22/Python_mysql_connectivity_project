import mysql.connector as m
from tabulate import tabulate
con=m.connect(host="localhost", user="root", password="12345")
print("""++++++++++++++++++++++++++++++++STUDENT MANAGEMENT SYSTEM++++++++++++++++++++++++++++++++++++++++""")
def menu():
        print("""
===========================WELCOME TO MENU SECTION OF STUDENT MANAGEMENT SYSTEM=========================
WHAT DO YOU WANT TO DO ?
1)BUILD DATABASE AND MAKE TABLE OR MAKE TABLE IN DEFAULT DATABASE #PRESS 1
2)DISPLAY THE DATA #PRESS 2
3)DELETE THE DATA #PRESS 3
4)UPDATE THE RECORDS, COLUMN NAME, TABLE NAME, DATABASE NAME #PRESS 4
5)MENU
6)EXIT #PRESS 5""")
def fun():
        for i in range(118):
            print("=", end="")
def database():
        global con
        n=input(" DO YOU WANT TO CREATE DATABASE (Y/N):")
        if n=="y" or n=="Y":
                db_name=input("ENTER THE DATABASE NAME:")
                cur=con.cursor()
                cur.execute( f"CREATE DATABASE {db_name}")
                print(f"DATABASE '{db_name}' SUCCESSFULLY CREATED.")
                con=m.connect(host="localhost", user="root", password="12345", database=f"{db_name}")
                cur=con.cursor()
                ac=input("\nDO YOU WANT TO CREATE TABLE:")
                if ac=="y" or ac=="Y":
                        tbna=input("ENTER THE TABLE NAME:")
                        att=int(input("ENTER THE NUMBER OF ATTRIBUTE:"))
                        f="y"
                        l=[]
                        while f=="Y" or f=="y":
                                for i in range(att):
                                        na=input("ENTER THE ATTRIBUTE NAME WITHOUT SPACES(EX-STOCK_ID):")
                                        fun()
                                        print("""
                        int-1
                        int(m)-2 #m-no. of digits
                        float-3
                        float(m,d)-4 #m-maximum possible length including decimal
                                                #d-fixed no. of decimal places
                        date-5 #YYYY-MM-DD
                        time-6 #HH:MM:SS
                        datetime-7 #YYYY-MM-DD HH:MM:SS
                        year(m)-8 #m=2 (ex-12)
                                           #m=4 (ex-2012)
                        varchar(m)-9 #length of text
                        char-10 #default value 1
                        char(m)-11 #length of text
                        null 12""")
                                        fun()
                                        dt=int(input("ENTER THE DT NO.:"))
                                        if dt==1:
                                                ab="int"
                                                l.append([na,ab])
                                        elif dt==2:
                                                n=int(input("ENTER THE LENGTH:"))
                                                ab=f"int({n})"
                                                l.append([na,ab])
                                        elif dt==3:
                                                ab="float"
                                                l.append([na,ab])
                                        elif dt==4:
                                                n=int(input("maximum possible length including decimal:"))
                                                v=int(input("fixed no. of decimal places:"))
                                                ab=f"float({n},{v})"
                                                l.append([na,ab])
                                        elif dt==5:
                                                ab="date"
                                                l.append([na,ab])
                                        elif dt==6:
                                                ab="time"
                                                l.append([na,ab])
                                        elif dt==7:
                                                ab="datetime"
                                                l.append([na,ab])
                                        elif dt==8:
                                                n=int(input("ENTER THE LENGTH(2 OR 4):"))
                                                ab=f"year({n})"
                                                l.append([na,ab])
                                        elif dt==9:
                                                n=int(input("ENTER THE LENGTH:"))
                                                ab=f"varchar({n})"
                                                l.append([na,ab])
                                        elif dt==10:
                                                ab="char"
                                                l.append([na,ab])
                                        elif dt==11:
                                                n=int(input("ENTER THE LENGTH:"))
                                                ab=f"char({n})"
                                                l.append([na,ab])
                                        elif dt==12:
                                                ab="null"
                                                l.append([na,ab])
                                        else:
                                                print("wrong choice!!!")
                                f=input("MORE ENTRIES(Y/N):")
                        attri= ", ".join([f"{attr[0]} {attr[1]}" for attr in l])
                        cur.execute(f"CREATE TABLE {tbna}({attri})")
                        print("TABLE SUCCESSFULLY CREATED!!!!")
                        c="y"
                        while c=="y" or c=="Y":
                                inp=input(f"ENTER THE VALUES {attri} SEPARATED BY COMMA:")
                                sqltxt=f"INSERT INTO {tbna} VALUES({', '.join(['%s']*len(l))});"
                                val=inp.split(",")
                                cur.execute(sqltxt,val)
                                con.commit()
                                c=input("do you want to continue:")
        else:
                cur= con.cursor()
                cur.execute("SHOW DATABASES")
                data=[db[0] for db in cur.fetchall()]
                print("AVAILABLE DATABASES:", *data, sep="\n")
                seldb=input("ENTER THE SELECTED DB_NAME: ")
                if seldb.lower() in data or seldb in data:
                        con=m.connect(host="localhost", user="root", password="12345", database=seldb)
                        print(f"SUCCESSFULLY CONNECTED TO DATABASE: {seldb}")
                        fun()
                        con=m.connect(host="localhost", user="root", password="12345", database=f"{seldb}")
                        cur=con.cursor()
                        ac=input("DO YOU WANT TO CREATE TABLE:")
                        if ac=="y" or ac=="Y":
                                tbna=input("ENTER THE TABLE NAME:")
                                att=int(input("ENTER THE NUMBER OF ATTRIBUTE:"))
                                f="y"
                                l=[]
                                while f=="Y" or f=="y":
                                        for i in range(att):
                                                na=input("ENTER THE ATTRIBUTE NAME WITHOUT SPACES(EX-STOCK_ID):")
                                                fun()
                                                print("""
                                int-1
                                int(m)-2 #m-no. of digits
                                float-3
                                float(m,d)-4 #m-maximum possible length including decimal
                                                        #d-fixed no. of decimal places
                                date-5 #YYYY-MM-DD
                                time-6 #HH:MM:SS
                                datetime-7 #YYYY-MM-DD HH:MM:SS
                                year(m)-8 #m=2 (ex-12)
                                                   #m=4 (ex-2012)
                                varchar(m)-9 #length of text
                                char-10 #default value 1
                                char(m)-11 #length of text
                                null 12""")
                                                fun()
                                                dt=int(input("ENTER THE DT NO.:"))
                                                if dt==1:
                                                        ab="int"
                                                        l.append([na,ab])
                                                elif dt==2:
                                                        n=int(input("ENTER THE LENGTH:"))
                                                        ab=f"int({n})"
                                                        l.append([na,ab])
                                                elif dt==3:
                                                        ab="float"
                                                        l.append([na,ab])
                                                elif dt==4:
                                                        n=int(input("maximum possible length including decimal:"))
                                                        v=int(input("fixed no. of decimal places:"))
                                                        ab=f"float({n},{v})"
                                                        l.append([na,ab])
                                                elif dt==5:
                                                        ab="date"
                                                        l.append([na,ab])
                                                elif dt==6:
                                                        ab="time"
                                                        l.append([na,ab])
                                                elif dt==7:
                                                        ab="datetime"
                                                        l.append([na,ab])
                                                elif dt==8:
                                                        n=int(input("ENTER THE LENGTH(2 OR 4):"))
                                                        ab=f"year({n})"
                                                        l.append([na,ab])
                                                elif dt==9:
                                                        n=int(input("ENTER THE LENGTH:"))
                                                        ab=f"varchar({n})"
                                                        l.append([na,ab])
                                                elif dt==10:
                                                        ab="char"
                                                        l.append([na,ab])
                                                elif dt==11:
                                                        n=int(input("ENTER THE LENGTH:"))
                                                        ab=f"char({n})"
                                                        l.append([na,ab])
                                                elif dt==12:
                                                        ab="null"
                                                        l.append([na,ab])
                                                else:
                                                        print("wrong choice!!!")
                                        f=input("MORE ENTRIES(Y/N):")
                                attri= ", ".join([f"{attr[0]} {attr[1]}" for attr in l])
                                cur.execute(f"CREATE TABLE {tbna}({attri})")
                                print("TABLE SUCCESSFULLY CREATED")
                                c="y"
                                while c=="y" or c=="Y":
                                        inp=input(f"ENTER THE VALUES {attri} SEPARATED BY COMMA:")
                                        sqltxt=f"INSERT INTO {tbna} VALUES({', '.join(['%s']*len(l))});"
                                        val=inp.split(",")
                                        cur.execute(sqltxt,val)
                                        con.commit()
                                        c=input("DO YOU WANT TO CONTINUE:")
                        else:
                                print("ERROR!!")
                else:
                        print("INVALID DATABASE NAME!!!!!!!!!!")

def delete():
        fun()
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
        fun()
        def delbase():
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
                                      fun()
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
                                fun()
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
                                        fun()                                       
                                        cd=input("DO YOU WANT TO DELETE MORE(Y/N):")
                                else:
                                        print("TABLE DOES'NT EXISTS!!!")
                        else:
                                print("DATABASE DOES'NT EXISTS!!!")
        sf="Y"
        while sf=="y" or sf=="Y":
                h=int(input("ENTER YOUR CHOICE:"))
                if h==1:
                        delbase()
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
def update():
        fun()
        print("""UPDATE OPERATIONS
1)UPDATE TABLE NAME-1
2)UPDATE COLUMN NAME-2♫
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
                                        fun()
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
                                    fun()
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
                                            fun()
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

def display():
    print("""DISPLAY OPERATION
1) DISPLAY TABLE
2) DISPLAY NO. OF RECORDS
3) DISPLAY DATA ACCORDING TO CONDITIONS
4) DISPLAY DATA ACCORDING TO CONDITIONS, GROUP BY, AND AGGREGATE FUNCTION
5) DISPLAY DATA ACCORDING TO CONDITIONS, ORDER BY, AND AGGREGATE FUNCTION""")
    sd = int(input("ENTER YOUR CHOICE: "))
    con = m.connect(host="localhost", user="root", password="12345")
    cur = con.cursor()
    cur.execute("SHOW DATABASES")
    databases = [db[0] for db in cur.fetchall()]
    print("AVAILABLE DATABASES:", *databases, sep="\n")
    seldb = input("ENTER THE SELECTED DB_NAME: ")
    if seldb.lower() not in databases:
        print("INVALID DATABASE NAME!")
        return
    con = m.connect(host="localhost", user="root", password="12345", database=seldb)
    cur = con.cursor()
    cur.execute("SHOW TABLES")
    tables = [tbl[0] for tbl in cur.fetchall()]
    print("AVAILABLE TABLES:", *tables, sep="\n")
    tblna = input("ENTER THE TABLE NAME: ")
    if tblna.lower() not in tables:
        print("INVALID TABLE NAME!")
        return
    if sd == 1:
        cur.execute(f"SELECT * FROM {tblna}")
        rows = cur.fetchall()
        cur.execute(f"DESCRIBE {tblna}")
        headers = [col[0] for col in cur.fetchall()]
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    elif sd == 2:
        cur.execute(f"SELECT * FROM {tblna}")
        num_records = int(input("ENTER THE NUMBER OF RECORDS TO DISPLAY: "))
        rows = cur.fetchmany(num_records)
        cur.execute(f"DESCRIBE {tblna}")
        headers = [col[0] for col in cur.fetchall()]
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    elif sd == 3:
        cur.execute(f"DESCRIBE {tblna}")
        headers = [col[0] for col in cur.fetchall()]
        condition = input("ENTER YOUR CONDITION (e.g., age > 30): ")
        query = f"SELECT * FROM {tblna} WHERE {condition}"
        cur.execute(query)
        rows = cur.fetchall()
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    elif sd == 4:
        cur.execute(f"DESCRIBE {tblna}")
        headers = [col[0] for col in cur.fetchall()]
        group_by_col = input(f"ENTER THE COLUMN NAME TO GROUP BY (available: {', '.join(headers)}): ")
        aggregate_col = input(f"ENTER THE COLUMN NAME TO APPLY AGGREGATE FUNCTION ON (available: {', '.join(headers)}): ")
        aggregate_func = input("ENTER THE AGGREGATE FUNCTION (e.g., SUM, AVG, COUNT): ").upper()
        query = f"SELECT {group_by_col}, {aggregate_func}({aggregate_col}) AS result FROM {tblna} GROUP BY {group_by_col}"
        cur.execute(query)
        rows = cur.fetchall()
        print(tabulate(rows, headers=[group_by_col, f"{aggregate_func}({aggregate_col})"], tablefmt="grid"))
    elif sd == 5:
        cur.execute(f"DESCRIBE {tblna}")
        headers = [col[0] for col in cur.fetchall()]
        order_by_col = input(f"ENTER THE COLUMN NAME TO ORDER BY (available: {', '.join(headers)}): ")
        order_type = input("ENTER THE ORDER TYPE (ASC/DESC): ").upper()
        aggregate_col = input(f"ENTER THE COLUMN NAME TO APPLY AGGREGATE FUNCTION ON (available: {', '.join(headers)}): ")
        aggregate_func = input("ENTER THE AGGREGATE FUNCTION (e.g., SUM, AVG, COUNT): ").upper()
        query = f"SELECT {aggregate_func}({aggregate_col}) AS result FROM {tblna} ORDER BY {order_by_col} {order_type}"
        cur.execute(query)
        rows = cur.fetchall()
        print(tabulate(rows, headers=[f"{aggregate_func}({aggregate_col})"], tablefmt="grid"))

    else:
        print("INVALID CHOICE!")

def display():
            fun()
            print("""DISPLAY OPERATION
        1) DISPLAY TABLE
        2) DISPLAY NO. OF RECORDS
        3) DISPLAY DATA ACCORDING TO CONDITIONS
        4) DISPLAY DATA ACCORDING TO CONDITIONS, GROUP BY, AND AGGREGATE FUNCTION
        5) DISPLAY DATA ACCORDING TO CONDITIONS, ORDER BY, AND AGGREGATE FUNCTION""")
            
            sd = int(input("ENTER YOUR CHOICE: "))
            con = m.connect(host="localhost", user="root", password="12345")
            cur = con.cursor()
            cur.execute("SHOW DATABASES")
            databases = [db[0] for db in cur.fetchall()]
            print("AVAILABLE DATABASES:", *databases, sep="\n")
            seldb = input("ENTER THE SELECTED DB_NAME: ")
            if seldb.lower() not in databases:
                print("INVALID DATABASE NAME!")
                return
            con = m.connect(host="localhost", user="root", password="12345", database=seldb)
            cur = con.cursor()
            cur.execute("SHOW TABLES")
            tables = [tbl[0] for tbl in cur.fetchall()]
            print("AVAILABLE TABLES:", *tables, sep="\n")
            tblna = input("ENTER THE TABLE NAME: ")
            if tblna.lower() not in tables:
                print("INVALID TABLE NAME!")
                return
            if sd == 1:
                cur.execute(f"SELECT * FROM {tblna}")
                rows = cur.fetchall()
                cur.execute(f"DESCRIBE {tblna}")
                headers = [col[0] for col in cur.fetchall()]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
                fun()
            elif sd == 2:
                cur.execute(f"SELECT * FROM {tblna}")
                num_records = int(input("ENTER THE NUMBER OF RECORDS TO DISPLAY: "))
                rows = cur.fetchmany(num_records)
                cur.execute(f"DESCRIBE {tblna}")
                headers = [col[0] for col in cur.fetchall()]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
                fun()
            elif sd == 3:
                cur.execute(f"DESCRIBE {tblna}")
                headers = [col[0] for col in cur.fetchall()]
                condition = input("ENTER YOUR CONDITION (e.g., age > 30): ")
                query = f"SELECT * FROM {tblna} WHERE {condition}"
                cur.execute(query)
                rows = cur.fetchall()
                print(tabulate(rows, headers=headers, tablefmt="grid"))
                fun()
            elif sd == 4:
                cur.execute(f"DESCRIBE {tblna}")
                headers = [col[0] for col in cur.fetchall()]
                group_by_col = input(f"ENTER THE COLUMN NAME TO GROUP BY (available: {', '.join(headers)}): ")
                aggregate_col = input(f"ENTER THE COLUMN NAME TO APPLY AGGREGATE FUNCTION ON (available: {', '.join(headers)}): ")
                aggregate_func = input("ENTER THE AGGREGATE FUNCTION (e.g., SUM, AVG, COUNT): ").upper()
                query = f"SELECT {group_by_col}, {aggregate_func}({aggregate_col}) AS result FROM {tblna} GROUP BY {group_by_col}"
                cur.execute(query)
                rows = cur.fetchall()
                print(tabulate(rows, headers=[group_by_col, f"{aggregate_func}({aggregate_col})"], tablefmt="grid"))
                fun()
            elif sd == 5:
                cur.execute(f"DESCRIBE {tblna}")
                headers = [col[0] for col in cur.fetchall()]
                order_by_col = input(f"ENTER THE COLUMN NAME TO ORDER BY (available: {', '.join(headers)}): ")
                order_type = input("ENTER THE ORDER TYPE (ASC/DESC): ").upper()
                aggregate_col = input(f"ENTER THE COLUMN NAME TO APPLY AGGREGATE FUNCTION ON (available: {', '.join(headers)}): ")
                aggregate_func = input("ENTER THE AGGREGATE FUNCTION (e.g., SUM, AVG, COUNT): ").upper()
                query = f"SELECT {aggregate_func}({aggregate_col}) AS result FROM {tblna} ORDER BY {order_by_col} {order_type}"
                cur.execute(query)
                rows = cur.fetchall()
                print(tabulate(rows, headers=[f"{aggregate_func}({aggregate_col})"], tablefmt="grid"))
                fun()
            else:
                print("INVALID CHOICE!")
menu()
btx=int(input("ENTER YOUR CHOICE ACCORDING TO MENU:"))
if btx==1:
        database()
        btx=int(input("ENTER YOUR CHOICE ACCORDING TO MENU:"))
elif btx==2:
        display()
        menu()
        btx=int(input("ENTER YOUR CHOICE ACCORDING TO MENU:"))
elif btx==3:
        delete()
        menu()
        btx=int(input("ENTER YOUR CHOICE ACCORDING TO MENU:"))
elif btx==4:
        update()
        menu()
        btx=int(input("ENTER YOUR CHOICE ACCORDING TO MENU:"))
elif btx==5:
        menu()
        btx=int(input("ENTER YOUR CHOICE ACCORDING TO MENU"))
elif btx==6:
        exit(0)
else:
        print("INVALID CHOICE")
