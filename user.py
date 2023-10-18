class User:
    user_list = []
    def __init__(self,user_name,phone_number,email,password):
        self.user_name = user_name
        self.password = password
        self.phone_number = phone_number
        self.email = email
       
    def save_user(self):
        '''
          Adding the created object to the list
        '''
        User.user_list.append(self)
        
      
    def delete_user(self):
        '''
          Removing an object from our list
        '''
        User.user_list.remove(self)
    
    @classmethod
    def display_users(cls):
        '''
         Method that shows all elements in our list
        '''
        return cls.user_list
        
    
