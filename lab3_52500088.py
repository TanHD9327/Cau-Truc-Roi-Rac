def isPrime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
            else:
                return True
def isAllPositive(list):
    return all(number > 0 for number in list)

def isAllEven(list):
    return all(number % 2 == 0 for number in list)
def ex1():
    print("---- Exercise 1 ----")
    list1 = [2, 1, 4, 1, 2, 3, 5, 6]
    list2 = [-1, 2, 5, 7, 2, 6, 4 ,7]
    list3 = [-1, 2, 5, 0, 2, 6, 5, 2]


    print(f"All numbers in list1 are positive -> {all(number > 0 for number in list1)}")
    print(f"All numbers in list2 are positive -> {all(number > 0 for number in list2)}")
    print(f"All numbers in list3 are positive -> {all(number > 0 for number in list3)}")

def ex2():
    print("---- Exercise 2 ----")
    list1 = [11, 1, 17, 1, 3, 3, 5, 13]
    list2 = [-1, 2, 5, 7, 3, 9, 7 ,7]
    list3 = [0, 2, 4, 6, 8, 10, 12]

    print(f"There is at least one even number in list1 -> {any(number % 2 == 0 for number in list1)}")
    print(f"There is at least one even number in list2 -> {any(number % 2 == 0 for number in list2)}")
    print(f"There is at least one even number in list3 -> {any(number % 2 == 0 for number in list3)}")

def ex3():
    print("---- Exercise 3 ----")
    list1 = [11, 1, 17, 1, 3, 3, 5, 13]
    list2 = [-1, 2, 5, 7, 3, 9, 7 ,7]
    list3 = [0, 2, 4, 6, 8, 10, 12]

    print(f"Not all numbers in list1 are even -> {any(number % 2 != 0 for number in list1)}")
    print(f"Not all numbers in list2 are even -> {any(number % 2 != 0 for number in list2)}")
    print(f"Not all numbers in list3 are even -> {any(number % 2 != 0 for number in list3)}")

def ex4():
    print("---- Exercise 4 ----")
    list1 = [11, 1, 17, 1, 3, 3, 5, 13]
    list2 = [-1, 2, 5, 7, 3, 9, 7 ,7]
    list3 = [0, 2, 4, 6, 8, 10, 12]

    print(f"There exists at least one prime number in list1 -> {any(isPrime(number) for number in list1)}")
    print(f"There exists at least one prime number in list2 -> {any(isPrime(number) for number in list2)}")
    print(f"There exists at least one prime number in list3 -> {any(isPrime(number) for number in list3)}")

def ex5():
    print("---- Exercise 5 ----")
    list1 = [[10, 1, 16], [2, 4, 6], [2, 10 , 6]]
    list2 = [[-1, 2, 5], [7, 3, 9], [7 ,7, 0]]
    list3 = [[0, 2, 4], [6, 8, 10], [12, 14, 16]]

    print(f"Every list in list1 contains at least one even number -> {all(any(number % 2 == 0 for number in sublist) for sublist in list1)}")
    print(f"Every list in list2 contains at least one even number -> {all(any(number % 2 == 0 for number in sublist) for sublist in list2)}")
    print(f"Every list in list3 contains at least one even number -> {all(any(number % 2 == 0 for number in sublist) for sublist in list3)}")

def ex6():
    print("---- Exercise 6 ----")
    list1 = [11, 1, 17, 1, 3, 3, 5, 13]
    list2 = [10, 9, 8, 7, 6, 5, 4 ,3]
    list3 = [0, 2, 4, 6, 8, 10, 12]

    print(f"For every number x in list1, there exists a number y in list1 that is greater than x -> {all(any(y > x for y in list1) for x in list1)}")
    print(f"For every number x in list2, there exists a number y in list2 that is greater than x -> {all(any(y > x for y in list2) for x in list2)}")
    print(f"For every number x in list3, there exists a number y in list3 that is greater than x -> {all(any(y > x for y in list3) for x in list3)}")

def ex7():
    print("---- Exercise 7 ----")
    list1 = [11, 1, 17, 1, 3, 3, 5, 13]
    list2 = [10, 9, 8, 7, 6, 5, 4 ,3]
    list3 = [0, 2, 4, 6, 8, 10, 12]

    print(f"For every number x in list1, there exists a number y in list1 that x + y is divisible by 5 and y is greater than x -> {all(any((x + y) % 5 == 0 and y > x for y in list1) for x in list1)}")
    print(f"For every number x in list2, there exists a number y in list2 that x + y is divisible by 5 and y is greater than x -> {all(any((x + y) % 5 == 0 and y > x for y in list2) for x in list2)}")
    print(f"For every number x in list3, there exists a number y in list3 that x + y is divisible by 5 and y is greater than x -> {all(any((x + y) % 5 == 0 and y > x for y in list3) for x in list3)}")
def ex8():
    list1 = [(11, 1), (17, 1), (3, 3), (5, 13)]
    list2 = [(-1, 2), (5, 7), (5, 9), (7 ,7)]
    list3 = [(0, 2), (4, 6), (8, 10), (0, 3)]

    
    print(isFunc(list1))
    print(isFunc(list2))
    print(isFunc(list3))
    

    def isFunc(pair):
        first_x = {}
        for x, y in pair:

            if x in first_x:
                first_x.append[x] 
                    
                
def main():
    ex1()
    print()
    ex2()
    print()
    ex3()
    print()
    ex4()
    print()
    ex5()
    print()
    ex6()
    print()
    ex7()
    print()
    ex8()
    print()

main()