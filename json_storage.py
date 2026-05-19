import json
from json import JSONDecodeError
from datetime import datetime
from mapping_trans import transaction_data


file_path = "storage.json"

def json_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj).__name__} not serializable")


def save_transactions(data):
    with open(file_path, "w") as file:
        json.dump(data, file, default=json_serializer, indent=4)


def load_transactions():
    try:
        with open(file_path, "r") as file:
            try:
                data = json.load(file)
            except JSONDecodeError:
                data = []

        if not data:
            print("No transactions found in storage. Initializing default storage.")
            data = [transaction.dict() for transaction in transaction_data]
            save_transactions(data)

        print(f"Loaded transactions: {len(data)}")
        return data
    except FileNotFoundError:
        print("Storage file not found. Creating new storage file.")
        data = [transaction.dict() for transaction in transaction_data]
        save_transactions(data)
        print(f"Created storage with {len(data)} default transaction(s).")
        return data
    
# def show_transactions():
#     transactions = load_transactions()
#     if not transactions:
#         print("No transactions to show.")
#         return
    
#     print("\nDaftar Transaksi: ")
#     for t in transactions:
#         print(f"{t['id']}. Date: {t['created_date']}, Category: {t['category']}, Description: {t['description']}, Nominal: {t['nominal']}, Instrument: {t['instrument']}")
    
# def input_transaction():
#     transactions = load_transactions()
#     len_tran = len(transactions)
#     last_id = transactions[len_tran - 1]['id'] + 1 if len_tran > 0 else 1

#     category = input("Enter category: ")
#     description = input("Enter description: ")
#     nominal = float(input("Enter nominal: "))
#     instrument = input("Enter instrument: ")
#     note = input("Enter note (optional): ")
#     if note == "":
#         note = None

#     return {
#         "id": last_id,
#         "tele_id": 1851975506,
#         "created_date": datetime.now().isoformat(),
#         "category": category,
#         "description": description,
#         "nominal": nominal,
#         "instrument": instrument,
#         "note": note
#     }


# load_transactions()

# while True:
#     print("\nMenu:")
#     print("1. Show Transactions")
#     print("2. Add Transaction")
#     print("3. Exit")
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         show_transactions()
#     elif choice == "2":
#         new_transaction = input_transaction()
#         transactions = load_transactions()
#         transactions.append(new_transaction)
#         save_transactions(transactions)
#         print("Transaction added successfully!")
#     elif choice == "3":
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice. Please try again.")
    
