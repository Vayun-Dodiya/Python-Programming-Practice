
"""
Contact Management System
Author: Vayun
Description: A CRUD-based contact manager using record-markers and exception handling.
"""

def Features():
    while True:
        try:
            print("\n1. List | 2. Add | 3. Search | 4. Edit | 5. Remove | 6. Exit")
            operation = int(input("Enter Operation : "))
            if 1 <= operation <= 6:
                return operation
            print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input! Please enter a numeric digit.")


def ConP(name = "Unknown",CNo = ""):
    str_To_print = f"\n->\nName : {name.capitalize()}\nContact Number : {CNo}\n"
    return str_To_print


print("\t"*9 + " ===== Contact - Editor =====")


while True:

    conact = None
    opera = Features()
    
    if opera == 1: # List The Contact
    
        print("Printing The Contact ...")
    
        with open("Contact.txt") as f:
            Contact = f.read()
        print(Contact)
    
    elif opera == 2: # Add More Contact

        Name = input("Enter The Name : ")
        Number = input("Enter Number : ")

        if len(Number) != 10 or not(Number.isdigit()):
            print("Invalid Number !")
            break

        else:

            addContact = ConP(Name, Number)
            with open("Contact.txt", "a") as f:
                f.write(addContact)


    elif opera == 3: # Search For Contact

        line = None
        found = 0
        search = input("Enter The Name : ")
    
        with open("Contact.txt") as f:
            line = f.readline()
    
            while line != "":
    
                if search.lower() in line.lower():
                    print("\n----Contact Found----\n")
                    found += 1
    
                if found == 1:
                    print("=>\n    "+line , end="")
                    line = f.readline()
                    print("    "+line , end="")
                    found = 0
    
                line = f.readline()
    
    elif opera == 4: # Edit Contact
        
        search = input("Enter The Contact Name or Number You Want TO Edit : ")
        
        if search.isdigit():
            i,NewContent,found = 0,[],0

            with open("Contact.txt") as f:
                content = f.readlines()
            
            count = 0
            
            for i in content:
            
                if search.lower() in i.lower():
                    found= 1
                    break
                count += 1
            
            edit_Line = None
            
            if found == 1:
                edit_Line = content[count-1]
            
                new_name = input("Enter New Name : ")
                new_contact = input("Enter New Contact Number : ")
                
                while len(new_contact) != 10 or new_contact.isdigit() != True :
                    new_contact = input("Enter a valid number Contact Number : ")
                else:Update_Contact = f"Name : {new_name.capitalize()}\nContact Number : {new_contact}\n"
            
                edit= edit_Line.replace(edit_Line,Update_Contact)
            
            index = 0
            
            for i in content:
            
                if index == count :
                    index += 1
                    continue
                if index != count -1 :
                    NewContent.append(i)
                else: 
                    NewContent.append(edit)
            
                index += 1

            with open("Contact.txt","w") as f:
                for i in NewContent:
                    f.write(i)
            
            break

        elif search.isalpha():
            NewContent = []
            count,found = 0,0
            with open("Contact.txt") as f:
                content = f.readlines()
            
            for i in content:
            
                if search.lower() in i.lower():
                    found= 1
                    break
                count += 1
            
            if found == 1:
                edit_Line = content[count]

                new_name = input("Enter New Name : ")
                new_contact = input("Enter New Contact Number : ")
                
                while len(new_contact) != 10 or new_contact.isdigit() != True :
                    new_contact = input("Enter a valid number Contact Number : ")
                else:Update_Contact = f"Name : {new_name.capitalize()}\nContact Number : {new_contact}\n"

                edit= edit_Line.replace(edit_Line,Update_Contact)
            
                index = 0
                
                for i in content:
                
                    if index == count +1 :
                        index += 1
                        continue
                    if index != count :
                        NewContent.append(i)
                    else: 
                        NewContent.append(edit)
                
                    index += 1

                with open("Contact.txt","w") as f:
                    for i in NewContent:
                        f.write(i)
            else:
                print("Contact Not Found !")
                break

    elif opera == 5: # Remove The Contact 

        marker = "->\n"
        with open("Contact.txt") as f:
            content = f.readlines()
        
        search = input("Enter The Contact Name You Want TO Delete : ")

        index,found = 0,0

        for i in content :
            if search.lower() in i.lower():
                content_2 = content.copy()
                break
            index += 1
        
        else:print("Contact Not Found !")

        try:

            Mark2In = content_2.index(marker, index)
            
            for i in range(index, Mark2In + 1):
                content.pop(index - 1)

        except ValueError:

            print("Deleting the last contact in the list...")
            
            content = content[:index-2]

        with open("Contact.txt","w") as f:
            for i in content:
                f.write(i)

    elif opera == 6: # Close The Execution
        break