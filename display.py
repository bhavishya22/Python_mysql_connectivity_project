print("""DISPLAY OPERATION
1)DISPLAY TABLE-1
2)DISPLAY NO. OF RECORDS-2
3)DISPLAY DATA ACCORDING TO CONDITIONS-3
4)DISPLAY DATA ACCORDING TO CONDITIONS, GROUP BY AND AGGREGATE FUNCTION-4 
5)DISPLAY DATA ACCORDING TO CONDITIONS AND ORDER BY AND AGGREGATE FUNCTION-5""")
def disptable():
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
                if tblna in data1:
                        cur.execute(f"SELECT * FROM {tblna}")
                        rec=cur.fetchall()
                        cur.execute(f"DESCRIBE {tblna}")
                        data2 = [(dg[0], dg[1]) for dg in cur.fetchall()]
                        data3=[col[0] for col in data2]
                        for col in data3:
                                print(f"{col:<15}", end="")
                        print()
                        for row in rec:
                                for val in row:
                                        print(f"{val:<15}", end="")
                                print()
                else:
                        print("INCORRECT TABLE NAME!!!!!")
def disprec():
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
                        cur.execute(f"SELECT * FROM {tblna}")
                        cx = int(input("ENTER THE NO. OF RECORDS:"))
                        rec = cur.fetchmany(cx) 
                        cur.fetchall()
                        cur.execute(f"DESCRIBE {tblna}")
                        data2 = [(dg[0], dg[1]) for dg in cur.fetchall()]
                        data3 = [col[0] for col in data2]
                        for col in data3:
                            print(f"{col:<15}", end="")
                        print()
                        for row in rec:
                            for val in row:
                                print(f"{val:<15}", end="")
                            print()
                else:
                        print("INCORRECT TABLE NAME!!!!!")
def dispcond():
    con = m.connect(host="localhost", user="root", password="12345")
    cur = con.cursor()
    cur.execute("SHOW DATABASES")
    data = [db[0] for db in cur.fetchall()]
    print("AVAILABLE DATABASES:", *data, sep="\n")
    seldb = input("ENTER THE SELECTED DB_NAME: ")
    if seldb.lower() in data:
        con = m.connect(host="localhost", user="root", password="12345", database=f"{seldb}")
        cur = con.cursor()
        cur.execute("SHOW TABLES")
        data1 = [df[0] for df in cur.fetchall()]
        print("AVAILABLE TABLES:", *data1, sep="\n")
        tblna = input("ENTER THE TABLE NAME: ")
        if tblna.lower() in data1:
            cur.execute(f"DESCRIBE {tblna}")
            data2 = [(dg[0], dg[1]) for dg in cur.fetchall()]
            data3 = [col[0] for col in data2]
            print("AVAILABLE COLUMNS:", *data3, sep="\n")
            ad = int(input("ENTER THE NO. OF COLUMNS TO DISPLAY: "))
            selected_columns = []
            for i in range(ad):
                cs = input("ENTER THE COLUMN NAME: ")
                if cs in data3:
                    selected_columns.append(cs)
                else:
                    print(f"INVALID COLUMN NAME: {cs}")
            if selected_columns:
                condition = input("DO YOU WANT TO PUT ANY CONDITION? (y/n): ")
                query = f"SELECT {', '.join(selected_columns)} FROM {tblna}"
                if condition.lower() == 'y':
                    cond = input("ENTER YOUR CONDITION (e.g., age > 30): ")
                    query += f" WHERE {cond}"
                cur.execute(query)
                rc = cur.fetchall()
                for col in selected_columns:
                    print(f"{col:<15}", end="")
                print()
                for row in rc:
                    for value in row:
                        print(f"{value:<15}", end="")
                    print()
            else:
                print("NO VALID COLUMNS SELECTED!")
        else:
            print("INCORRECT TABLE NAME!!!!!")
    else:
        print("INCORRECT DATABASE NAME!!!!!")
def dispgrop():
            con = m.connect(host="localhost", user="root", password="12345")
            cur = con.cursor()
            cur.execute("SHOW DATABASES")
            data = [db[0] for db in cur.fetchall()]
            print("AVAILABLE DATABASES:", *data, sep="\n")
            seldb = input("ENTER THE SELECTED DB_NAME: ")
            if seldb.lower() in data:
                con = m.connect(host="localhost", user="root", password="12345", database=f"{seldb}")
                cur = con.cursor()
                cur.execute("SHOW TABLES")
                data1 = [df[0] for df in cur.fetchall()]
                print("AVAILABLE TABLES:", *data1, sep="\n")
                tblna = input("ENTER THE TABLE NAME: ")
                if tblna.lower() in data1:
                    cur.execute(f"DESCRIBE {tblna}")
                    data2 = [(dg[0], dg[1]) for dg in cur.fetchall()]
                    data3 = [col[0] for col in data2]
                    print("AVAILABLE COLUMNS:", *data3, sep="\n")
                    ad = int(input("ENTER THE NO. OF COLUMNS TO DISPLAY: "))
                    selected_columns = []
                    for i in range(ad):
                        cs = input("ENTER THE COLUMN NAME: ")
                        if cs in data3:
                            selected_columns.append(cs)
                        else:
                            print(f"INVALID COLUMN NAME: {cs}")
                    if selected_columns:
                        condition = input("DO YOU WANT TO PUT ANY CONDITION? (y/n): ")
                        query = f"SELECT {', '.join(selected_columns)} FROM {tblna}"
                        if condition.lower() == 'y':
                            cond = input("ENTER YOUR CONDITION (e.g., age > 30): ")
                            query += f" WHERE {cond}"
                        group_by = input("DO YOU WANT TO GROUP BY ANY COLUMN? (y/n): ")
                        if group_by.lower() == 'y':
                            group_col = input(f"ENTER THE COLUMN NAME TO GROUP BY (available columns: {', '.join(data3)}): ")
                            if group_col in data3:
                                query += f" GROUP BY {group_col}"
                                aggregated_cols = input("DO YOU WANT TO APPLY AGGREGATE FUNCTIONS? (e.g., SUM, COUNT) (y/n): ")
                                if aggregated_cols.lower() == 'y':
                                    for i, col in enumerate(selected_columns):
                                        if col != group_col:
                                            func = input(f"ENTER AGGREGATE FUNCTION FOR '{col}' (e.g., SUM, AVG): ").strip().upper()
                                            selected_columns[i] = f"{func}({col}) AS {col}_{func.lower()}"
                                    query = f"SELECT {', '.join(selected_columns)} FROM {tblna} GROUP BY {group_col}"
                            else:
                                print(f"INVALID GROUP BY COLUMN: {group_col}")
                                return
                        cur.execute(query)
                        rc = cur.fetchall()
                        for col in selected_columns:
                            print(f"{col.split(' AS ')[-1]:<15}", end="")
                        print()
                        for row in rc:
                            for value in row:
                                print(f"{value:<15}", end="")
                            print()
                    else:
                        print("NO VALID COLUMNS SELECTED!")
                else:
                    print("INCORRECT TABLE NAME!!!!!")
            else:
                print("INCORRECT DATABASE NAME!!!!!")
def dispord():
    con = m.connect(host="localhost", user="root", password="12345")
    cur = con.cursor()
    cur.execute("SHOW DATABASES")
    data = [db[0] for db in cur.fetchall()]
    print("AVAILABLE DATABASES:", *data, sep="\n")
    seldb = input("ENTER THE SELECTED DB_NAME: ")
    if seldb.lower() in data:
        con = m.connect(host="localhost", user="root", password="12345", database=f"{seldb}")
        cur = con.cursor()
        cur.execute("SHOW TABLES")
        data1 = [df[0] for df in cur.fetchall()]
        print("AVAILABLE TABLES:", *data1, sep="\n")
        tblna = input("ENTER THE TABLE NAME: ")
        if tblna.lower() in data1:
            cur.execute(f"DESCRIBE {tblna}")
            data2 = [(dg[0], dg[1]) for dg in cur.fetchall()]
            data3 = [col[0] for col in data2]
            print("AVAILABLE COLUMNS:", *data3, sep="\n")
            ad = int(input("ENTER THE NO. OF COLUMNS TO DISPLAY: "))
            selected_columns = []
            for i in range(ad):
                cs = input("ENTER THE COLUMN NAME: ")
                if cs in data3:
                    selected_columns.append(cs)
                else:
                    print(f"INVALID COLUMN NAME: {cs}")
            if selected_columns:
                condition = input("DO YOU WANT TO PUT ANY CONDITION? (y/n): ")
                query = f"SELECT {', '.join(selected_columns)} FROM {tblna}"
                if condition.lower() == 'y':
                    cond = input("ENTER YOUR CONDITION (e.g., age > 30): ")
                    query += f" WHERE {cond}"
                order_by = input("DO YOU WANT TO ORDER BY ANY COLUMN? (y/n): ")
                if order_by.lower() == 'y':
                    order_col = input(f"ENTER THE COLUMN NAME TO ORDER BY (available columns: {', '.join(data3)}): ")
                    if order_col in data3:
                        order_type = input("ENTER ORDER TYPE (ASC/DESC): ").strip().upper()
                        if order_type not in ["ASC", "DESC"]:
                            order_type = "ASC"  
                        query += f" ORDER BY {order_col} {order_type}"
                    else:
                        print(f"INVALID ORDER BY COLUMN: {order_col}")
                        return
                cur.execute(query)
                rc = cur.fetchall()
                for col in selected_columns:
                    print(f"{col:<15}", end="")
                print()
                for row in rc:
                    for value in row:
                        print(f"{value:<15}", end="")
                    print()
            else:
                print("NO VALID COLUMNS SELECTED!")
        else:
            print("INCORRECT TABLE NAME!!!!!")
    else:
        print("INCORRECT DATABASE NAME!!!!!")
sd=int(input("ENTER YOUR CHOICE:"))
if sd==1:
        disptable()
        sd=int(input("ENTER YOUR CHOICE:"))
elif sd==2:
        disprec()
        sd=int(input("ENTER YOUR CHOICE:"))
elif sd==3:
        dispcond()
        sd=int(input("ENTER YOUR CHOICE:"))
elif sd==4:
        dispgrop()
elif sd==5:
        dispord()
        sd=int(input("ENTER YOUR CHOICE:"))
else:
        print("WRONG CHOICE:")
