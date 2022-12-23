from BD_core import *
#obj=DB()
objadmin=admin()

while 1:
    input_1 = int(input(
        "Enter the choice \n1.for add new user: \n2. for search the donor: \n3. for view all donors \n4. Update donor: \n5. Delete donor: \n\t Enter the choice:"))
    if input_1==1:


        name = input("Enter your name:")
        bg = input("enter the blood group:")
        location = input("enter the location: ")
        no = int(input("Enter the Ph.no:"))

        objadmin.create(name,bg,location,no)
        print("====================================================")




    elif input_1==2:

        blood_type = input("Enter the blood group:")
        loc=input("Enter the location:")
        objadmin.search(blood_type,loc)
        lst=objadmin.search(blood_type,loc)


        if lst==[]:
              print("\nOOP! No results found.")
              print("\n===========================================")
        else:
              print('\n',len(lst),"result(s) found.\n\n")
              for x,y in enumerate(lst):
                  print(x+1,')',sep='')
                  print("Name:",y[0],"\nBlood group:",y[1],"\nLocation:",y[2],"\nContact:",y[3],'\n')
              print("\n===========================================")


        #print( objadmin.search(blood_type,loc))



    elif input_1==3:
        objadmin.all_donor()


        print(  objadmin.all_donor())
    elif input_1==4:
        ch = int(input(
            "Enter the choice \n\t 1. For change name \n\t2. for change blood group \n\t3. for change location \n\t4. change no \n\tEnter your choice:"))
        obj_update = update()
        if(ch==1):

            old = input("Enter the  Name:")
            new = input("Enter the new name:")
            obj_update.update_name(old,new)

        if (ch == 2):

            old = input("Enter the old Name:")
            new = input("Enter the new Blood Group:")
            obj_update.update_bloodgroup(old, new)



        if (ch == 3):

            old = input("Enter the  Name:")
            new = input("Enter the new  Location:")
            obj_update.update_location(old, new)
        if (ch == 4):

            old = input("Enter the  Name :")
            new = input("Enter the new Phone No:")
            obj_update.update_no(old, new)


    #elif input_1==5:
        #print("Enda ipadi delelte pandringaa pera pasangla thatha soldra kelulnga da")
        #objadmin.delete()
    else:
        print("Invalid selection")

