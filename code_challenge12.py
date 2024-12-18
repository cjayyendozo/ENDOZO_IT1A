
def cc12():
    for a in range (1,5):
        for b in range(4, a,-1): 
            print(" ", end = " ")

        for c in range(0, a+1): 
            print("*", end =" ")
        for d in range(1,a):
            print ("*",end =" ")
        print()

    #arrow down

    for x in range(1,7):
            #print("*", end=" ")
        for y in range(1,4): 
            print(" ", end = " ")
        for z in range(1,3):
            print("*",end=" ")
        print()