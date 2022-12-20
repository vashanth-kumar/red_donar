from BD_core import *
obj=DB()
obj=admin()

while 1:
    input_1 = int(input(
        "Enter the choice\n1.for add new user: \n2. for search the donor: \n3. for view all donors \n4. Update donor: \n5. Delete donor: \n\t Enter the choice:"))
    if input_1==1:

        obj.create()
    elif input_1==2:
        obj.search()
    elif input_1==3:
        obj.all_donor()
    elif input_1==4:
        obj.update()
    elif input_1==5:
        obj.delete()
    else:
        print("Invalid selection")

