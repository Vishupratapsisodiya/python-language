print ("~~**~~Mini Calculator~~**~~")

num1 = float(input("enter first numer here: "))
num2 = float(input("enter second numer here: "))

print ("press 1 for addition \npress 2 for subtraction \npress 3 for multiplication \npress 4 for division")

choice = int(input("enter your choice from 1-4: "))

if choice == 1:
    print ("the addition of given two number is" ,num1 + num2)
elif choice == 2:
    print ("the subtraction of given two number is" ,num1 - num2) 
elif choice == 3:
    print ("the multiplication of given two number is" ,num1 * num2) 
elif choice == 4:
    print ("the division of given two number is" ,num1 / num2) 
else:
    print ("Invalid Input") 