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

    def create(self):
        global name, bg, location, no, R, C
        R = 4
        C = int(input("Enter the number of columns:"))

        name = input("Enter your name:")
        bg = input("enter the blood group")
        location = input("enter the location ")
        no = int(input("Enter the Ph.no"))
        lst = [name, bg, location, no]

        entries = list(map(str, input().split()))
        matrix = np.array(entries).reshape(R, C)
        print(matrix)

b=DB()
b.create()