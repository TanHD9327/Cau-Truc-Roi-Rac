import math, string
def calculate1(a, b, op):
    if op == "+":
        answer = a + b
    if op == "-":
        answer = a - b
    if op == "*":
        answer = a * b
    if op == "/":
        answer = a / b
    if op == "%":
        answer = a % b
    if op == "^":
        answer = a**b
    return answer
    
def calculate2(a, b, op):
   d = {
   		'+' : a+b, 
  	 	'-' : a-b, 
 	  	'*' : a*b,  
 	  	'/' : a/b, 
 	  	'%' : a%b, 
	   	'^' : a**b
   		}
   return d[op]


def exercise1():
    a = 15 * 2 + 7 * 8
    b = 20 -  15 + 15*2
    c = 20 + 30  - 3 * 15 + 5 * 52
    d = (4/6 + 2/6) / (5/2 + 1/2)
    e = 14/2 + 7
    f = (5*2) / (5 - 20 * 3**2 + 30)
    values = {"a": a, "b": b, "c": c, "d": d, "e": e, "f": f} 
    for left, right in values.items(): 
        print(f"{left} = {right}")

def exercise2(): 
    print("a. 15 * 2 + 7 * 8 =", 15 * 2 + 7 * 8) 
    print("b. 20 - 15 + 15*2 =", 20 - 15 + 15*2) 
    print("c. 20 + 30 - 3*15 + 5*52 =", 20 + 30 - 3*15 + 5*52) 
    print("d. (4/6 + 2/6) / (5/2 + 1/2) =", (4/6 + 2/6) / (5/2 + 1/2)) 
    print("e. 14/2 + 7 =", 14/2 + 7) 
    print("f. (5*2) / (5 - 20 * 3**2 + 30) =", (5*2) / (5 - 20 * 3**2 + 30))

def exercise3():
    n = int(input("Enter an integer: "))
    total = 0
    if n >= 0:
        for i in range(0, n+1):
            total += i
    else:
        for i in range(0, n-1, -1):
            total += i

    print(f"sumN({n}) = {total}")
def exercise4():
    A = input("Input your string: ")
    B = A.split()
    C = "_".join(B)
    D = "".join(B)
    print(f"(a) = {D}")
    print(f"(b) = {C}")

def exercise5():
    operation = input("Input an operation between 2 postive integers: ")
    num1, op, num2 = operation.split()
    num1, num2 = int(num1), int(num2)
    answer = calculate1(num1, num2, op) 
    print(f"{num1} {op} {num2} = {answer}")

def exercise6():
    operation = input("Input an operation between 2 postive integers: ")
    num1, op, num2 = operation.split()
    num1, num2 = int(num1), int(num2)
    answer = calculate2(num1, num2, op) 
    print(f"{num1} {op} {num2} = {answer}")
def exercise7():
    a = 1
def exercise8():
    a = 1
def exercise9():
    a = 1

def main():
    choice = int(input("Enter exercise from 1 to 9: "))
    match choice:
        case 1:  
            print("---------Exercise 1---------")
            exercise1()
        case 2:  
            print("---------Exercise 2---------")
            exercise2()
        case 3:  
            print("---------Exercise 3---------")
            exercise3()
        case 4:  
            print("---------Exercise 4---------")
            exercise4()
        case 5:  
            print("---------Exercise 5---------")
            exercise5()
        case 6:  
            print("---------Exercise 6---------")
            exercise6()
        case 7:  
            print("---------Exercise 7---------")
            exercise7()
        case 8:  
            print("---------Exercise 8---------")
            exercise8()
        case 9:  
            print("---------Exercise 9---------")
            exercise9()
main()