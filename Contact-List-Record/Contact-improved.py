
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
            continue

        else:

            addContact = ConP(Name, Number)
            with open("Contact.txt", "a") as f:
                f.write(addContact)


    elif opera == 3: # Search For Contact

        line = None
        found = 0
        search = input("Enter The Name : ")
    
        with open("Contact.txt") as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if search.lower() in line.lower():
                # find the start marker '->\n' going backwards
                start = i
                while start > 0 and lines[start].strip() != "->":
                    start -= 1
                print("\n----Contact Found----")
                found = 1
                # print name and number lines (marker is at start, name at start+1, number at start+2)
                print("=>\n    " + lines[start + 1], end="")
                print("    " + lines[start + 2], end="")
        if found == 0:print("Contact Not Found !")
        else:pass
    
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
                edit_Line = content[count]
            
                new_name = input("Enter New Name : ")
                new_contact = input("Enter New Contact Number : ")
                
                while len(new_contact) != 10 or new_contact.isdigit() != True :
                    new_contact = input("Enter a valid number Contact Number : ")
                else:Update_Contact = f"Name : {new_name.capitalize()}\nContact Number : {new_contact}\n"
            
                edit= edit_Line.replace(edit_Line,Update_Contact)
            else:
                print("Contact Not Found !")
                continue
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
                continue

    elif opera == 5: # Remove The Contact 

        marker = "->\n"
        with open("Contact.txt") as f:
            content = f.readlines()
        
        search = input("Enter The Contact Name You Want TO Delete : ")

        index,found = 0,0

        found = False
        for i in content:
            if search.lower() in i.lower():
                content_2 = content.copy()
                found = True
                break
            index += 1

        if not found:
            print("Contact Not Found!")
            continue  # go back to menu
        
        try:

            Mark2In = content_2.index(marker, index)
            
            # The block starts 2 lines before match: blank line + "->\n"
            block_start = index - 2  
            lines_to_delete = Mark2In - block_start + 1

            for _ in range(lines_to_delete):
                content.pop(block_start)

        except ValueError:

            print("Deleting the last contact in the list...")
            
            content = content[:index-2]

        with open("Contact.txt","w") as f:
            for i in content:
                f.write(i)

    elif opera == 6: # Close The Execution
        break