from sum import *
class Calc:
     def __init__(self):
        self.num = []
        self.n=0
         
     def Innput(self):
        self.n=int(input("Enter the number of elements you want to add\n"))
        for x in range(0,self.n):
            y=input("Enter the number \n")
            self.num.append(y)

obj1=Calc()
obj1.Innput()
number=obj1.num
# print(number)
# print(type(number))
print(f'The sum is {sum(number)}')


