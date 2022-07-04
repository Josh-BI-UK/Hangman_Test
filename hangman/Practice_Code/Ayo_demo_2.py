# print('Pick a number')
# raw_input = input()
# str_input = str(raw_input)
# #print('str_input =', str_input)
# i = True
# while i ==  True:
#     if str_input.isalpha():
# 	    print('Please only enter numbers')
#         i == True
#     else:
#         Sum_example = 2 * float(raw_input)
#         print('2 x ',raw_input,' = ',Sum_example)

# class Person:
#   def __init__(self, fname, age):
#     self.fname = fname
#     self.age = age
    
#     def is_pensionior(self):
#         if self.age > 38:
#             print(self.fname,'Is an old Gee')
#         else:
#             print(self.fname,'Is a young buck')

#     def Check_if_old(Person):
#         Ayo.is_pensionior()


    if __name__ == '__main__':
        Ayo = Person('Azeez', 39)
        Ayo.Check_if_old(self)


        __name__ == '__main__'
        # Suppose this is foo.py.

print("before import")
import math

print("before function_a")
def function_a():
    print("Function A")

print("before function_b")
def function_b():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    function_a()
    function_b()
print("after __name__ guard")