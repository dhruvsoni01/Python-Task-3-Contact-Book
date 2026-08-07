contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("\n✅ Contact Added Successfully!")

def view_contacts():
    if len(contacts) == 0:
        print("\nNo Contacts Available!")
    else:
        print("\n------ Contact List ------")
        for i, contact in enumerate(contacts, start=1):
            print(f"\nContact {i}")
            print("Name :", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])

def search_contact():
    name = input("Enter Name to Search: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("\n✅ Contact Found")
            print("Name :", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            return

    print("\n❌ Contact Not Found!")

def delete_contact():
    name = input("Enter Name to Delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("\n✅ Contact Deleted Successfully!")
            return

    print("\n❌ Contact Not Found!")

while True:
    print("\n========== CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("\nThank You for Using Contact Book!")
        break
    else:
        print("\nInvalid Choice! Please Try Again.")