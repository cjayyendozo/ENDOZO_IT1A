
def act21():
    tuloy = True
    count = 0

    while tuloy == True:
        name = input("Please enter a name ---> ")
        
        if name.lower() == "stop":
            print("Loop has now stopped")
            print(f"You have entered {count} number")
            break
            
    else:
            count += 1