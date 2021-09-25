print("===============================")
print("==STUDENT==MANAGEMENT==SYSTEM==")
print("===============================")

import mysql.connector as con
mycon=con.connect(host="localhost", user="root", password="root", database="school")
c=mycon.cursor()


def add():
    print("\a1-to add student info\n\a2-to add marks")
    a=int(input("enter no b/w 1-2:"))

    if a==1:
        a1=int(input("enter addmision no "))
        a2=input("enter name of student")
        a3=input("enter parent name")
        a4=int(input("enter roll no"))
        a5=int(input("enter phone no"))
        c.execute("insert into 12s values(%s,%s,%s,%s,%s)",(a1,a2,a3,a4,a5))
        mycon.commit()

    elif a==2:
        a1=int(input("enter roll no:"))
        a2=input("enter name of student:")
        a3=int(input("marks in phy:"))
        a4=int(input("marks in chem:"))
        a5=int(input("marks in maths"))
        c.execute("insert into 12m values(%s,%s,%s,%s,%s)",(a1,a2,a3,a4,a5))
        mycon.commit()

    print("record added") 


def tc():
    print("\a1-to delete student info\n\a2-to delete marks info")
    a=int(input("enter no b/w 1-2:"))

    if a==1:
        a1=int(input("enter addmision no"))
        c.execute("delete from 12s where ano=%s",(a1,))
        mycon.commit()

    elif a==2:
        a1=int(input("enter roll no"))
        c.execute("delete from 12m where rno=%s",(a1,))
        mycon.commit()
        
    print("record deleted")


def upd():
    print("\a1-to update info\n\a2-to update marks")
    a=int(input("enter no b/w 1-2"))

    if a==1:
        a1=int(input("enter addmision no"))
        print("\a1-change addmision no\n\a2-change student name\n\a3-change parent name\n\a4-change roll no\n\a5-change phone no")
        b=int(input("enter no b/w 1-5"))

        if b==1:
            d=int(input("new addmision no"))
            c.execute("update 12s set ano=%s where ano=%s",(d,a1))
            mycon.commit()        

        elif b==2:
            d=input("new name")
            c.execute("update 12s set name=%s where ano=%s",(d,a1))
            mycon.commit()

        elif b==3:
            d=input("new parent name")
            c.execute("update 12s set pname=%s where ano=%s",(d,a1))
            mycon.commit()

        elif b==4:
            d=int(input("new roll no"))
            c.execute("update 12s set rno=%s where ano=%s",(d,a1))
            mycon.commit()

        elif b==5:
            d=input("new phone no")
            c.execute("update 12s set pno=%s where ano=%s",(d,a1))
            mycon.commit()

    elif a==2:
        a1=int(input("enter roll no"))
        print("\a1-change roll no\n\a2-change name of student\n\a3-change phy marks\n\a4-change chem marks\n\a5-change maths marks")
        b=int(input("enter no b/w 1-5"))

        if b==1:
            d=int(input("new roll no"))
            c.execute("update 12m set rno=%s where rno=%s",(d,a1))
            mycon.commit()        

        elif b==2:
            d=input("new name")
            c.execute("update 12m set name=%s where rno=%s",(d,a1))
            mycon.commit()

        elif b==3:
            d=input("new marks of physics")
            c.execute("update 12m set phy=%s where rno=%s",(d,a1))
            mycon.commit()

        elif b==4:
            d=int(input("new marks of chemistry"))
            c.execute("update 12m set chem=%s where rno=%s",(d,a1))
            mycon.commit()

        elif b==5:
            d=input("new marks of maths")
            c.execute("update 12s set math=%s where rno=%s",(d,a1))
            mycon.commit()
        
    print("record updated")


def ch():
    print("\a1-check student info\n\a2-check student marks")
    a=int(input("enter no b/w 1-2"))

    if a==1:
        print("\a1-check all records\n\a2-check particular record")
        a1=int(input("enter a no b/w 1-2"))

        if a1==1:
            c.execute("select * from 12s ")
            x=c.fetchall()
            print(x)

        elif a1==2:
            b=int(input("addmision no of student"))
            c.execute("select * from 12s where ano=%s",(b,))
            print(c.fetchone())

    elif a==2:
        print("\a1-check marks of all students\n\a2-check marks of particular student")
        a1=int(input("enter a no b/w 1-2"))

        if a1==1:
            c.execute("select * from 12m ")
            x=c.fetchall()
            print(x)

        elif a1==2:
            b=int(input("roll no of student"))
            c.execute("select * from 12m where rno=%s",(b,))
            print(c.fetchone())
        

n="y"
while n=="y":
    print("\a1-inserting a record \n\a2-delete a record \n\a3-updating a rec \n\a4-check record")
    x = int(input("enter no b/w 1-4:"))

    if x==1:
        add()
    elif x==2:
        tc()
    elif x==3:
        upd()
    elif x==4:
        ch()
    n=input("do you want to continue y/n")

