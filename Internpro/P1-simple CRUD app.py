import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase with service account key and database URL
cred = credentials.Certificate('credentials.json.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://crud-application-88d24-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

def create_entry(path):
    """
    Prompts the user to input new data and adds it to the specified path.
    """
    name = input("Enter name: ")
    email = input("Enter email: ")
    age = input("Enter age: ")

    data = {
        'name': name,
        'email': email,
        'age': age
    }

    ref = db.reference(path)
    new_ref = ref.push()  # Generates a unique key
    new_ref.set(data)
    print(f"Data added to {path} with key {new_ref.key}")
    return new_ref.key

def read_entry(path):
    """
    Prompts the user to retrieve either a specific entry or all entries.
    """
    ref = db.reference(path)
    key = input("Enter specific key to retrieve (leave blank to retrieve all data): ")
    
    if key:
        data = ref.child(key).get()
        if data:
            print(f"Data retrieved for key {key}: {data}")
        else:
            print(f"No data found for key {key}.")
    else:
        data = ref.get()
        print(f"Data retrieved from {path}: {data}")

def update_entry(path):
    """
    Prompts the user for a key and updates the corresponding data.
    """
    key = input("Enter the key of the entry you want to update: ")
    ref = db.reference(path).child(key)

    if ref.get():
        new_name = input("Enter new name: ")
        new_email = input("Enter new email: ")
        new_age = input("Enter new age: ")

        updated_data = {
            'name': new_name,
            'email': new_email,
            'age': new_age
        }

        ref.update(updated_data)
        print(f"Data at {path}/{key} updated.")
    else:
        print(f"No data found for key {key}.")

def delete_entry(path):
    """
    Prompts the user for a key and deletes the corresponding entry.
    """
    key = input("Enter the key of the entry you want to delete: ")
    ref = db.reference(path).child(key)

    if ref.get():
        ref.delete()
        print(f"Data at {path}/{key} has been deleted.")
    else:
        print(f"No data found for key {key}.")

def main():
    print("Firebase CRUD Operations")
    print("1. Create a new entry")
    print("2. Read data")
    print("3. Update an existing entry")
    print("4. Delete an entry")
    print("5. Exit")
    
    path = 'users'  # You can change this to another path in the database if needed

    while True:
        choice = input("\nChoose an operation (1-5): ")

        if choice == '1':
            create_entry(path)
        elif choice == '2':
            read_entry(path)
        elif choice == '3':
            update_entry(path)
        elif choice == '4':
            delete_entry(path)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
