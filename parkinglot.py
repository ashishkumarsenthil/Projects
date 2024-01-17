import mysql.connector
import threading
import time
import datetime
from datetime import date
cnx=mysql.connector.connect(user="root",password="7Vizhi7Senthil7$",host="localhost", auth_plugin="mysql_native_password")
def availableslots():
    file1=open("slots.txt","w")
    st=100
    floor=3
    totst=3*100
availableslots()
print("the price for parking here for an hour is 30 RUPEES") 
print("if arival of the vehicle--say a")
print("if departure of the vehicle--say d")
i=0
cursor=cnx.cursor()
cursor.execute("drop database if exists parking")
cursor.execute("create database if not exists parking")
cursor.execute("use parking")
cursor.execute("create table if not exists arrival(slot_number int,floor_no int,car_number varchar(20),time_arr time,date_arr date,contact_num bigint(10))")
cursor.execute("create table if not exists parked_cars(slot_number int,floor_no int,car_number varchar(20),time_arr time,date_arr date,contact_num bigint(10))")
cursor.execute("create table if not exists departure(slot_number int,floor_no int,car_number varchar(20),time_dep time,date_dep date,rate decimal(10,2))")
i=0
#ARRIVAL
def arrival():
    global i
    i=i+1
    if i>300:
        print("the parking slots are full")
    else:
        b=input("enter car number")
        phone=int(input("enter contact number"))
        date=input("enter todays date(yyyy-mm-dd)")
        time=input("enter current time(hh:min:sec)")
        fl=0
        if i>100 and i<=200:
            fl=2
        elif i>200 and i<=300:
            fl=3
        else:
            fl=1       
        query="insert into arrival(slot_number,floor_no,car_number,time_arr,date_arr,contact_num) values(%s,%s,%s,%s,%s,%s)"
        query11="insert into parked_cars(slot_number,floor_no,car_number,time_arr,date_arr,contact_num) values(%s,%s,%s,%s,%s,%s)"
        val=(i,fl,b,time,date,phone,)
        cursor.execute(query,val)
        cursor.execute(query11,val)
#DEPARTURE
def departure():
    global i
    i=i-1
    if i<0:
        print("there are no cars to leave")
    else:
        p=1
        u=0
        while u==0:
            c=input("enter car number")
            date1=input("enter todays date(yyyy-mm-dd)")
            time1=input("enter current time(hh:min:sec)")
            query="select car_number from arrival"
            cursor.execute(query)
            t=cursor.fetchall()
            for o in t:
                if c==o[0]:
                    u=u+1
                    q=0
                    break
                else:
                    q=1
                    p=p+1
            while q!=0:
                if p>1:
                    print("the car number entered is invalid")
                q=0
        h=c
        fl=0
        if i+1>100 and i+1<=200:
            fl=2
        elif i+1>200 and i+1<=300:
            fl=3
        else:
            fl=1
        d=i+1
        query22="delete from parked_cars where car_number=(%s)"
        val22=(h,)
        cursor.execute(query22,val22)
        query="insert into departure(slot_number,floor_no,car_number,time_dep,date_dep,rate) values(%s,%s,%s,%s,%s,%s)"
        val=(d,fl,h,time1,date1,30)
        cursor.execute(query,val)
        cnx.commit()
        val1=(h,)
        query3="select hour(time_dep) from departure where car_number=(%s)"
        cursor.execute(query3,val1)
        mm=cursor.fetchall()
        query4="select minute(time_dep) from departure where car_number=(%s)"
        cursor.execute(query4,val1)
        nn=cursor.fetchall()
        query5="select second(time_dep) from departure where car_number=(%s)"
        cursor.execute(query5,val1)
        oo=cursor.fetchall()
        query6="select year(date_dep) from departure where car_number=(%s)"
        cursor.execute(query6,val1)
        pp=cursor.fetchall()
        query7="select month(date_dep) from departure where car_number=(%s)"
        cursor.execute(query7,val1)
        qq=cursor.fetchall()
        query8="select day(date_dep) from departure where car_number=(%s)"
        cursor.execute(query8,val1)
        rr=cursor.fetchall()
        query9="select hour(time_arr) from arrival where car_number=(%s)"
        cursor.execute(query9,val1)
        ss=cursor.fetchall()
        query10="select minute(time_arr) from arrival where car_number=(%s)"
        cursor.execute(query10,val1)
        tt=cursor.fetchall()
        query11="select second(time_arr) from arrival where car_number=(%s)"
        cursor.execute(query11,val1)
        uu=cursor.fetchall()
        query12="select year(date_arr) from arrival where car_number=(%s)"
        cursor.execute(query12,val1)
        vv=cursor.fetchall()
        query13="select month(date_arr) from arrival where car_number=(%s)"
        cursor.execute(query13,val1)
        xx=cursor.fetchall()
        query14="select day(date_arr) from arrival where car_number=(%s)"
        cursor.execute(query14,val1)
        yy=cursor.fetchall()
        a=datetime.datetime(pp[0][0],qq[0][0],rr[0][0],mm[0][0],nn[0][0],oo[0][0])
        b=datetime.datetime(vv[0][0],xx[0][0],yy[0][0],ss[0][0],tt[0][0],uu[0][0])
        c=a-b
        time_parked=int((c.seconds)/(60*60))+((c.days)*24)
        print("YOU HAVE PARKED FOR",c,"AND",time_parked,"HOURS")
        
        if time_parked!=0:
            rat=(time_parked*30)+30
            query66="update departure set rate=(%s) where car_number=(%s)"
            val3=(rat,h,)
            cursor.execute(query66,val3)
            cnx.commit()
            print("THE AMOUNT TO BE PAID IS:",rat)
        else:
            rat=30
            print("THE AMOUNT TO BE PAID IS:",rat)
def parked():
    query10="select count(distinct car_number) from arrival"
    cursor.execute(query10)
    w=cursor.fetchall()
    query11="select count(distinct car_number) from departure"
    cursor.execute(query11)
    q=cursor.fetchall()
    park=w[0][0]-q[0][0]
    print("THERE ARE",park,"CARS PARKED RIGHT NOW")
    print("THERE ARE ",300-park,"EMPTY SLOTS LEFTS")
    query33="select * from parked_cars"
    cursor.execute(query33)
    e=cursor.fetchall()
    print("slot_num","\t","floor_num","\t","car_num","\t","time_arr","\t","\t","date_arr","\t","\t","contact_num")
    for mp in range(0,len(e)):
        for np in range(0,len(e[mp])):
            print(e[mp][np],end="\t\t")
        print()
def arr_reports():
    query12="select * from arrival"
    cursor.execute(query12)
    e=cursor.fetchall()
    print("slot_num","\t","floor_num","\t","car_num","\t","time_arr","\t","\t","date_arr","\t","\t","contact_num")
    for mp in range(0,len(e)):
        for np in range(0,len(e[mp])):
            print(e[mp][np],end="\t\t")
        print()
def dep_reports():
    query13="select * from departure"
    cursor.execute(query13)
    f=cursor.fetchall()
    print("slot_num","\t","floor_num","\t","car_num","\t","time_dep","\t","\t","date_dep","\t","\t","rate")
    for mpc in range(0,len(f)):
        for npc in range(0,len(f[mpc])):
            print(f[mpc][npc],end="\t\t")
        print()

while True:
    ch=input("enter if your admin or customer")
    
    if ch=="admin":
        passw="admin123"
        et=input("enter admin password")
        if et==passw:
            while True:
                it=int(input("enter which option you want--to see how many cars are parked[1],reports of cars arrived[2],reports of cars departed[3],quit[4]"))
                if it==1:
                    parked()
                elif it==2:
                    arr_reports()
                elif it==3:
                    dep_reports()
                oy=input("enter y if you want to continue and n if you want to quit")
                if oy=="y":
                    continue
                elif oy=="n":
                    print("quiting admin program")
                    break
                else:
                    print("invalid")
                    break
                
        else:
            print("THE PASSWORD ENTERED IS INCORRECT")
    elif ch=="customer":
        while True:
            ty=input("enter if your arriving or departing")
            if ty=="a":
                arrival()
            elif ty=="d":
                departure()
            mt=input("enter y if you want to continue and n if you want to quit")
            if mt=="y":
                continue
            elif mt=="n":
                print("quiting customer program")
                break
            else:
                print("invalid")
                break
    elif ch=="quit":
        print("quiting program")
        break
