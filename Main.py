print('\t','*'*50,'\t')
print('\t\tWelcome to Vehicle Management System\t\t')
print('\t','*'*50,'\t')
import admin
import cust
adminusers=['Manager','Adminstaff','Cashier']
passwrd=['1111','2222','3333']
def  main():
    print()
    print()
    print('\t\t','*'*30,'\t')
    print('\t\t\tLOGIN IN SCREEN\t\t')
    print('\t\t','*'*30,'\t')
    while True:
        print()
        print('Please enter any of the following choice to continue')
        print("Admin      : 1")
        print("Customer   : 2")
        print()
        x=input("Enter choice :-- ")
        if x=='1':
            adminlogin()
        elif x=='2':
            cust.selectvehicle()
        else:
            print()
            print('*'*16)
            print("  Wrong choice  ")
            print("Please Try Again")
            print('*'*16)
            print()
def adminlogin():
    user=input("Enter User Name :--  ")
    pin=input("Enter pin       :--  ")
    if user in adminusers:
        if pin in passwrd:
            if user==adminusers[0] and pin==passwrd[0]:
                print()
                print('\t','*'*17)
                print("\t LOGIN SUCCESSFULL")
                print('\t','*'*17)
                admin_m()
            elif user==adminusers[1] and pin==passwrd[1]:
                print()
                print('\t','*'*17)
                print("\t LOGIN SUCCESSFULL")
                print('\t','*'*17)
                admin_m()
            elif user==adminusers[2] and pin==passwrd[2]:
                print()
                print('\t','*'*17)
                print("\t LOGIN SUCCESSFULL")
                print('\t','*'*17)
                admin_m()
            else:
                print()
                print('----------------')
                print("Please Try Again")
                print('----------------')
                print()
        else:
            print()
            print('----------------')
            print("INVALID PASSWORD")
            print('----------------')
            print()
    else:
        print()
        print('----------------')
        print("INVALID USERNAME")
        print("Please Try Again")
        print("----------------")
        print()
def admin_m():
    while True:
        print()
        print('Please enter any of the following choice to continue')
        print("Add vehicle    : 1")
        print("Update vehicle : 2")
        print("Delete vehicle : 3")
        print("Select vehicle : 4")
        print("Exit           : 5")
        print()
        x=input("Enter choice :- ")
        if x=='1':
            admin.addvehicle()
        elif x=='2':
            admin.updatevehicle()
        elif x=='3':
            admin.deletevehicle()       
        elif x=='4':
            cust.selectvehicle()
        elif x=='5':
            break
        else:
            print()
            print('*'*16)
            print("  Wrong choice  ")
            print("Please Try Again")
            print('*'*16)
            print()
main()
