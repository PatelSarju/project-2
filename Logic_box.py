import os
print("Welcome to the Pattern Generator and Number Analyzer!")

is_on=True

while is_on:
    choice=int(input("\nSelect an option:\n1. Generate a Pattern\n2. Analyze a range of Numbers\n3. Exit\nEnter your choice:"))
    os.system('cls')
    
    if choice==1:
        pattern_type=int(input("\nChoose a pattern type:\n1. Left-angled Triangle\n2. Pyramid\n3. Right-angled Triangle\nEnter your choice:"))
        os.system('cls')
        
        if pattern_type==1:
            rows=int(input("\nEnter the number of rows:"))
            os.system('cls')
            
            # Left-angled Triangle
            print("\nPattern:")
            for i in range(1,rows+1):
                for k in range(rows,i,-1):
                    print(" ",end="")
                for j in range(1,i+1):
                    print("*",end="")
                print()
        
        elif pattern_type==2:
            rows=int(input("\nEnter the number of rows:"))
            os.system('cls')
            
            # Pyramid
            print("\nPattern:")
            for i in range(1,rows+1):
                for k in range(rows,i,-1):
                    print(" ",end="")
                for j in range(1,i+1):
                    print("* ",end="")
                print()
        
        elif pattern_type==3:
            rows=int(input("\nEnter the number of rows:"))
            os.system('cls')
            
            # Right-angled Triangle
            print("\nPattern:")
            for i in range(1,rows+1):
                for j in range(1,i+1):
                    print("*",end="")
                print()
            
        else:
            print("\nYou entered the invalid input!")
    
    elif choice==2:
        start=int(input("\nEnter the start of the range:"))
        end=int(input("Enter the end of the range:"))
        total=0
        for i in range(start,end+1):
            if i%2==0:
                print(f"Number {i} is Even")
            else:
                print(f"Number {i} is Odd")
            total+=i
        print(f"Sum of all numbers from {start} to {end} is:{total}")
    
    elif choice==3:
        print("\nExiting the program. Goodbye!")
        is_on=False
    
    else:
        print("\nYou entered the wrong choice, you are exiting from the program!")
        is_on=False