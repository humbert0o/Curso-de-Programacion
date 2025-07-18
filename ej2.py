#ej2 
num1= int(input("escribe un numero: "))
num2= int(input("escribe otro numero: "))
num3= int(input("escribe otro numero: ")) 

if num1 > num2 and num1> num3: 
    print(f"el primer numero: {num1} es el mayor")
elif  num1 < num2 and num1< num3: 
    print(f"el primer numero: {num1} es el menor")
if num2 > num1 and num2> num3: 
    print(f"el segundo numero: {num2} es el mayor")
elif  num2 < num1 and num2< num3: 
    print(f"el segundo numero: {num2} es el menor")
if num3 > num1 and num3> num2: 
    print(f"el tercer numero: {num3} es el mayor")
elif  num3 < num1 and num3< num2: 
    print(f"el tercer numero: {num3} es el menor")
