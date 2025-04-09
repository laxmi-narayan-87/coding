#project on employee management system
import mysql .connector as driver
import sys
def menu():
    loop='y'
    while(loop=='y' or loop =='y'):
        print("...........MENU.........")
        print("1.CREATE DATABASE")
        print("2.SHOW DATABASE")
        print("3.CREATE TABLE")
        print("4.SHOW TABLE")
        print("5. INSERT RECORD")
        print("6.UPDATE RECORD")
        print("7.DELETE RECORD")
        print("8.SEARCH RECORD")
        print("9. DISPLAY RECORD")
        print()
        print()
        choice=int(input(" ENTER THE CHOICE(1-9):"))
        if(choice==1):
            create_database()
        elif(choice==2):
            show_databse()
        elif(choice==3):
            create_table()
        elif(choice==4):
            show_table()
        elif(choice==5):
            insert_record()
        elif(choice==6):
            update_record()
        elif(choice==7):
            delete_record()
        elif(choice==8):
            search_record()
        elif(choice==9):
            display_record()
        else:
            sys.exit()
# DATABASE CREATION:
def create_databse():
    con=driver.connect(host='localhost',use='root',password='akshaj',charset='utf8')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('create database if not exists employee')
    print()
    print("database created")
    con.close()
#DISPLAY DATABASE:
def show_databse():
    con=driver.connect(host='localhost',use='root',password='akshaj',charset='utf8')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('show database')
    for i in cur:
        print(i)
    con.close()
#TABLE CREATION :
    
