import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="agentbp",database="vehicle")
mycursor=mydb.cursor()
def selectvehicle():
    print()
    print('\t\t','*'*30,'\t')
    print('\t\t\tSELECTION  SCREEN\t\t')
    print('\t\t','*'*30,'\t')
    print()
    while True:
        print()
        print("SELECT BY              CHOICE")
        print()
        print("Select by Year          : 1")
        print("Select by Vehicletype   : 2")
        print("Select by Charge        : 3")
        print("Select by Colour        : 4")
        print("Select by Make          : 5")
        print("Exit                    : 6")
        print()
        x=input("Enter choice :>> ")
        if x.isdigit():
            if x=='1':
                selectyear()
            elif x=='2':
                selectvehicletype()
            elif x=='3':
                selectcharge()
            elif x=='4':
                selectcolour()
            elif x=='5':
                selectmake()
            elif x=='6':
                break
            else:
                print()
                print('*'*16)
                print("  Wrong choice  ")
                print("Please Try Again")
                print('*'*16)
                print()
        else:
            print()
            print("Please Try again")
            print()
def selectyear():
    year=input("Enter Year :- ")
    if year.isdigit():
        mycursor.execute("select*from cars where year="+year)
        y=mycursor.fetchall()
        if len(y)!=0:
            print()
            print('*'*76)
            print("CarID",'\t',"CarName",'\t',"Year",'\t',"Type",'\t',"Price",'\t',"Extra",'\t',"Color",'\t',"Make")
            for i in y:
                for j in i:
                    print(j,end=" \t ")
                print()
            print('*'*76)
            print()
            print('-'*76)
            print()
        else:
            print()
            print("             SORRY!!             ")
            print("There is NO record with this YEAR")
            print("---------------------------------")
    else:
        print()
        print("Try again")
        print()
        selectyear()
def selectvehicletype():
    vehicletype=input("Enter Vehicletype :- ")
    if vehicletype.isalpha():
        mycursor.execute("select*from cars where vehicletype='{}'".format(vehicletype))
        y=mycursor.fetchall()
        if len(y)!=0:
            print()
            print('*'*76)
            print("CarID",'\t',"CarName",'\t',"Year",'\t',"Type",'\t',"Price",'\t',"Extra",'\t',"Color",'\t',"Make")
            for i in y:
                for j in i:
                    print(j,end=" \t ")
                print()
            print('*'*76)
            print()
            print('-'*76)
            print()
        else:
            print()
            print("                  SORRY!!             ")
            print("There is NO record with this VEHICLETYPE")
            print("----------------------------------------")
    else:
        print()
        print("Try again")
        print()
        selectvehicletype()
def selectcharge():
    charge=input("Enter Charge :- ")
    if charge.isdigit():
        mycursor.execute("select*from cars where charge="+charge)
        y=mycursor.fetchall()
        if len(y)!=0:
            print()
            print('*'*76)
            print("CarID",'\t',"CarName",'\t',"Year",'\t',"Type",'\t',"Price",'\t',"Extra",'\t',"Color",'\t',"Make")
            for i in y:
                for j in i:
                    print(j,end=" \t ")
                print()
            print('*'*76)
            print()
            print('-'*76)
            print()
        else:
            print()
            print("               SORRY!!             ")
            print("There is NO record with this CHARGE")
            print("-----------------------------------")
    else:
        print()
        print("Please try again")
        print()
        selectcharge()
def selectcolour():
    colour=input("Enter Colour :- ")
    if colour.isalpha():
        mycursor.execute("select*from cars where colour='{}'".format(colour))
        y=mycursor.fetchall()
        if len(y)!=0:
            print()
            print('*'*76)
            print("CarID",'\t',"CarName",'\t',"Year",'\t',"Type",'\t',"Price",'\t',"Extra",'\t',"Color",'\t',"Make")
            for i in y:
                for j in i:
                    print(j,end=" \t ")
                print()
            print('*'*76)
            print()
            print('-'*76)
            print()
        else:
            print()
            print("              SORRY!!             ")
            print("There is NO record with this COLOUR")
            print("-----------------------------------")
    else:
        print()
        print("Try again")
        print()
        selectcolour()
def selectmake():
    make=input("Enter Make :- ")
    if make.isalpha():
        mycursor.execute("select*from cars where make='{}'".format(make))
        y=mycursor.fetchall()
        if len(y)!=0:
            print()
            print('*'*76)
            print("CarID",'\t',"CarName",'\t',"Year",'\t',"Type",'\t',"Price",'\t',"Extra",'\t',"Color",'\t',"Make")
            for i in y:
                for j in i:
                    print(j,end=" \t ")
                print()
            print('*'*76)
            print()
            print('-'*76)
            print()
        else:
            print()
            print("             SORRY!!             ")
            print("There is NO record with this MAKE")
            print("---------------------------------")
    else:
        print()
        print('Try again')
        print()
        selectmake()
