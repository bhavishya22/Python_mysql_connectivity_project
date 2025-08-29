import mysql.connector as mysql
mydb=mysql.connect(host="localhost", user="root", password="12345", database="store")
cur=mydb.cursor()
ac=input("DO YOU WANT TO CREATE TABLE:")
if ac=="y" or ac=="Y":
        tbna=input("ENTER THE TABLE NAME:")
        att=int(input("ENTER THE NUMBER OF ATTRIBUTE:"))
        f="y"
        l=[]
        while f=="Y" or f=="y":
                for i in range(att):
                        na=input("ENTER THE ATTRIBUTE NAME WITHOUT SPACES(EX-STOCK_ID):")
                        print("""int-1
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
        c="y"
        while c=="y" or c=="Y":
                inp=input(f"ENTER THE VALUES {attri} SEPARATED BY COMMA:")
                sqltxt=f"INSERT INTO {tbna} VALUES({', '.join(['%s']*len(l))});"
                val=inp.split(",")
                cur.execute(sqltxt,val)
                mydb.commit()
                c=input("do you want to continue:")
else:
        print("error!!")
        

