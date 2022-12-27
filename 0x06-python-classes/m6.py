#!/usr/bin/python3

Square = __import__('101-square').Square



my_square_1 = Square(3)

my_square_1.my_print()



print("--")



my_square_2 = Square(1, (1,1))

my_square_2.my_print()



print("--")



my_square_3 = Square(3, (3,2))

print(my_square_3)



print("--")
