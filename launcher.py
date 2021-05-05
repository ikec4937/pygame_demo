import finished_class as foop #Finished: OOP
import finished_functional as fpro #Finished: Functional

def launcher_main():
    print("Which file are you running? 1. Procedural \n2. Object-Oriented")
    sel = int(input("-> "))
    if sel == 1:
        foop.main()
    elif sel == 2:
        fpro.main()
    else:
        print("INVALID input")
        launcher_main()
launcher_main()