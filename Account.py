import json
from New_Account import *
from RSA_Encrpytion import *
class User_Account:
  def __init__(self):
    self.username = ''
    self.password = ''
    self.db = {}

  def deposit(self):
    amount = float(input('Enter amount to be added: '))
    self.db[self.username]["savings"] += amount

  def withdraw(self):
    amount = float(input('Enter amount to be removed: '))
    if self.db[self.username]["savings"] < amount:
      print('Savings not enough!')
      return
    self.db[self.username]["savings"] -= amount

  def update_goal(self):
    print(self.db[self.username]["goal"])
    change_in_goal = float(input('Enter change in goal: '))
    self.db[self.username]["goal"] += change_in_goal

  def progress(self):
    if self.db[self.username]["goal"] == 0:
      percent = 0
      remainder = 0
    else:
      percent = (self.db[self.username]["savings"]/self.db[self.username]["goal"]) * 100
      remainder = self.db[self.username]["goal"] - self.db[self.username]["savings"]
    print('{}% '.format(percent) + ' of goal completed')
    print('${}'.format(remainder) + ' left to go')

  def open_account(self):
    self.username = input('Enter Account Name: ')
    with open("database.json","r") as read_file:
      self.db = json.load(read_file)
    if self.username not in self.db:
      decision = input('Would you like to create a new account? Enter yes or no: ')
      if decision == 'yes':
        x = Create_New_Account()
        x.credentials()
        x.updating_database()
        print()
        self.credentials()
      else:
        return
    while True:
      self.password = input('Enter Account Password: ')
      p = self.db[self.username]["password"]
      k = self.db[self.username]["key"]
      r = RSA_Encryption()
      correct_password = r.decrypt(k,p)
      if correct_password == self.password:
        break
      print('Wrong Password! Please Try Again!')
    print('**************** ' + self.username + '\'s Account ***************')
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Update Goal')
    print('4. Progress')
    choice = int(input('Enter your choice number (1-4): '))
    if choice == 1:
      self.deposit()
    elif choice == 2:
      self.withdraw()
    elif choice == 3:
      self.update_goal()
    elif choice == 4:
      self.progress()
    with open("database.json","w") as write_file:
      json.dump(self.db,write_file,indent=4)




