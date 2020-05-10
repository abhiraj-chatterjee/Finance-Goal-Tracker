import json
from New_Account import *
from RSA_Encrpytion import *
from History import *
class User_Account:
  def __init__(self):
    self.username = ''
    self.password = ''
    self.db = {}

  def update(self,amt,t):
    hist = Transaction_History(self.username)
    hist.update_history(amt,t)

  def deposit(self):
    amount = float(input('Enter amount to be added: '))
    self.db[self.username]["savings"] += amount
    self.update(amount,'Deposit')

  def withdraw(self):
    amount = float(input('Enter amount to be removed: '))
    if self.db[self.username]["savings"] < amount:
      print('Savings not enough!')
      return
    self.db[self.username]["savings"] -= amount
    self.update(amount,'Withdraw')

  def update_goal(self):
    print(self.db[self.username]["goal"])
    change_in_goal = float(input('Enter change in goal: '))
    self.db[self.username]["goal"] += change_in_goal
    self.update(change_in_goal,"Goal Update")

  def progress(self):
    if self.db[self.username]["goal"] == 0:
      percent = 0
      remainder = 0
    else:
      percent = (self.db[self.username]["savings"]/self.db[self.username]["goal"]) * 100
      remainder = self.db[self.username]["goal"] - self.db[self.username]["savings"]
    print('{}% '.format(percent) + ' of goal completed')
    print('${}'.format(remainder) + ' left to go')

  def create_bank_statement(self):
    f = open(self.username+' Statement.tsv',"w")
    f.write('Type\tAmount\tSource\tTime\n')
    with open("history.json","r") as read_file:
      data = json.load(read_file)
    for each in data[self.username]:
      row = ''
      if each == 'Transactions':
        continue
      for each1 in data[self.username][each]:
        row = row + str(data[self.username][each][each1]) + '\t'
      row = row.rstrip('\t')
      row = row + '\n'
      f.write(row)
    print('Success! Your statement is ready as ' + self.username + ' Statement.tsv')
    f.close()

  def security_verify(self):
    print()
    print('**************** Security Questions ****************')
    correct = 0
    email = input('Enter Linked Email: ')
    if email == self.db[self.username]["email"]:
      correct += 1
    phone = input('Enter Linked Phone Number (without country code): ')
    if phone == self.db[self.username]["phone"]:
      correct += 1
    date_of_birth = input('Enter your date of birth (MM/DD/YYYY): ')
    if date_of_birth == self.db[self.username]["dob"]:
      correct += 1
    if correct == 3:
      print()
      print('Verified!')
      return True
    else:
      return False

  def open_account(self,logged_in=0):
    print()
    print('**************** Finance Goal Tracker ****************')
    while logged_in == 0 and True:
      self.username = input('Enter Account Name: ')
      if ' ' not in self.username:
        decision = input('Do you have an account? Enter yes or no: ')
        if decision == 'no':
          break
        else:
          print('Please enter your full name.', end=' ')
      else:
        break
    with open("database.json","r") as read_file:
      self.db = json.load(read_file)
    if self.username not in self.db:
      decision = input('Would you like to create a new account? Enter yes or no: ')
      if decision == 'yes':
        x = Create_New_Account()
        x.credentials()
        x.updating_database()
        print()
        self.open_account(1)
        return
      else:
        print()
        print('Thank you for using Finance Goal Tracker! Goodbye!')
        return
    password_tries = 0
    while logged_in == 0 and True:
      password_tries += 1
      self.password = input('Enter Account Password: ')
      p = self.db[self.username]["password"]
      k = self.db[self.username]["key"]
      r = RSA_Encryption()
      correct_password = r.decrypt(k,p)
      if correct_password == self.password:
        if password_tries > 1:
          if self.security_verify() == False:
            print()
            print('Sorry! You answered incorrectly to 1 or more of the security questions. Goodbye!')
            return
        else:
          break
      if password_tries == 5:
        print()
        print('Sorry! You have no more attempts left. Goodbye!')
        return
      print('Wrong Password! You have ' + str(5-password_tries) + ' more attempt(s). Please Try Again!')
    flag = 0
    while flag != 2:
      print()
      print('**************** ' + self.username + '\'s Account ***************')
      print('1. Deposit')
      print('2. Withdraw')
      print('3. Update Goal')
      print('4. Progress')
      print('5. Create Statement')
      if flag == 1:
        print()
        print('Incorrect choice entered. Please try again!', end=' ')
        flag = 0
      else:
        print()
      try:
        choice = int(input('Enter your choice number (1-5): '))
        if (choice < 1 or choice > 5):
          flag = 1
        else:
          flag = 2
      except:
        flag = 1
    if choice == 1:
      self.deposit()
    elif choice == 2:
      self.withdraw()
    elif choice == 3:
      self.update_goal()
    elif choice == 4:
      self.progress()
    elif choice == 5:
      self.create_bank_statement()
    with open("database.json","w") as write_file:
      json.dump(self.db,write_file,indent=4)




