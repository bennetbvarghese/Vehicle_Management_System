import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="agentbp",database="vehicle")
mycursor=mydb.cursor()
def addvehicle():
    print()
    print('\t'+' *'*14)
    print('\t WELCOME TO INSERTION SCREEN')
    print('\t'+' *'*14)
    print()
    while True:
        carid=input("Enter Car ID :- ")
        if carid.isdigit():
            mycursor.execute("select * from cars where carid="+carid)
            test=mycursor.fetchone()
            if test==None:
                break
            else:
                print()
                print('------------------------')
                print('This Car ID already exists')
                print()
                print("Please enter another Car ID")
                print('------------------------')
                print()
        else:
            print()
            print('----------------------------')
            print('Please enter a integer value')
            print('----------------------------')
            print()
    while True:
        print()
        carname=input("Enter Carname :- ")
        if carname.isalpha():
            break
        else:
            print()
            print('--------------------------')
            print('Entered value is wrong')
            print()
            print("Please enter a valid input")
            print('--------------------------')
            print()
    while True:
        print()
        year=input("Enter Year :- ")
        if year.isdigit() and len(year)==4 and int(year)>1980 and int(year)<2030:
            break
        else:
            print()
            print('--------------------------')
            print('Please enter a valid year')
            print('--------------------------')
            print()
    while True:
        print()
        vehicletype=input("Enter Vehicletype :- ")
        if vehicletype.isalpha():
            break
        else:
            print()
            print('--------------------------')
            print('Entered value is wrong')
            print()
            print("Please enter a valid input")
            print('--------------------------')
            print()
    while True:
        print()
        charge=input("Enter Charge :- ")
        if charge.isdigit():
            break
        else:
            print()
            print('--------------------------')
            print('Entered value is wrong')
            print()
            print("Please enter a valid input")
            print('--------------------------')
            print()
    while True:
        print()
        extracharge=input("Enter Extracharge :- ")
        if extracharge.isdigit():
            break
        else:
            print()
            print('--------------------------')
            print('Entered value is wrong')
            print()
            print("Please enter a valid input")
            print('--------------------------')
            print()
    while True:
        print()
        colour=input("Enter Colour :- ")
        if colour.isalpha():
            break
        else:
            print()
            print('--------------------------')
            print('Entered value is wrong')
            print()
            print("Please enter a valid input")
            print('--------------------------')
            print()
    while True:
        print()
        make=input("Enter Make :- ")
        if make.isalpha():
            break
        else:
            print()
            print('--------------------------')
            print('Entered value is wrong')
            print()
            print("Please enter a valid input")
            print('--------------------------')
            print()
    mycursor.execute("insert into cars values({},'{}',{},'{}',{},{},'{}','{}')".format(carid,carname,year,vehicletype,charge,extracharge,colour,make))
    mydb.commit()
    mycursor.execute("select*from cars")
    y=mycursor.fetchall()
    print()
    print('*'*76)
    print("%10s"%"S.no","%12s"%"CarName","%10s"%"Year","%10s"%"Type","%10s"%"Price","%10s"%"Extra","%10s"%"Color","%12s"%"Make")
    print(' '*4,'-----'*18)
    if len(y)!=0:
        for i in y:
            print("%10s"%i[0],"%12s"%i[1],"%10s"%i[2],"%10s"%i[3],"%10s"%i[4],"%10s"%i[5],"%10s"%i[6],"%12s"%i[7])
            print(' '*4,'-----'*18)
    print('*'*76)
    print()
    print('-'*76)


def updatevehicle():
    print()
    print('\t'+' *'*14)
    print('\t WELCOME TO UPDATE SCREEN')
    print('\t'+' *'*14)
    print()
    while True:
        print('Update','  ','Choice')
        print("Carname     : 1")
        print("year        : 2")
        print("vehicletype : 3")
        print("Charge      : 4")
        print("Colour      : 5")
        print("Make        : 6")
        print("Exit        : 7")
        ch=input("Enter choice :- ")
        if ch=='1':
            updatecarname()
        elif ch=='2':
            updateyear()
        elif ch=='3':
            updatevehicletype()
        elif ch=='4':
            updatecharge()
        elif ch=='5':
            updatecolour()
        elif ch=='6':
            updatemake()
        elif ch=='7':
            break
        else:
            print()
            print('*'*16)
            print("  Wrong choice  ")
            print("Please Try Again")
            print('*'*16)
            print()

def updatecarname():
    while True:
        carid=input("Enter Car ID to update :- ")
        if carid.isdigit():
            mycursor.execute("select*from cars where carid="+carid)
            y=mycursor.fetchall()
            if y!=[]:
                print()
                print('*'*98)
                print("%10s"%"S.no","%12s"%"CarName","%10s"%"Year","%10s"%"Type","%10s"%"Price","%10s"%"Extra","%10s"%"Color","%12s"%"Make")
                print(' '*4,'-----'*18)
                for i in y:
                    print("%10s"%i[0],"%12s"%i[1],"%10s"%i[2],"%10s"%i[3],"%10s"%i[4],"%10s"%i[5],"%10s"%i[6],"%12s"%i[7])
                    print(' '*4,'-----'*18)
                print()
                print('*'*98)
                print()
                print('-'*98)
                break
            else:
                print()
                print('-----------------------------------')
                print("There is NO such record in the table")
                print('-----------------------------------')
                print()
    while True:
        print()
        carname=input("Enter carname :- ")
        if carname.isalpha():
            ans=input("Are you sure you want to update this record:(y/n)")
            if ans in ('Y','y'):
                mycursor.execute("update cars set carname='{}' where carid={}".format(carname,carid))
                mydb.commit()
                mycursor.execute("select*from cars where carid="+carid)
                y=mycursor.fetchall()
                if y!=[]:
                    print()
                    print('*'*76)
                    print("%10s"%"S.no","%12s"%"CarName","%10s"%"Year","%10s"%"Type","%10s"%"Price","%10s"%"Extra","%10s"%"Color","%12s"%"Make")
                    for i in y:
                        print("%10s"%i[0],"%12s"%i[1],"%10s"%i[2],"%10s"%i[3],"%10s"%i[4],"%10s"%i[5],"%10s"%i[6],"%12s"%i[7])
                    print(' '*4,'-----'*18)
                    print()
                    print('*'*76)
                    print()
                    print('-'*76)
                    break
            elif ans in ('n','N'):
                print()
                break
            else:
                print()
                print('Please Try Again')
                print()
        else:
            print('--------------------------')
            print("Please enter a valid value")
            print('--------------------------')


def updateyear():
    while True:
        carid=input("Enter Car ID to update :- ")
        if carid.isdigit():
            mycursor.execute("select*from cars where carid="+carid)
            y=mycursor.fetchall()
            if y!=[]:
                print()
                print('*'*76)
                print("%10s"%"S.no","%12s"%"CarName","%10s"%"Year","%10s"%"Type","%10s"%"Price","%10s"%"Extra","%10s"%"Color","%12s"%"Make")
                for i in y:
                    print("%10s"%i[0],"%12s"%i[1],"%10s"%i[2],"%10s"%i[3],"%10s"%i[4],"%10s"%i[5],"%10s"%i[6],"%12s"%i[7])
                    print(' '*4,'-----'*18)
                print()
                print('*'*76)
                print()
                print('-'*76)
                break
            else:
                print()
                print('-----------------------------------')
                print("There is NO such record in the table")
                print('-----------------------------------')
                print()
    while True:
        print()
        year=input("Enter year :- ")
        if year.isdigit()and len(year)==4 and int(year)>1980 and int(year)<2030:
            ans=input("Are you sure you want to update this record:(y/n)")
            if ans in ('Y','y'):
                mycursor.execute("update cars set year={} where carid={}".format(year,carid))
                mydb.commit()
                mycursor.execute("select*from cars where carid="+carid)
                y=mycursor.fetchall()
                if y!=[]:
                    print()
                    print('*'*76)
                    print("%10s"%"S.no","%12s"%"CarName","%10s"%"Year","%10s"%"Type","%10s"%"Price","%10s"%"Extra","%10s"%"Color","%12s"%"Make")
                    for i in y:
                        print("%10s"%i[0],"%12s"%i[1],"%10s"%i[2],"%10s"%i[3],"%10s"%i[4],"%10s"%i[5],"%10s"%i[6],"%12s"%i[7])
                    print(' '*4,'-----'*18)
                    print()
                    print('*'*76)
                    print()
                    print('-'*76)
                    break
            elif ans in ('n','N'):
                print()
                break
            else:
                print()
                print('Please Try Again')
                print()
        else:
            print('--------------------------')
            print("Please enter a valid value")
            print('--------------------------')

def updatevehicletype():
    while True:
        carid=input("Enter Car ID to update :- ")
        if carid.isdigit():
            mycursor.execute("select*from cars where carid="+carid)
            y=mycursor.fetchall()
            if y!=[]:
                print()
                print('*'*76)
                print("%10s"%"S.no","%12s"%"CarName","%10s"%"Year","%10s"%"Type","%10s"%"Price","%10s"%"Extra","%10s"%"Color","%12s"%"Make")
                for i in y:
                    print("%10s"%i[0],"%12s"%i[1],"%10s"%i[2],"%10s"%i[3],"%10s"%i[4],"%10s"%i[5],"%10s"%i[6],"%12s"%i[7])
                    print(' '*4,'-----'*18)
                print()
                print('*'*76)
                print()
                print('-'*76)
                break
            else:
                print()
                print('-----------------------------------')
                print("There is NO such record in the table")
                print('-----------------------------------')
                print()
    while True:
        print()
        vehicletype=input("Enter vehicletype :- ")
        if vehicletype.isalpha():
            ans=input("Are you sure you want to update this record:(y/n)")
            if ans in ('Y','y'):
                mycursor.execute("update cars set vehicletype='{}' where carid={}".format(vehicletype,carid))
                mydb.commit()
                mycursor.execute("select*from cars where carid="+carid)
                y=mycursor.fetchall()
                if y!=[]:
                    print()
                    print('*'*76)
                    print("%10s"%"S.no","%12s"%"CarName","%10s"%"Year","%10s"%"Type","%10s"%"Price","%10s"%"Extra","%10s"%"Color","%12s"%"Make")
                    for i in y:
                        print("%10s"%i[0],"%12s"%i[1],"%10s"%i[2],"%10s"%i[3],"%10s"%i[4],"%10s"%i[5],"%10s"%i[6],"%12s"%i[7])
                    print(' '*4,'-----'*18)
                    print()
                    print('*'*76)
                    print()
                    print('-'*76)
                    break
            elif ans in ('n','N'):
                print()
                break
            else:
                print()
                print('Please Try Again')
                print()
        else:
            print('--------------------------')
            print("Please enter a valid value")
            print('--------------------------')

def updatecharge():
    while True:
        carid=input("Enter Car ID to update :- ")
        if carid.isdigit():
            mycursor.execute("select*from cars where carid="+carid)
            y=mycursor.fetchall()
            if y!=[]:
                print()
                print('*'*76)
                print("%10s"%"S.no","%12s"%"CarName","%10s"%"Year","%10s"%"Type","%10s"%"Price","%10s"%"Extra","%10s"%"Color","%12s"%"Make")
                for i in y:
                    print("%10s"%i[0],"%12s"%i[1],"%10s"%i[2],"%10s"%i[3],"%10s"%i[4],"%10s"%i[5],"%10s"%i[6],"%12s"%i[7])
                    print(' '*4,'-----'*18)
                print()
                print('*'*76)
                print()
                print('-'*76)
                break
            else:
                print()
                print('-----------------------------------')
                print("There is NO such record in the table")
                print('-----------------------------------')
                print()
    while True:
        print()
        charge=input("Enter charge :- ")
        if charge.isdigit():
            ans=input("Are you sure you want to update this record:(y/n)")
            if ans in ('Y','y'):
                mycursor.execute("update cars set charge={} where carid={}".format(charge,carid))
                mydb.commit()
                mycursor.execute("select*from cars where carid="+carid)
                y=mycursor.fetchall()
                if y!=[]:
                    print()
                    print('*'*76)
                    print("%10s"%"S.no","%12s"%"CarName","%10s"%"Year","%10s"%"Type","%10s"%"Price","%10s"%"Extra","%10s"%"Color","%12s"%"Make")
                    for i in y:
                        print("%10s"%i[0],"%12s"%i[1],"%10s"%i[2],"%10s"%i[3],"%10s"%i[4],"%10s"%i[5],"%10s"%i[6],"%12s"%i[7])
                    print(' '*4,'-----'*18)
                    print()
                    print('*'*76)
                    print()
                    print('-'*76)
                    break
            elif ans in ('n','N'):
                print()
                break
            else:
                print()
                print('Please Try Again')
                print()
        else:
            print('--------------------------')
            print("Please enter a valid value")
            print('--------------------------')

def updatecolour():
    while True:
        carid=input("Enter Car ID to update :- ")
        if carid.isdigit():
            mycursor.execute("select*from cars where carid="+carid)
            y=mycursor.fetchall()
            if y!=[]:
                print()
                print('*'*76)
                print("%10s"%"S.no","%12s"%"CarName","%10s"%"Year","%10s"%"Type","%10s"%"Price","%10s"%"Extra","%10s"%"Color","%12s"%"Make")
                for i in y:
                    print("%10s"%i[0],"%12s"%i[1],"%10s"%i[2],"%10s"%i[3],"%10s"%i[4],"%10s"%i[5],"%10s"%i[6],"%12s"%i[7])
                    print(' '*4,'-----'*18)
                print()
                print('*'*76)
                print()
                print('-'*76)
                break
            else:
                print()
                print('-----------------------------------')
                print("There is NO such record in the table")
                print('-----------------------------------')
                print()
    while True:
        print()
        colour=input("Enter colour :- ")
        if colour.isalpha():
            ans=input("Are you sure you want to update this record:(y/n)")
            if ans in ('Y','y'):
                mycursor.execute("update cars set colour='{}' where carid={}".format(colour,carid))
                mydb.commit()
                mycursor.execute("select*from cars where carid="+carid)
                y=mycursor.fetchall()
                if y!=[]:
                    print()
                    print('*'*76)
                    print("%10s"%"S.no","%12s"%"CarName","%10s"%"Year","%10s"%"Type","%10s"%"Price","%10s"%"Extra","%10s"%"Color","%12s"%"Make")
                    for i in y:
                        print("%10s"%i[0],"%12s"%i[1],"%10s"%i[2],"%10s"%i[3],"%10s"%i[4],"%10s"%i[5],"%10s"%i[6],"%12s"%i[7])
                    print(' '*4,'-----'*18)
                    print()
                    print('*'*76)
                    print()
                    print('-'*76)
                    break
            elif ans in ('n','N'):
                print()
                break
            else:
                print()
                print('Please Try Again')
                print()
        else:
            print('--------------------------')
            print("Please enter a valid value")
            print('--------------------------')

def updatemake():
    while True:
        carid=input("Enter Car ID to update :- ")
        if carid.isdigit():
            mycursor.execute("select*from cars where carid="+carid)
            y=mycursor.fetchall()
            if y!=[]:
                print()
                print('*'*76)
                print("%10s"%"S.no","%12s"%"CarName","%10s"%"Year","%10s"%"Type","%10s"%"Price","%10s"%"Extra","%10s"%"Color","%12s"%"Make")
                for i in y:
                    print("%10s"%i[0],"%12s"%i[1],"%10s"%i[2],"%10s"%i[3],"%10s"%i[4],"%10s"%i[5],"%10s"%i[6],"%12s"%i[7])
                    print(' '*4,'-----'*18)
                print()
                print('*'*76)
                print()
                print('-'*76)
                break
            else:
                print()
                print('-----------------------------------')
                print("There is NO such record in the table")
                print('-----------------------------------')
                print()

    while True:
        print()
        make=input("Enter make :- ")
        if make.isalpha():
            ans=input("Are you sure you want to update this record:(y/n)")
            if ans in ('Y','y'):
                mycursor.execute("update cars set make='{}' where carid={}".format(make,carid))
                mydb.commit()
                mycursor.execute("select*from cars where carid="+carid)
                y=mycursor.fetchall()
                if y!=[]:
                    print()
                    print('*'*76)
                    print("%10s"%"S.no","%12s"%"CarName","%10s"%"Year","%10s"%"Type","%10s"%"Price","%10s"%"Extra","%10s"%"Color","%12s"%"Make")
                    for i in y:
                        print("%10s"%i[0],"%12s"%i[1],"%10s"%i[2],"%10s"%i[3],"%10s"%i[4],"%10s"%i[5],"%10s"%i[6],"%12s"%i[7])
                    print(' '*4,'-----'*18)
                    print()
                    print('*'*76)
                    print()
                    print('-'*76)
                    break
            elif ans in ('n','N'):
                print()
                break
            else:
                print()
                print('Please Try Again')
                print()
        else:
            print('--------------------------')
            print("Please enter a valid value")
            print('--------------------------')

def deletevehicle():
    while True:
        carid=input("Enter Car ID to delete :- ")
        if carid.isdigit():
            mycursor.execute("select*from cars where carid="+carid)
            y=mycursor.fetchall()
            if y!=[]:
                print()
                print('*'*76)
                print("%10s"%"S.no","%12s"%"CarName","%10s"%"Year","%10s"%"Type","%10s"%"Price","%10s"%"Extra","%10s"%"Color","%12s"%"Make")
                for i in y:
                    print("%10s"%i[0],"%12s"%i[1],"%10s"%i[2],"%10s"%i[3],"%10s"%i[4],"%10s"%i[5],"%10s"%i[6],"%12s"%i[7])
                    print(' '*4,'-----'*18)
                print()
                print('*'*76)
                print()
                print('-'*76)
                
            else:
                print()
                print('-----------------------------------')
                print('           SORRY !!                ')        
                print("There is NO such record in the table")
                print('-----------------------------------')
                print()
        print()
        ans=input("Are you sure you want to **DELETE** this record:(y/n)")
        if ans in ('Y','y'):
            mycursor.execute("delete from cars where carid="+carid)
            mydb.commit()
            mycursor.execute("select*from cars")
            y=mycursor.fetchall()
            if len(y)!=0:
                print()
                print('*'*98)
                if len(y)!=0:
                    print("%10s"%"S.no","%12s"%"CarName","%10s"%"Year","%10s"%"Type","%10s"%"Price","%10s"%"Extra","%10s"%"Color","%12s"%"Make")
                    print(' '*4,'-----'*18)
                    for i in y:
                        print("%10s"%i[0],"%12s"%i[1],"%10s"%i[2],"%10s"%i[3],"%10s"%i[4],"%10s"%i[5],"%10s"%i[6],"%12s"%i[7])
                        print(' '*4,'-----'*18)
                print('*'*98)
                print()
                print('-'*98)
                break
        elif ans in ('n','N'):
            break
        else:
            print('----------------')
            print('Please Try Again')
            print('----------------')
