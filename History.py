import json
import datetime
class Transaction_History:
  def __init__(self,u):
    self.data = {}
    self.username = u

  def time(self):
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

  def update_history(self,amt,t):
    with open("history.json","r") as read_file:
      self.data = json.load(read_file)
    self.data[self.username]['Transactions'] += 1
    index = 'T' + str(self.data[self.username]['Transactions'])
    self.data[self.username][index] = {}
    self.data[self.username][index]["type"] = t
    self.data[self.username][index]["amount"] = amt
    src = input('Source: ')
    self.data[self.username][index]["source"] = src
    self.data[self.username][index]["time"] = self.time()
    with open("history.json","w") as write_file:
      json.dump(self.data,write_file,indent=4)
