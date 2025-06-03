import Pyro4

num1 = float (input("Enter The First Number: "))
num2 = float (input("Enter The Second Number: "))
print ("A List Of Available Mathematical Operations \n")
print ("1.Multiple ")
print ("2.Divide ")
print ("3.Substract ")
print ("4.Add \n")
opr = int (input("Enter Your Choice (1,2,3,4): "))

hitung = Pyro4.Proxy("PYRONAME:penghitung")

if opr==1:
    print ("Result: ")
    print (hitung.Mul_func(num1,num2))
elif opr==2:
    print ("Result: ")
    print (hitung.Div_func(num1,num2))
elif opr==3:
    print ("Result: ")
    print (hitung.Sub_func(num1,num2))
elif opr==4:
    print ("Result: ")
    print (hitung.Add_func(num1,num2))
else:
    print ("\n Error : Mathematical Operations Input doesn't match With The List!")
