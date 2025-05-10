import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')

db = client.get_database('schools')
collection = db.students

#db = client['Sample']
#collection = db['Sample1']

def VIEWALLRECORD():
    try:
        while True:
            print("\n\t1. Display One Document \n\t2. Display All \n\t3. Display Name & Section \n\t4. Display with Filter")
            choice = int(input("\nChoice: "))
            print("\n")
            if choice == 1:
                name = input("Name: ")
                query = {"Name": name,}
                print(collection.find_one(query))
            elif choice == 2:
                result = collection.find()
                for i in result:
                    print(i)
            elif choice == 3:
                for i in collection.find({},{"Name": 1, "Section": 1}):
                    print(i)
            elif choice == 4:
                age = input("Enter Age: ")
                result = collection.find({"Age": {"$gte": age}})
                for i in result:
                    print(i)
            else:
                break
    except ValueError as e:
        pass

def ADDNEWRECORD():
    try:
        print("\n\t1. One Record \n\t2. Multiple")
        choice = int(input("\nChoice: "))
        if choice == 1:
            name = input("Name: ")
            age = input("Age: ")
            section = input("Section: ")
            record = {"Name": name, "Age": age, "Section": section}
            collection.insert_one(record)
            print('\t\nStudent: \"', name,'\" Detailed Inserted.')
        elif choice == 2:
            number = int(input('Enter Number of Employees: '))
            l = []
            for i in range(number):
                name = input("\nName: ")
                age = input("Age: ")
                section = input("Section: ")
                record = {"Name": name, "Age": age, "Section": section}
                l.append(record)
            collection.insert_many(l)
        else:
            ADDNEWRECORD()
    except ValueError as e:
        pass

def UPDATERECORD():
    try:
        print("\n\t1. Update One Record \n\t2. Update Multiple")
        choice = int(input("\nChoice: "))

        if choice == 1:
            u_id = input("Enter ID of Student: ")
            query = {"Name": {"$eq": u_id}}
            present_data = collection.find_one(query)
            key = input("Enter Key(Fields): ")
            value = input("Enter Value(Data): ")
            new_data = {'$set': {key: value}}
            collection.update_one(present_data, new_data)
            print(collection.find_one(query))
        elif choice == 2:
            section = input("Enter Section: ")
            present_data = {'Section': section}
            new_sec = input("Enter New Section: ")
            new_data = {'$set': {'Section': new_sec}}
            collection.update_many(present_data, new_data)
            result = collection.find()
            for i in result:
                print(i)
    except ValueError as e:
        pass

def DELETERECORD():
    try:
        print("\n\t1. Delete One Record \n\t2. Delete Multiple")
        choice = int(input("\nChoice: "))

        if choice == 1:
            u_id = input("Enter ID of Student to be Deleted: ")
            query = {"Name": u_id}
            collection.delete_one(query)
            print('Student: ',u_id,' is deleted')
        elif choice == 2:
            section = input("Enter Section to be Deleted: ")
            query = {"Section": section}
            collection.delete_many(query)
            print("Sections: ", section ," are Deleted")

        result = collection.find()
        for i in result:
            print(i)
    except ValueError as e:
        pass
    #collection.drop() drop the collection


while True:
    print("\n<>======--- STUDENTS --======<>")
    v_list = "\t1. View All Record \n\t2. Add New Record \n\t3. Edit Record \n\t4. Delete Record \n\tX. Close Program"
    print(v_list)

    input1 = input("\nEnter Choice: ")

    if input1 == "1": # VIEW AND SEARCH RECORD
        VIEWALLRECORD()

    elif input1 == "2":  # ADD NEW RECORD
        ADDNEWRECORD()

    elif input1 == "3":  # EDIT/UPDATE RECORD
        UPDATERECORD()

    elif input1 == "4": # DELETE RECORD
        DELETERECORD()

    else:
        print("\n====Program Exit====\n")
        break
        exit()