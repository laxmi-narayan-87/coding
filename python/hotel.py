import random
import datetime
name=[]
phone no. =[]
add=[]
checkin=[]
checkout=[]
room=[]
price=[]
rc=[]
p=[]
room no.[]
customer id=[]
day=[]
i=0
def home():
    print("\t\t\t\t\t\tWELCOME TO HOTEL NARAYAN\n")
    print("\t\t\t 1Booking\n")
    print("\t\t\t 2Rooms info\n")
    print("\t\t\t 3room services(menu card)\n")
    print("\t\t\t 4 payment\n")
    print("\t\t\t 5 record\n")
    print("\t\t\t 0 exit\n")
    ch=int(input("->"))
    if ch==1:
        print("")
        booking()
    elif ch==2:
        print("")
        rooms_info()
    elif ch==3:
        print("")
        restaurant()
    elif ch==4:
        print("")
        payment()
    elif ch==5:
        print("")
        record()
    else:
        exit()
def date(c):
    if c[2]>=2019and c[2]<=2020:
        if c[1]!=0 and c[1]<=12:
            if c[1]==2 and c[0]!=0 and c[0]<=31:
                
