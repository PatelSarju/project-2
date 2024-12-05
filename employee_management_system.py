print("Welcome to the employee management system!")

employee_list=[]
id_set=set({})
emp_id_set=set({})

is_on=True

while is_on:
    choice=int(input("\nPress 1 for add new employee data\nPress 2 for fetch the all employee data\nPress 3 for fetch single employee data\nPress 4 for update the employee data\nPress 5 for delete the employee data\nPress 6 for exit from the management system\nEnter the your choice:"))
    
    if choice==1:
        total_emp=int(input("\nHow many employee's data you want to add:"))
        for i in range(total_emp):
            emp_id=int(input(f"\n{i+1}. Enter the employee id:"))
            while emp_id in id_set:
                print("\nThis id already exist in the system!")
                print("Please enter the new employee id!")
                emp_id=int(input(f"\n{i+1}. Enter the employee id:"))
            else:
                id_set.add(emp_id)
            emp_name=input(f"{i+1}. Enter the employee name:").title()
            emp_age=int(input(f"{i+1}. Enter the employee age:"))
            emp_role=input(f"{i+1}. Enter the employee job role:").title()
            emp_salary=int(input(f"{i+1}. Enter the employee salary:"))
            print("\nNew employee data stored successfully!")
            employee_list.append({'Id':emp_id,'Name':emp_name,'Age':emp_age,'Job_role':emp_role,'Salary':emp_salary})

    if choice==2:
        print("\nAll employee data is given below:\n")
        print(f"{'Id':^10} | {'Name':^20} | {'Age':^5} | {'Job_role':^20} | {'Salary':^10}")
        print("-" * 75)
        for i in employee_list:
            print(f"{i['Id']:^10} | {i['Name']:^20} | {i['Age']:^5} | {i['Job_role']:^20} | {i['Salary']:^10}")
        print()
    
    if choice==3:
        emp_id = int(input("\nEnter the employee id to fetch data: "))
        found = False
        for i in employee_list:
            if i['Id'] == emp_id:
                print("\nEmployee details are given below:\n")
                print(f"{'Id':^10} | {'Name':^20} | {'Age':^5} | {'Job_role':^20} | {'Salary':^10}")
                print("-" * 75)
                print(f"{i['Id']:^10} | {i['Name']:^20} | {i['Age']:^5} | {i['Job_role']:^20} | {i['Salary']:^10}")
                found = True
                break
        if not found:
            print("\nThe employee with the entered ID was not found!")
    
    if choice==4:
        id=int(input("\nEnter the employee id which employee data you want to update:"))
        if id in id_set:
            for i in employee_list:
                if id==i['Id']:
                    detail=input("\nEnter the column name which you want to update:").title()
                    if detail=='Id':
                        new_id=int(input("\nEnter the new id:"))
                        i[detail]=new_id
                        print("Id updated successfully!")
                        id_set.add(new_id)
                        for i in employee_list:
                            emp_id_set.add(i['Id'])
                        id_set=id_set.intersection(emp_id_set)
                    elif detail=='Name':
                        new_name=input("\nEnter the new name:")
                        i[detail]=new_name
                        print("Name updated successfully!")
                    elif detail=='Age':
                        new_age=int(input("\nEnter the new age:"))
                        i[detail]=new_age
                        print("Age updated successfully!")
                    elif detail=='Job_role':
                        new_role=input("\nEnter the new job role:")
                        i[detail]=new_role
                        print("Job role updated successfully!")
                    elif detail=='Salary':
                        new_salary=int(input("\nEnter the new salary:"))
                        i[detail]=new_salary
                        print("Salary updated successfully!")
                    else:
                        print("\nYou entered the wrong column name!")
                        break
        else:
            print("\nYour entered id is not found in the system!")
    
    if choice==5:
        id=int(input("\nEnter the id which employee data you want to remove from the system:"))
        if id in id_set:
            for i in employee_list:
                if i['Id']==id:
                    print(i)
                    employee_list.remove(i)
                    for i in employee_list:
                        emp_id_set.add(i['Id'])
                    id_set=id_set.intersection(emp_id_set)
                    
            print("\nEmployee data removed successfully!")
        else:
            print("\nEntered id is not found in the system!")
    
    if choice==6:
        print("\nYou are exit from the system!")
        is_on=False