import os
import pickle

class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class ContactBook:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists("contacts.pickle"):
            with open("contacts.pickle", "rb") as f:
                self.contacts = pickle.load(f)

    def save_contacts(self):
        with open("contacts.pickle", "wb") as f:
            pickle.dump(self.contacts, f)

    def add_contact(self, name, phone_number):
        contact = Contact(name, phone_number)
        self.contacts.append(contact)
        self.save_contacts()

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

    def update_contact(self, name, new_phone_number):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = new_phone_number
                self.save_contacts()
                return True
        return False

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                self.save_contacts()
                return True
        return False

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            contact_book.add_contact(name, phone_number)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            name = input("Enter name of contact to update: ")
            new_phone_number = input("Enter new phone number: ")
            if not contact_book.update_contact(name, new_phone_number):
                print("Contact not found.")
        elif choice == "4":
            name = input("Enter name of contact to delete: ")
            if not contact_book.delete_contact(name):
                print("Contact not found.")
        elif choice == "5":
            contact_book.save_contacts()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
