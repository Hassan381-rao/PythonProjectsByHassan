print("||Contact Management System||")
input1 = input("\n1. Search by Name \n2. Search by Phone Number\n")
contacts = [
    {'name':'Hassan', 'ID': '095-1111', 'Phone':'+92454813812', 'email': 'ABDURRAHMAN@gmail.com', 'address':'XYZ'},
    {'name':'Sameed', 'ID': '095-4224', 'Phone':'+923123716235', 'email': 'SAMEED@gmail.com', 'address':'XYZ'},
    {'name':'Umar', 'ID': '095-3243', 'Phone':'+921988816232', 'email': 'UMAR@gmail.com', 'address':'XYZ'},
    {'name':'Shoaib', 'ID': '095-5432', 'Phone':'+923478814234', 'email': 'SHOAIB@gmail.com', 'address':'XYZ'},
    {'name':'Danial', 'ID': '095-2433', 'Phone':'+923638816214', 'email': 'DANIAL@gmail.com', 'address':'XYZ'},
    {'name':'Bilal', 'ID': '095-7953', 'Phone':'+923313216437', 'email': 'BILAL@gmail.com', 'address':'XYZ'},
    {'name':'Asim', 'ID': '095-2345', 'Phone':'+923372346232', 'email': 'ASIM@gmail.com', 'address':'XYZ'},
    {'name':'Rasheed', 'ID': '095-1734', 'Phone':'+9213478816236', 'email': 'RASHEED@gmail.com', 'address':'XYZ'},
    {'name':'Imran', 'ID': '095-1937', 'Phone':'+923371816230', 'email': 'IMRAN@gmail.com', 'address':'XYZ'},
    {'name':'Ali', 'ID': '095-9378', 'Phone':'+923873416137', 'email': 'ALI@gmail.com', 'address':'XYZ'}
]

if input1.strip().lower() in ['1', 'name', 'search by name']:
    search_name = input("\nEnter the Name of the contact:\n").strip().lower()
    found_contacts = [c for c in contacts if c['name'].strip().lower() == search_name]
    
    if found_contacts:
        for c in found_contacts:
            print(f"\nName:   {c['name']}\nID:     {c['ID']}\nPhone:  {c['Phone']}\nEmail:  {c['email']}\nAddress: {c['address']}\n")
    else:
        print("\n\nX Error! No contact found with that Name\n\n")

elif input1.strip().lower() in ['2', 'phone', 'search by phone']:
    search_phone = input("\nEnter the Phone Number:\n").strip().lower()
    found_contacts = [c for c in contacts if c['Phone'].strip().lower() == search_phone]
    
    if found_contacts:
        for c in found_contacts:
            print(f"\nName:   {c['name']}\nID:     {c['ID']}\nPhone:  {c['Phone']}\nEmail:  {c['email']}\nAddress: {c['address']}\n")
    else:
        print("\n\nX Error! No contact found with that Phone Number\n\n")

else:
    print("Invalid Input")
