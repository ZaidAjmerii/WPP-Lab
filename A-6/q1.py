


'''
Write a class called Password_manager. The class should have a list called old_passwords that 
holds all of the user’s past passwords. The last item of the list is the user’s current pass word. 
There should be a method called get_password that returns the current password and a method 
called set_password that sets the user’s password. The set_password method should only 
change the password if the attempted password is different from all the user’s past passwords. 
Finally, create a method called is_correct that receives a string and returns a boolean True or 
False depending on whether the string is equal to the current password or not.
'''


class PasswordManager:
    def _init_(self, old_password = None):
        if old_password is None:
            self.old_password = []
        else:
            self.old_password = old_password
    def set_password(self, new_password):
        if new_password not in self.old_password:
            self.old_password.append(new_password)
            return True
        return False    
        
    def get_password(self):
        if self.old_password:
            return self.old_password[-1]
        return None   
        
    def is_correct(self, new_password):
        return self.old_password[-1] == new_password


# Example Usage:
pm = PasswordManager(["password123", "securePass"])

print(pm.get_password())  # Output: "securePass"

print(pm.set_password("newPass"))  # Output: True (New password set)
print(pm.set_password("password123"))  # Output: False (Already used)

print(pm.is_correct("newPass"))  # Output: True
print(pm.is_correct("wrongPass"))  # Output: False            



