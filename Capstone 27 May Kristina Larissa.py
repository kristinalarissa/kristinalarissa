patients = []
next_id = 1

# Dictionary of diseases
diseases = {
    "1": "Flu",
    "2": "Diabetes",
    "3": "Vertigo",
    "4": "Mental Health",
    "5": "Covid-19"
}

def main_menu():
    print("=== Main Menu ===")
    print("1. Create Data")
    print("2. Read Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Exit")

def display_table(data):
    if data:
        headers = data[0].keys()
        row_format = "{:<15}" * (len(headers))
        print(row_format.format(*headers))
        print("=" * 15 * len(headers))
        for patient in data:
            print(row_format.format(*patient.values()))
    else:
        print("Data does not exist.\n")

def create_data():
    global next_id
    while True:
        print("=== Create Data Menu (Add Data) ===")
        print("1. Add Data")
        print("2. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            id = str(next_id)
            next_id += 1

            name = input("Enter Patient Name: ")
            age = input("Enter Patient Age: ")
            gender = input("Enter Patient Gender (L/P): ")

            # Display disease options
            print("Select Disease:")
            for key, value in diseases.items():
                print(f"{key}. {value}")
            disease_choice = input("Enter the number corresponding to the disease: ")
            diagnosis = diseases.get(disease_choice, "Unknown")
            patient = {
                "ID": id,
                "Name": name,
                "Age": age,
                "Gender": gender,
                "Diagnosis": diagnosis
            }

            print("=== Data Saving Option Menu ===")
            print("1. Save Data")
            print("2. Cancel")
            save_choice = input("Enter your choice: ")

            if save_choice == "1":
                patients.append(patient)
                print("Data successfully saved.\n")
            else:
                print("Data not saved.\n")
        elif choice == "2":
            break
        else:
            print("The option you entered is not valid.\n")

def read_data():
    while True:
        print("=== Show Display Data Menu (Read Data) ===")
        print("1. Display All Data")
        print("2. Search Data by ID")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            if patients:
                display_table(patients)
            else:
                print("Data does not exist.\n")
        elif choice == "2":
            if patients:
                id = input("Enter Patient ID to search: ")
                found_data = [patient for patient in patients if patient["ID"] == id]
                if found_data:
                    display_table(found_data)
                else:
                    print("Data does not exist.\n")
                    print("1. Try again")
                    print("2. Back to Read Data Menu")
                    sub_choice = input("Enter your choice: ")
                    if sub_choice == "1":
                        continue
                    elif sub_choice == "2":
                        break
                    else:
                        print("The option you entered is not valid.\n")
                        break
            else:
                print("Data does not exist.\n")
        elif choice == "3":
            break
        else:
            print("The option you entered is not valid.\n")

def update_data():
    while True:
        print("=== Show Update Data Menu (Edit Data) ===")
        print("1. Update Data")
        print("2. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Patient Name to update: ")
            found = False
            for patient in patients:
                if patient["Name"] == name:
                    found = True
                    display_table([patient])
                    print("Do you want to continue updating this data?")
                    print("1. Yes")
                    print("2. No")
                    update_choice = input("Enter your choice: ")

                    if update_choice == "1":
                        print("Enter new values (leave blank to keep current value):")
                        new_name = input(f"Enter new Patient Name (current: {patient['Name']}): ") or patient['Name']
                        new_age = input(f"Enter new Patient Age (current: {patient['Age']}): ") or patient['Age']
                        new_gender = input(f"Enter new Patient Gender (current: {patient['Gender']}): ") or patient['Gender']

                        print("Select new Disease (leave blank to keep current value):")
                        for key, value in diseases.items():
                            print(f"{key}. {value}")
                        disease_choice = input(f"Enter the number corresponding to the disease (current: {patient['Diagnosis']}): ") or None
                        diagnosis = diseases.get(disease_choice, patient['Diagnosis'])

                        patient["Name"] = new_name
                        patient["Age"] = new_age
                        patient["Gender"] = new_gender
                        patient["Diagnosis"] = diagnosis
                        print("Data successfully updated.\n")
                    else:
                        print("Update canceled.\n")
                    break
            if not found:
                print("The data you are looking for does not exist.\n")
        elif choice == "2":
            break
        else:
            print("The option you entered is not valid.\n")

def delete_data():
    while True:
        print("=== Show Delete Data Menu (Delete Data) ===")
        print("1. Delete Data")
        print("2. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Patient Name to delete: ")
            found = False
            for patient in patients:
                if patient["Name"] == name:
                    found = True
                    display_table([patient])
                    print("Do you want to delete this data?")
                    print("1. Yes")
                    print("2. No")
                    delete_choice = input("Enter your choice: ")

                    if delete_choice == "1":
                        patients.remove(patient)
                        print("Data successfully deleted.\n")
                    else:
                        print("Deletion canceled.\n")
                    break
            if not found:
                print("The data you are looking for does not exist.\n")
        elif choice == "2":
            break
        else:
            print("The option you entered is not valid.\n")

while True:
    main_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        create_data()
    elif choice == "2":
        read_data()
    elif choice == "3":
        update_data()
    elif choice == "4":
        delete_data()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("The option you entered is not valid.\n")