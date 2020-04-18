from RSA_Encrpytion import *
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


