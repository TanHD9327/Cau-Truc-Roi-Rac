

def ex1():
    print("---------------Exercise 1---------------")
    p= bool(input("Input logic for p: "))
    q= bool(input("Input logic for q: "))
    r= bool(input("Input logic for r: "))
    print("1. p → q = ", not p or q)
    print("2. p ^ q = ", not p and q)
    print("3. p ^ (q ^ r) = ", p and (q and r))
    print("4. p ^ (¬q v r) = ", p and (not q or r))



def ex2():
    print()
    print(f"{'p':<6} \t {'q':<6} \t {'¬p':<6} \t {'p ^ q':<6} \t  {'p v q':<6} \t {'p → q':<6} \t {'¬p ^ q':<7} \t {'¬p v q → ¬q':<11} \t {'(p v q) v (¬p ^ q) → q':<22}")
    print("===================================================================================================================================================")
    for p in [True, False]:
        for q in [True, False]:
            print(f"{str(p):<6} \t "
                  f"{str(q):<6} \t "
                  f"{str(not p):<6} \t "
                  f"{str(p and q):<6} \t "
                  f"{str(p or q):<6} \t "
                  f"{str(not p or q):<6} \t "
                  f"{str(not p and q):<6} \t "
                  f"{str(not(not p or q) or not q):<11} \t "
                  f"{str(not((p or q) or (not p and q)) or q):<22} ")
    print()

def ex3_4():
    true = [True]
    false = [False]
    tautology = True
    contradiction = True
    expressions = [
        (),
        (),
        (),
        ()
    ]
    for p in [True, False]:
        for q in [True, False]:
            a = p or not q
            b = p and not p
            c = (p and q) or (not p or (p and not q))
            d = (p and not q) and (not p or q)
            if (a not in true):
                tautology = False
            if (a not in false and tautology == True ):
                contradiction = False

    if (tautology):
        print("This function is tautology")
    elif (contradiction):
        print("This function is contradiction")
    elif (not tautology and not contradiction):
        print("This function is contingency")

def main():
    choice = int(input("Enter exercise: "))
    match choice:
        case 1: ex1()
        case 2: ex2()
        case 3: ex3_4()
        case 4: ex3_4()
        case 5: ex5()
        case 6: ex6()
        case 7: ex7()
        case 8: ex8()

main()