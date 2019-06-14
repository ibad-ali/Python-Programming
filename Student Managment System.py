data = []
while True:
    print("Press 1: for Show All Students") #here is the choices for user
    print("Press 2: for Search Student")
    print("Press 3: for Add Student")
    print("Press 4: for Update Student")
    print("Press 5: for Delete Student")
    print("Press 6: for Exit")

    ask = input("\nEnter the Choice : ")


    if(ask=="1"):                           #here show all data of student
        if(data == []):
            print("\nNo record found\n")

        else:
            for i in data:
                print(i,end='\n')
            print('\n')
        continue

    if (ask == "2"):                        #here search a particular student data
        ask_id = int(input("\nEnter the ID of Student :"))
        for j in data:
            if(j["ID"]==ask_id):
                print("\nStudent Name = ",j["Name"])
                print("Student Age = ",j["Age"])
                print("Student Class = ",j["Class"],"\n")

            else:
                print("Sorry no record found")
        continue

    if (ask == "3"):                        #here add a new record/student data
        std_id = int(input("Enter the Id of student :"))
        std_name = input("Enter the Name of student :")
        std_age = input("Enter the Age of student :")
        std_class = input("Enter the class of student :")
        rec = {}
        rec["ID"] = std_id
        rec["Name"] = std_name
        rec["Age"] = std_age
        rec["Class"] = std_class
        data.append(rec)
        print("\nNew Record Add Successfully\n")
        continue

    if (ask == "4"):                        #here update the student data
        ask_id = int(input("\nEnter the ID of Student :"))
        for j in data:
            if (j["ID"] == ask_id):
                print("\nStudent Name = ", j["Name"])
                print("Student Age = ", j["Age"])
                print("Student Class = ", j["Class"], "\n")

                askstd_id = int(input("Enter the new Id of student :"))
                askstd_name = input("Enter the new Name of student :")
                askstd_age = input("Enter the new Age of student :")
                askstd_class = input("Enter the new class of student :")

                j["ID"] = askstd_id
                j["Name"] = askstd_name
                j["Age"] = askstd_age
                j["Class"] = askstd_class

                print("\nRecord Updated Successfully\n")

            else:
                print("Sorry no record found")

        continue

    if (ask == "5"):                        #here delete a particular student data
        ask_id = int(input("\nEnter the ID of Student :"))
        for j in data:
            if (j["ID"]== ask_id):
                data.remove(j)
                print("\nRecord deleted successfully\n")
            else:
                print("\nNo record found\n")

        continue

    if (ask == "6"):                        #here exit from program
        print("\nYou are exit from System\n")
        break

    else:
        print("\nInvalid Choice\n")
        continue

