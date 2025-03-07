print("||Contact Management System||")
input1 = input("\n1.Search by Name: \n2.Search by number:\n")
if input1.strip().lower() in ['1','name','search by name']:
  from colorama import Fore,Style,init
  init()
  contacts = []
  contacts.append({'name':'M.Hassan','ID': '095-1111','Phone':'+923378816234','email': 'ABDURRAHMAN@gmail.com','address':'XYZ'})
  contacts.append({'name':'Sameed','ID': '095-4224','Phone':'+923123716235','email': 'SAMEED@gmail.com', 'address':'XYZ'})
  contacts.append({'name':'Umar','ID': '095-3243','Phone':'+921988816232','email': 'UMAR@gmail.com', 'address':'XYZ'})
  contacts.append({'name':'Shoaib','ID': '095-5432','Phone':'+923478814234','email': 'SHOAIB@gmail.com','address':'XYZ'})
  contacts.append({'name':'Danial','ID': '095-2433','Phone':'+923638816214','email': 'DANIAL@gmail.com','address':'XYZ'})
  contacts.append({'name':'Bilal','ID': '095-7953','Phone':'+923313216437','email': 'BILAL@gmail.com','address':'XYZ'})
  contacts.append({'name':'Asim','ID': '095-2345','Phone':'+923372346232','email': 'ASIM@gmail.com','address':'XYZ'})
  contacts.append({'name':'Rasheed','ID': '095-1734','Phone':'+9213478816236','email': 'RASHEED@gmail.com','address':'XYZ'})
  contacts.append({'name':'Imran','ID': '095-1937','Phone':'+923371816230','email': 'IMRAN@gmail.com','address':'XYZ'})
  contacts.append({'name':'Ali','ID': '095-9378','Phone':'+923873416137','email': 'ALI@gmail.com','address':'XYZ'})

  search_name = input("\nEnter the Name of the contact:\n").strip().lower()
  found_contacts = []
  for c in contacts:
      if c['name'].strip().lower() == search_name:
        found_contacts.append(c)
  if found_contacts:
     for c in found_contacts:
         print(Fore.GREEN+f"\nName:   {c['name']}\nID:     {c['ID']}\nPhone:  {c['Phone']}\nEmail:  {c['email']}\nAdress: {c['address']}\n")
  else:
       print(Fore.RED+"\n\nX Error! No contact found with that Name\n\n")
       
elif input1.strip().lower() in ['2','phone','search by name']:
  from colorama import Fore,Style,init
  init()
  contacts = []
  contacts.append({'name':'M.Hassan','ID': '095-1111','Phone':'+923378816234','email': 'ABDURRAHMAN@gmail.com','address':'XYZ'})
  contacts.append({'name':'Sameed','ID': '095-4224','Phone':'+923123716235','email': 'SAMEED@gmail.com', 'address':'XYZ'})
  contacts.append({'name':'Umar','ID': '095-3243','Phone':'+921988816232','email': 'UMAR@gmail.com', 'address':'XYZ'})
  contacts.append({'name':'Shoaib','ID': '095-5432','Phone':'+923478814234','email': 'SHOAIB@gmail.com','address':'XYZ'})
  contacts.append({'name':'Danial','ID': '095-2433','Phone':'+923638816214','email': 'DANIAL@gmail.com','address':'XYZ'})
  contacts.append({'name':'Bilal','ID': '095-7953','Phone':'+923313216437','email': 'BILAL@gmail.com','address':'XYZ'})
  contacts.append({'name':'Asim','ID': '095-2345','Phone':'+923372346232','email': 'ASIM@gmail.com','address':'XYZ'})
  contacts.append({'name':'Rasheed','ID': '095-1734','Phone':'+9213478816236','email': 'RASHEED@gmail.com','address':'XYZ'})
  contacts.append({'name':'Imran','ID': '095-1937','Phone':'+923371816230','email': 'IMRAN@gmail.com','address':'XYZ'})
  contacts.append({'name':'Ali','ID': '095-9378','Phone':'+923873416137','email': 'ALI@gmail.com','address':'XYZ'})

  search_name = input("\nEnter the phone Number:\n").strip().lower()
  found_contacts = []
  for c in contacts:
      if c['ID'].strip().lower() == search_name:
        found_contacts.append(c)
  if found_contacts:
     for c in found_contacts:
         print(Fore.GREEN+f"\nName:   {c['name']}\nID:     {c['ID']}\nPhone:  {c['Phone']}\nEmail:  {c['email']}\nAdress: {c['address']}\n")
  else:
       print(Fore.RED+"\n\nX Error! No contact found with that ID\n\n")       
else:
    print("Invalid Input")       