import pyperclip
import random
class Credentials:
    credential_list = []
    password_list = ["Allan","Champez254","Lildurk7","XotourUzi1","Emergingh20","dIvergencE666","ModuloFanForum11","Oldtraffordseat12"]
    random_password = random.choice(password_list)
    def __init__(self,application_name,password):
        self.application_name = application_name
        self.password = password
      
    @classmethod    
    def generate_random_password(cls):
        '''
         function that returns a random password
        '''
        return cls.random_password
    def save_credential(self):
        '''
          Adding the created object to the list
        '''
        Credentials.credential_list.append(self)
    def delete_credential(self):
        '''
          Removing an object from our list
        '''
        Credentials.credential_list.remove(self)
        
    @classmethod
    def display_credentials(cls):
        '''
         Method that shows all elements in our list
        '''
        return cls.credential_list
    
    @classmethod 
    def find_by_credential_name(cls,name):
        '''
          method that takes in a number and returns a contact that matches that number
        '''
        for credential in cls.credential_list:
            if credential.application_name == name:
                return credential
    
    @classmethod
    def copy_credentials(cls,name):
        '''
          Function that copies the credentials to the clipboard
        '''
        credentials_found = Credentials.find_by_credential_name(name)
        pyperclip.copy(credentials_found)
