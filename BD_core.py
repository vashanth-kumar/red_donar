
class DB:
    global m
    m = [["banu", "b+", "erode", 7373], ["deeksha", "a+", "erode", 7374], ["karthi", "b+", "erode", 7375],
         ["sarvanan", "o+", "erode", 7376]]
    #m=[]
    def create(self):
        global name, bg, location, no, k, m
        k = int(input("Enter the no of donor's need to be added:"))

        for i in range(k):
            a = []
            name = input("Enter your name:")
            bg = input("enter the blood group:")
            location = input("enter the location: ")
            no = int(input("Enter the Ph.no:"))

            a.append(name)
            a.append(bg)
            a.append(location)
            a.append(no)
            print("Recorded updated succesfully")
            m.append(a)
            for i in m:
                print(i, end=" \n")
            print("====================================================")

    #def create(self,name,bg,location,no):
    def update(self):
        ch = int(input("Enter the choice \n 1. For change name \n2. for change blood group \n3. for change location \n4. change no \nEnter your choice:"))

        if ch == 1:
            name = input("Enter the name:")
            for i in range(len(m)):

                if m[i][0] == name:
                    x = input("Enter the new name:")
                    m[i][0] = x
                    print(m[i])
                    print("=====Details Updated=====")

        if ch == 2:
            name = input("Enter the name:")
            for i in range(len(m)):

                if m[i][0] == name:
                    x = input("Enter the new blood group:")
                    m[i][1] = x
                    print(m[i])
                    print("=====Details Updated=====")

        if ch == 3:
            name = input("Enter the name:")
            for i in range(len(m)):

                if m[i][0] == name:
                    x = input("Enter the new address:")
                    m[i][2] = x
                    print(m[i])
                    print("=====Details Updated=====")

        if ch == 4:
            name = input("Enter the name:")
            for i in range(len(m)):

                if m[i][0] == name:
                    x = input("Enter the no:")
                    m[i][3] = x
                    print(m[i])
                    print("=====Details Updated=====")
        else:
            print("Invalid selection")



    def search(self):
        #print(m)

        blood_type = input("Enter the blood group:")

        for i in range(len(m)):
           # print(m[i][1])
            if m[i][1] == blood_type:
                print(m[i])
        print("====================================================")


    def all_donor(self):
        print("======Total Donar======")
        for i in m:
            print(i, end=" \n")

    def delete(self):
        name = input("\nEnter the name:")
        for i in range(len(m)):

            if m[i][0] == name:
                del m[i]
                for i in m:
                    print(i, end=" \n")

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