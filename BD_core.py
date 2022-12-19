import numpy as np
class DB:

    """
    import numpy as np

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
entries = list(map(int, input().split()))

# For printing the matrix
matrix = np.array(entries).reshape(R,C)
print(matrix)"""
    def create(self,lst2):
        global name,bg,location,no,R,C
        R = 4
        C = int(input("Enter the number of columns:"))

        name=input("Enter your name:")
        bg=input("enter the blood group")
        location=input("enter the location ")
        no=int(input("Enter the Ph.no"))

        entries = list(map(int, input().split("\n")))
        matrix = np.array(entries).reshape(R, C)
        lst =[name,bg,location,no]

        lst2.extend(lst)
        #lst.append(name,bg,location,no)
        print(lst2)
        return("Add Operation")
    #def create(self,name,bg,location,no):
    def update(self):
        return ("update Operation")

    def search(self):
        return("result ")

    def delete(self):
        return("delete Operation")



class user(DB):

    def login(self):
        global name, password
        name=str(input("    \n\tEnter the Username :"))
        password=input("\n\tEnter the password :")
        print("\n\tLogined")
    def signup(self):
        name1 = str(input("    \n\tEnter the Username :"))
        password1 = input("\n\tEnter the password :")
        if name1==name or password1  == password:
            print("\n\t signin succesfully")
    def log_out(self):
        return("Log Out")
    def user_details(self):
        return('succesfully submitted')

class admin(user):
    def send(self):
        return "Alert sended"
   
    def request(self):
        return("request sended")
    def bd_view(self):
        #IT WILL SEARCH FOR THE DONOR
        obj_DB.search()
        obj_DB.create()
        obj_DB.update()
        obj_DB.delete()
        #login and logout
        obj_DB.login()
        obj_DB.log_out()

        return("bd values")

obj_DB=admin()