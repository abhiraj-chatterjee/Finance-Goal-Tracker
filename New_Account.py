from RSA_Encrpytion import *
import json
class Create_New_Account:
  def __init__(self):
    self.username = ''
    self.password = ''
    self.email = ''
    self.phone = ''
    self.date_of_birth = ''

  def credentials(self):
    print('**************** NEW ACCOUNT ****************')
    self.username = input('Enter Account Name: ')
    self.password = input('Enter Account Password: ')
    while True:
      confirm_password = input('Enter Account Password (Confirmation): ')
      if self.password != confirm_password:
        print('Incorrect!', end=' ')
      else:
        break
    self.email = input('Enter Account Email: ')
    self.phone = input('Enter Account Phone Number: ')
    self.date_of_birth = input('Enter Account Date of Birth (MM/DD/YYYY): ')

  def encrypting_the_password(self):
    x = RSA_Encryption()
    x.generate_numbers()
    x.generate_key()
    pv = x.private_key
    ps = x.encrypt(self.password)
    return (ps,pv)

  def updating_database(self):
    with open("database.json","r") as read_file:
      db = json.load(read_file)
    db[self.username] = {}
    db[self.username]["goal"] = 0
    db[self.username]["savings"] = 0
    p, k = self.encrypting_the_password()
    db[self.username]["password"] = p
    db[self.username]["key"] = k
    db[self.username]["email"] = self.email
    db[self.username]["phone"] = self.phone
    db[self.username]["dob"] = self.date_of_birth
    with open("database.json","w") as write_file:
      json.dump(db,write_file,indent=4)
    with open("history.json","r") as read_file:
      data = json.load(read_file)
    data[self.username] = {}
    data[self.username]["Transactions"] = 0
    with open("history.json","w") as write_file:
      json.dump(data,write_file,indent=4)


