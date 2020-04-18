from RSA_Encrpytion import *
import json
class Create_New_Account:
  def __init__(self):
    self.username = ''
    self.password = ''

  def credentials(self):
    print('**************** NEW ACCOUNT ****************')
    self.username = input('Enter Account Name: ')
    self.password = input('Enter Account Password: ')

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
    with open("database.json","w") as write_file:
      json.dump(db,write_file,indent=4)

