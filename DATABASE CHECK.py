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
upcolumn()
