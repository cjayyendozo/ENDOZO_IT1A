def cc11():

    for x in range (1,5):
        for a in range(4,x,-1): 
            print(" ", end = " ")
        for b in range(1,x): 
            print("*", end =" ")
        for c in range(0,x):
            print("*",end =" ")
        print()

    #arrow down

    for y in range (1,4):
        for d in range(0,y): 
            print(" ", end = " ")
        for e in range (4,y,-1): 
            print("*",end = " ")
        for f in range(3,y,-1):
            print("*",end =" ")
        print()
        

        
